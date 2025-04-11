# Whisper.cpp FastAPI Backend

This is the backend for the Tauri application that uses Whisper.cpp for transcription of audio recordings.

## Features

- Record system audio and microphone input on macOS
- Transcribe audio using Whisper.cpp
- Provide a REST API for the frontend to interact with

## Prerequisites

- Python 3.8+
- SoX for audio recording (`brew install sox`)
- A virtual audio device like BlackHole for capturing system audio on macOS
- CMake for building Whisper.cpp

## Setup

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Set up Whisper.cpp:

```bash
python setup_whisper.py
```

This will:
- Clone the Whisper.cpp repository
- Build the CLI and server components
- Download the base.en model

## Running the Backend

Start the FastAPI server:

```bash
python run.py
```

By default, the server will run on `http://127.0.0.1:8000`.

## API Endpoints

- `GET /`: Root endpoint, returns a welcome message
- `GET /check-whisper`: Check if Whisper.cpp is installed and built correctly
- `POST /start-recording`: Start recording audio
- `POST /stop-recording`: Stop recording audio
- `POST /transcribe`: Transcribe the recorded audio

## Testing

You can test the audio recording functionality separately:

```bash
python audio_recorder.py
```

And the transcription functionality:

```bash
python transcriber.py
```

## Troubleshooting

- If you encounter issues with audio recording, make sure SoX is installed and working correctly.
- For system audio capture, you need a virtual audio device like BlackHole configured.
- If transcription fails, check if Whisper.cpp is built correctly and the model is downloaded.

## License

This project is licensed under the MIT License.
