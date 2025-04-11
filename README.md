# Scribly 2.0 - Audio Transcription with Whisper.cpp

A Tauri desktop application for macOS that records system audio and microphone input, then transcribes it using Whisper.cpp.

## Features

- Record microphone input directly in the Tauri app using Rust
- Transcribe audio using Whisper.cpp
- Display transcription results with timestamps
- Cross-platform desktop application built with Tauri and SvelteKit

## Prerequisites

- macOS (this application is designed specifically for macOS)
- Node.js 16+ and npm
- Python 3.8+
- Rust and Cargo
- CMake

## Project Structure

- `frontend/`: Tauri + SvelteKit frontend application
- `backend/`: Python FastAPI backend for audio recording and transcription

## Setup

### 1. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create a Python virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Set up Whisper.cpp (clone, build, and download model)
python setup_whisper.py
```

### 2. Frontend Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install npm dependencies
npm install
```

## Running the Application

### 1. Start the Backend

```bash
# In the backend directory (with virtual environment activated)
python run.py
```

### 2. Start the Frontend

```bash
# In the frontend directory
npm run tauri dev
```

## Building for Production

```bash
# In the frontend directory
npm run tauri build
```

This will create a production-ready application in the `frontend/src-tauri/target/release` directory.

## How It Works

1. The frontend Tauri application provides a user interface for controlling audio recording and displaying transcription results.
2. Audio recording is handled directly in the Tauri app using Rust and the cpal library.
3. The backend FastAPI server handles transcription using Whisper.cpp.
4. When you start recording, the Tauri app captures microphone input.
5. When you stop recording and request transcription, the audio file is sent to the backend for processing with Whisper.cpp.
6. The transcription results are sent back to the frontend and displayed with timestamps.

## Troubleshooting

- If you encounter issues with audio recording, check your microphone settings and permissions.
- If transcription fails, check if Whisper.cpp is built correctly and the model is downloaded.

## License

This project is licensed under the MIT License.