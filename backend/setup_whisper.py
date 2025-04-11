#!/usr/bin/env python3
"""
Setup script to clone and build whisper.cpp
"""
import os
import subprocess
import sys
import logging
from pathlib import Path

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

def run_command(cmd, cwd=None, check=True):
    """Run a shell command and log the output"""
    logger.info(f"Running command: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=check
        )
        logger.info(result.stdout)
        if result.stderr:
            logger.warning(result.stderr)
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with exit code {e.returncode}")
        logger.error(e.stderr)
        if check:
            sys.exit(1)
        return e

def clone_whisper_cpp():
    """Clone the whisper.cpp repository"""
    if WHISPER_CPP_DIR.exists():
        logger.info(f"whisper.cpp directory already exists at {WHISPER_CPP_DIR}")
        return
    
    logger.info("Cloning whisper.cpp repository...")
    run_command(["git", "clone", "https://github.com/ggml-org/whisper.cpp.git", str(WHISPER_CPP_DIR)])

def build_whisper_cpp():
    """Build whisper.cpp"""
    logger.info("Building whisper.cpp...")
    
    # Create build directory
    build_dir = WHISPER_CPP_DIR / "build"
    build_dir.mkdir(exist_ok=True)
    
    # Run CMake
    run_command(["cmake", ".."], cwd=build_dir)
    
    # Build
    run_command(["cmake", "--build", ".", "--config", "Release"], cwd=build_dir)
    
    # Check if the build was successful
    whisper_cli = build_dir / "bin" / "whisper-cli"
    if not whisper_cli.exists() and not (build_dir / "bin" / "whisper-cli.exe").exists():
        logger.error("Failed to build whisper-cli")
        sys.exit(1)
    
    logger.info("whisper.cpp built successfully")

def download_model():
    """Download the base.en model"""
    model_path = WHISPER_MODEL_DIR / "ggml-base.en.bin"
    if model_path.exists():
        logger.info(f"Model already exists at {model_path}")
        return
    
    logger.info("Downloading base.en model...")
    WHISPER_MODEL_DIR.mkdir(exist_ok=True)
    download_script = WHISPER_MODEL_DIR / "download-ggml-model.sh"
    
    if not download_script.exists():
        logger.error(f"Download script not found at {download_script}")
        sys.exit(1)
    
    run_command(["bash", str(download_script), "base.en"], cwd=WHISPER_CPP_DIR)
    
    if not model_path.exists():
        logger.error(f"Failed to download model to {model_path}")
        sys.exit(1)
    
    logger.info(f"Model downloaded to {model_path}")

def main():
    """Main function"""
    logger.info("Setting up whisper.cpp...")
    
    # Clone whisper.cpp
    clone_whisper_cpp()
    
    # Build whisper.cpp
    build_whisper_cpp()
    
    # Download model
    download_model()
    
    logger.info("whisper.cpp setup completed successfully")

if __name__ == "__main__":
    main()
