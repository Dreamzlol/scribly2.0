from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import subprocess
import tempfile
import json
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Whisper.cpp Transcription API")

# Add CORS middleware to allow requests from the Tauri app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, you should specify the exact origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the whisper.cpp directory
WHISPER_CPP_DIR = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "whisper.cpp")
WHISPER_MODEL_DIR = os.path.join(WHISPER_CPP_DIR, "models")
WHISPER_MODEL_PATH = os.path.join(WHISPER_MODEL_DIR, "ggml-base.en.bin")

# Check if whisper.cpp is installed
if not os.path.exists(WHISPER_CPP_DIR):
    logger.error(
        "whisper.cpp directory not found. Please clone and build it first.")

# Ensure the model directory exists
os.makedirs(WHISPER_MODEL_DIR, exist_ok=True)


class TranscriptionResponse(BaseModel):
    text: str
    segments: Optional[list] = None
    success: bool = True
    error: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Whisper.cpp Transcription API"}


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    try:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_file_path = temp_file.name
            # Write the uploaded file content to the temporary file
            content = await file.read()
            temp_file.write(content)

        # Check if the model exists, if not download it
        if not os.path.exists(WHISPER_MODEL_PATH):
            logger.info("Downloading Whisper model...")
            download_script = os.path.join(
                WHISPER_CPP_DIR, "models", "download-ggml-model.sh")
            subprocess.run(
                ["bash", download_script, "base.en"],
                cwd=WHISPER_CPP_DIR,
                check=True
            )

        # Path to the whisper-cli executable
        whisper_cli = os.path.join(
            WHISPER_CPP_DIR, "build", "bin", "whisper-cli")

        if not os.path.exists(whisper_cli):
            raise HTTPException(
                status_code=500,
                detail="whisper-cli not found. Please build whisper.cpp first."
            )

        # Create a temporary file for the JSON output
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as json_file:
            json_file_path = json_file.name

        # Run whisper-cli with JSON output
        cmd = [
            whisper_cli,
            "-m", WHISPER_MODEL_PATH,
            "-f", temp_file_path,
            "-oj",  # Output JSON
            # Output file path without extension
            "-of", os.path.splitext(json_file_path)[0]
        ]

        logger.info(f"Running transcription: {' '.join(cmd)}")
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Read the JSON output
        with open(json_file_path, "r") as f:
            transcription_data = json.load(f)

        # Clean up temporary files in the background
        def cleanup_files():
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

            if os.path.exists(json_file_path):
                os.unlink(json_file_path)

        if background_tasks:
            background_tasks.add_task(cleanup_files)
        else:
            cleanup_files()

        # Extract the full text and segments
        full_text = " ".join([segment.get("text", "")
                             for segment in transcription_data.get("segments", [])])

        return TranscriptionResponse(
            text=full_text,
            segments=transcription_data.get("segments", []),
            success=True
        )

    except subprocess.CalledProcessError as e:
        logger.error(f"Transcription process error: {e.stderr}")
        return TranscriptionResponse(
            text="",
            success=False,
            error=f"Transcription failed: {e.stderr}"
        )

    except Exception as e:
        logger.error(f"Transcription error: {str(e)}")
        return TranscriptionResponse(
            text="",
            success=False,
            error=f"Transcription failed: {str(e)}"
        )


@app.get("/check-whisper")
async def check_whisper():
    """Check if whisper.cpp is installed and built correctly"""
    whisper_cli = os.path.join(WHISPER_CPP_DIR, "build", "bin", "whisper-cli")
    model_exists = os.path.exists(WHISPER_MODEL_PATH)

    return {
        "whisper_cpp_dir_exists": os.path.exists(WHISPER_CPP_DIR),
        "whisper_cli_exists": os.path.exists(whisper_cli),
        "model_exists": model_exists,
        "status": "ready" if os.path.exists(whisper_cli) and model_exists else "not_ready"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
