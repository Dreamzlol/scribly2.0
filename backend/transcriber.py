#!/usr/bin/env python3
"""
Transcriber module to handle whisper.cpp transcription
"""
import os
import subprocess
import tempfile
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Path to the whisper.cpp directory
BACKEND_DIR = Path(__file__).parent.absolute()
WHISPER_CPP_DIR = BACKEND_DIR / "whisper.cpp"
WHISPER_MODEL_DIR = WHISPER_CPP_DIR / "models"
WHISPER_MODEL_PATH = WHISPER_MODEL_DIR / "ggml-base.en.bin"

class Transcriber:
    """Class to handle whisper.cpp transcription"""
    
    def __init__(self, model_name="base.en"):
        """
        Initialize the transcriber
        
        Args:
            model_name: Name of the whisper model to use
        """
        self.model_name = model_name
        self.model_path = WHISPER_MODEL_DIR / f"ggml-{model_name}.bin"
        self.whisper_cli = WHISPER_CPP_DIR / "build" / "bin" / "whisper-cli"
        
        # Check if whisper.cpp is installed
        if not WHISPER_CPP_DIR.exists():
            logger.error("whisper.cpp directory not found. Please run setup_whisper.py first.")
        
        # Check if the model exists
        if not self.model_path.exists():
            logger.warning(f"Model {self.model_path} not found. Will attempt to download it when needed.")
    
    def ensure_model(self) -> bool:
        """
        Ensure the model is downloaded
        
        Returns:
            bool: True if the model is available, False otherwise
        """
        if self.model_path.exists():
            return True
        
        logger.info(f"Downloading model {self.model_name}...")
        download_script = WHISPER_MODEL_DIR / "download-ggml-model.sh"
        
        if not download_script.exists():
            logger.error(f"Download script not found at {download_script}")
            return False
        
        try:
            subprocess.run(
                ["bash", str(download_script), self.model_name], 
                cwd=WHISPER_CPP_DIR, 
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            return self.model_path.exists()
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to download model: {e.stderr}")
            return False
    
    def transcribe(self, audio_file: str) -> Tuple[bool, Dict[str, Any]]:
        """
        Transcribe an audio file using whisper.cpp
        
        Args:
            audio_file: Path to the audio file to transcribe
            
        Returns:
            Tuple[bool, Dict]: Success status and transcription data or error message
        """
        if not os.path.exists(audio_file):
            return False, {"error": f"Audio file not found: {audio_file}"}
        
        # Ensure the model is downloaded
        if not self.ensure_model():
            return False, {"error": f"Failed to download model {self.model_name}"}
        
        # Check if whisper-cli exists
        if not self.whisper_cli.exists() and not (WHISPER_CPP_DIR / "build" / "bin" / "whisper-cli.exe").exists():
            return False, {"error": "whisper-cli not found. Please build whisper.cpp first."}
        
        try:
            # Create a temporary file for the JSON output
            with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as json_file:
                json_file_path = json_file.name
            
            # Run whisper-cli with JSON output
            cmd = [
                str(self.whisper_cli),
                "-m", str(self.model_path),
                "-f", audio_file,
                "-oj",  # Output JSON
                "-of", os.path.splitext(json_file_path)[0]  # Output file path without extension
            ]
            
            logger.info(f"Running transcription: {' '.join(cmd)}")
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            
            # Read the JSON output
            with open(json_file_path, "r") as f:
                transcription_data = json.load(f)
            
            # Clean up the temporary file
            os.unlink(json_file_path)
            
            # Extract the full text
            full_text = " ".join([segment.get("text", "") for segment in transcription_data.get("segments", [])])
            
            return True, {
                "text": full_text,
                "segments": transcription_data.get("segments", []),
                "language": transcription_data.get("language", "en")
            }
        
        except subprocess.CalledProcessError as e:
            logger.error(f"Transcription process error: {e.stderr}")
            return False, {"error": f"Transcription failed: {e.stderr}"}
        
        except Exception as e:
            logger.error(f"Transcription error: {str(e)}")
            return False, {"error": f"Transcription failed: {str(e)}"}
    
    def check_status(self) -> Dict[str, Any]:
        """
        Check the status of the transcriber
        
        Returns:
            Dict: Status information
        """
        return {
            "whisper_cpp_dir_exists": WHISPER_CPP_DIR.exists(),
            "whisper_cli_exists": self.whisper_cli.exists(),
            "model_exists": self.model_path.exists(),
            "model_name": self.model_name,
            "status": "ready" if self.whisper_cli.exists() and self.model_path.exists() else "not_ready"
        }

# Singleton instance
transcriber = Transcriber()

def transcribe_audio(audio_file: str) -> Tuple[bool, Dict[str, Any]]:
    """
    Transcribe an audio file
    
    Args:
        audio_file: Path to the audio file
        
    Returns:
        Tuple[bool, Dict]: Success status and transcription data or error
    """
    return transcriber.transcribe(audio_file)

def check_status() -> Dict[str, Any]:
    """
    Check the status of the transcriber
    
    Returns:
        Dict: Status information
    """
    return transcriber.check_status()

if __name__ == "__main__":
    # Simple test
    status = check_status()
    print(f"Transcriber status: {status}")
    
    if status["status"] == "ready":
        # Test with a sample audio file if available
        sample_file = WHISPER_CPP_DIR / "samples" / "jfk.wav"
        if sample_file.exists():
            print(f"Transcribing sample file: {sample_file}")
            success, result = transcribe_audio(str(sample_file))
            if success:
                print(f"Transcription: {result['text']}")
            else:
                print(f"Transcription failed: {result['error']}")
        else:
            print(f"Sample file not found: {sample_file}")
    else:
        print("Transcriber not ready. Please run setup_whisper.py first.")
