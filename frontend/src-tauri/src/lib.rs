// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
use std::sync::Mutex;
use serde::{Serialize, Deserialize};

mod audio_recorder;
use audio_recorder::AudioRecorder;

// Global state for the audio recorder
struct AppState {
    recorder: Mutex<Option<AudioRecorder>>,
    backend_url: String,
}

#[derive(Serialize, Deserialize)]
struct RecordingResponse {
    success: bool,
    file_path: Option<String>,
    error: Option<String>,
}

#[derive(Serialize, Deserialize)]
struct TranscriptionResponse {
    success: bool,
    text: String,
    error: Option<String>,
    segments: Option<serde_json::Value>,
}

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
async fn start_recording(state: tauri::State<'_, AppState>) -> Result<RecordingResponse, String> {
    // This function doesn't use await, so we don't need to worry about Send trait issues
    let mut recorder_lock = state.recorder.lock().unwrap();

    // Initialize recorder if not already initialized
    if recorder_lock.is_none() {
        match AudioRecorder::new() {
            Ok(recorder) => *recorder_lock = Some(recorder),
            Err(err) => return Ok(RecordingResponse {
                success: false,
                file_path: None,
                error: Some(format!("Failed to initialize recorder: {}", err)),
            }),
        }
    }

    // Start recording
    if let Some(recorder) = &*recorder_lock {
        match recorder.start_recording() {
            Ok(file_path) => Ok(RecordingResponse {
                success: true,
                file_path: Some(file_path.to_string_lossy().to_string()),
                error: None,
            }),
            Err(err) => Ok(RecordingResponse {
                success: false,
                file_path: None,
                error: Some(format!("Failed to start recording: {}", err)),
            }),
        }
    } else {
        Ok(RecordingResponse {
            success: false,
            file_path: None,
            error: Some("Recorder not initialized".to_string()),
        })
    }
}

#[tauri::command]
async fn stop_recording(state: tauri::State<'_, AppState>) -> Result<RecordingResponse, String> {
    // This function doesn't use await, so we don't need to worry about Send trait issues
    let recorder_lock = state.recorder.lock().unwrap();

    if let Some(recorder) = &*recorder_lock {
        match recorder.stop_recording() {
            Ok(Some(file_path)) => Ok(RecordingResponse {
                success: true,
                file_path: Some(file_path.to_string_lossy().to_string()),
                error: None,
            }),
            Ok(None) => Ok(RecordingResponse {
                success: false,
                file_path: None,
                error: Some("Not recording".to_string()),
            }),
            Err(err) => Ok(RecordingResponse {
                success: false,
                file_path: None,
                error: Some(format!("Failed to stop recording: {}", err)),
            }),
        }
    } else {
        Ok(RecordingResponse {
            success: false,
            file_path: None,
            error: Some("Recorder not initialized".to_string()),
        })
    }
}

#[tauri::command]
async fn transcribe_audio(state: tauri::State<'_, AppState>) -> Result<TranscriptionResponse, String> {
    // Get the file path and backend URL before releasing the lock
    let file_path_option = {
        let recorder_lock = state.recorder.lock().unwrap();
        if let Some(recorder) = &*recorder_lock {
            recorder.get_recording_file()
        } else {
            return Ok(TranscriptionResponse {
                success: false,
                text: String::new(),
                error: Some("Recorder not initialized".to_string()),
                segments: None,
            });
        }
    };

    let backend_url = state.backend_url.clone();

    // Now we can use await without holding the lock
    if let Some(file_path) = file_path_option {
        match audio_recorder::transcribe_audio(&file_path, &backend_url).await {
            Ok(json) => {
                // Extract the text and segments from the JSON response
                let text = json["text"].as_str().unwrap_or("").to_string();
                let success = json["success"].as_bool().unwrap_or(false);
                let error = json["error"].as_str().map(|s| s.to_string());

                // Convert segments to a format that can be serialized to JSON
                let segments = if json["segments"].as_array().is_some() {
                    Some(json["segments"].clone())
                } else {
                    None
                };

                Ok(TranscriptionResponse {
                    success,
                    text,
                    error,
                    segments,
                })
            },
            Err(err) => Ok(TranscriptionResponse {
                success: false,
                text: String::new(),
                error: Some(format!("Failed to transcribe audio: {}", err)),
                segments: None,
            }),
        }
    } else {
        Ok(TranscriptionResponse {
            success: false,
            text: String::new(),
            error: Some("No recording available".to_string()),
            segments: None,
        })
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    let app_state = AppState {
        recorder: Mutex::new(None),
        backend_url: "http://127.0.0.1:8000".to_string(),
    };

    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .manage(app_state)
        .invoke_handler(tauri::generate_handler![greet, start_recording, stop_recording, transcribe_audio])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
