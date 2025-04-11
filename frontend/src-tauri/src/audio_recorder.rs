use anyhow::{anyhow, Result};
use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use cpal::{Sample, SampleFormat};
use hound::{SampleFormat as HoundSampleFormat, WavSpec, WavWriter};
use std::path::PathBuf;
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;
use temp_dir::TempDir;

// Global state for the recorder
pub struct AudioRecorder {
    recording: Arc<Mutex<bool>>,
    output_file: Arc<Mutex<Option<PathBuf>>>,
    temp_dir: TempDir,
}

impl AudioRecorder {
    pub fn new() -> Result<Self> {
        let temp_dir = TempDir::new()?;
        Ok(Self {
            recording: Arc::new(Mutex::new(false)),
            output_file: Arc::new(Mutex::new(None)),
            temp_dir,
        })
    }

    pub fn start_recording(&self) -> Result<PathBuf> {
        // Check if already recording
        let mut recording = self.recording.lock().unwrap();
        if *recording {
            return Err(anyhow!("Already recording"));
        }

        // Create a temporary WAV file
        let file_path = self.temp_dir.path().join(format!("recording_{}.wav", chrono::Utc::now().timestamp()));

        // Set recording state
        *recording = true;

        // Store the output file path
        let mut output_file = self.output_file.lock().unwrap();
        *output_file = Some(file_path.clone());

        // Start recording in a new thread
        let recording_clone = Arc::clone(&self.recording);
        let file_path_clone = file_path.clone();

        thread::spawn(move || {
            if let Err(err) = record_audio(&file_path_clone, recording_clone) {
                eprintln!("Error recording audio: {}", err);
            }
        });

        Ok(file_path)
    }

    pub fn stop_recording(&self) -> Result<Option<PathBuf>> {
        // Check if recording
        let mut recording = self.recording.lock().unwrap();
        if !*recording {
            return Ok(None);
        }

        // Stop recording
        *recording = false;

        // Wait a moment for the recording thread to finish
        thread::sleep(Duration::from_millis(500));

        // Return the output file path
        let output_file = self.output_file.lock().unwrap().clone();
        Ok(output_file)
    }

    pub fn get_recording_file(&self) -> Option<PathBuf> {
        self.output_file.lock().unwrap().clone()
    }
}

fn record_audio(output_path: &PathBuf, recording: Arc<Mutex<bool>>) -> Result<()> {
    // Get default host
    let host = cpal::default_host();

    // Get default input device
    let device = host.default_input_device()
        .ok_or_else(|| anyhow!("No input device available"))?;

    println!("Using input device: {}", device.name()?);

    // Get supported config
    let config = device.default_input_config()?;
    println!("Default input config: {:?}", config);

    // Create WAV writer
    let spec = WavSpec {
        channels: config.channels(),
        sample_rate: config.sample_rate().0,
        bits_per_sample: 16,
        sample_format: HoundSampleFormat::Int,
    };

    let writer = WavWriter::create(output_path, spec)?;
    let writer = Arc::new(Mutex::new(Some(writer)));

    // Create stream
    let err_fn = move |err| {
        eprintln!("an error occurred on the audio stream: {}", err);
    };

    let writer_clone = Arc::clone(&writer);
    let recording_clone = Arc::clone(&recording);

    let stream = match config.sample_format() {
        SampleFormat::I16 => device.build_input_stream(
            &config.into(),
            move |data: &[i16], _: &_| {
                // Check if still recording
                if !*recording_clone.lock().unwrap() {
                    return;
                }

                // Write samples to WAV file
                if let Some(writer) = &mut *writer_clone.lock().unwrap() {
                    for &sample in data {
                        if writer.write_sample(sample).is_err() {
                            break;
                        }
                    }
                }
            },
            err_fn,
            None,
        )?,
        SampleFormat::U16 => device.build_input_stream(
            &config.into(),
            move |data: &[u16], _: &_| {
                // Check if still recording
                if !*recording_clone.lock().unwrap() {
                    return;
                }

                // Write samples to WAV file
                if let Some(writer) = &mut *writer_clone.lock().unwrap() {
                    for &sample in data {
                        if writer.write_sample(i16::from_sample(sample)).is_err() {
                            break;
                        }
                    }
                }
            },
            err_fn,
            None,
        )?,
        SampleFormat::F32 => device.build_input_stream(
            &config.into(),
            move |data: &[f32], _: &_| {
                // Check if still recording
                if !*recording_clone.lock().unwrap() {
                    return;
                }

                // Write samples to WAV file
                if let Some(writer) = &mut *writer_clone.lock().unwrap() {
                    for &sample in data {
                        if writer.write_sample(i16::from_sample(sample)).is_err() {
                            break;
                        }
                    }
                }
            },
            err_fn,
            None,
        )?,
        _ => return Err(anyhow!("Unsupported sample format")),
    };

    // Start the stream
    stream.play()?;

    // Wait until recording is stopped
    while *recording.lock().unwrap() {
        thread::sleep(Duration::from_millis(100));
    }

    // Finalize the WAV file
    let mut writer_lock = writer.lock().unwrap();
    if let Some(writer) = writer_lock.take() {
        writer.finalize()?;
    }

    Ok(())
}

// Helper function to send the audio file to the backend for transcription
pub async fn transcribe_audio(file_path: &PathBuf, backend_url: &str) -> Result<serde_json::Value> {
    // Create a multipart form with the audio file
    let client = reqwest::Client::new();

    // Create a file part
    let file_bytes = std::fs::read(file_path)?;
    let file_part = reqwest::multipart::Part::bytes(file_bytes)
        .file_name(file_path.file_name().unwrap_or_default().to_string_lossy().to_string())
        .mime_str("audio/wav")?;

    // Create the form with the file part
    let form = reqwest::multipart::Form::new()
        .part("file", file_part);

    let response = client.post(&format!("{}/transcribe", backend_url))
        .multipart(form)
        .send()
        .await?;

    if !response.status().is_success() {
        return Err(anyhow!("Failed to transcribe audio: HTTP {}", response.status()));
    }

    // Parse the JSON response
    let json: serde_json::Value = response.json().await?;

    Ok(json)
}
