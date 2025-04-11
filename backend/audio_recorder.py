#!/usr/bin/env python3
"""
Audio recorder module for macOS to capture system audio and microphone
"""
import os
import subprocess
import tempfile
import logging
import time
import signal
from typing import Optional, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class AudioRecorder:
    """Class to handle audio recording on macOS"""
    
    def __init__(self):
        self.recording_process = None
        self.output_file = None
    
    def start_recording(self) -> Tuple[bool, str]:
        """
        Start recording system audio and microphone
        
        Returns:
            Tuple[bool, str]: Success status and message or file path
        """
        # Stop any existing recording
        if self.recording_process is not None:
            self.stop_recording()
        
        # Create a temporary file for the recording
        self.output_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        self.output_file.close()
        
        try:
            # Check if 'rec' command is available (part of SoX)
            try:
                subprocess.run(["which", "rec"], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                return False, "SoX 'rec' command not found. Please install SoX: brew install sox"
            
            # Start recording both system audio and microphone on macOS
            # This requires SoX and a virtual audio device like BlackHole for system audio
            cmd = [
                "rec", 
                "-r", "16000",  # Sample rate required by Whisper
                "-c", "1",      # Mono audio
                "-b", "16",     # 16-bit depth
                self.output_file.name,
                "remix", "1,2"  # Mix all channels
            ]
            
            logger.info(f"Starting recording to {self.output_file.name}")
            self.recording_process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )
            
            return True, self.output_file.name
        
        except Exception as e:
            logger.error(f"Error starting recording: {str(e)}")
            if self.output_file and os.path.exists(self.output_file.name):
                os.unlink(self.output_file.name)
            return False, f"Failed to start recording: {str(e)}"
    
    def stop_recording(self) -> Tuple[bool, str]:
        """
        Stop the current recording
        
        Returns:
            Tuple[bool, str]: Success status and message or file path
        """
        if self.recording_process is None:
            return True, "No recording in progress"
        
        try:
            # Terminate the recording process
            self.recording_process.terminate()
            try:
                self.recording_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                # Force kill if it doesn't terminate gracefully
                self.recording_process.kill()
                self.recording_process.wait()
            
            self.recording_process = None
            
            if self.output_file and os.path.exists(self.output_file.name):
                logger.info(f"Recording stopped, saved to {self.output_file.name}")
                return True, self.output_file.name
            else:
                return False, "Recording file not found"
        
        except Exception as e:
            logger.error(f"Error stopping recording: {str(e)}")
            return False, f"Failed to stop recording: {str(e)}"
    
    def get_recording_file(self) -> Optional[str]:
        """
        Get the path to the current recording file
        
        Returns:
            Optional[str]: Path to the recording file or None
        """
        if self.output_file and os.path.exists(self.output_file.name):
            return self.output_file.name
        return None
    
    def cleanup(self):
        """Clean up any temporary files"""
        if self.recording_process is not None:
            self.stop_recording()
        
        if self.output_file and os.path.exists(self.output_file.name):
            try:
                os.unlink(self.output_file.name)
                logger.info(f"Removed temporary file {self.output_file.name}")
            except Exception as e:
                logger.error(f"Error removing temporary file: {str(e)}")

# Singleton instance
recorder = AudioRecorder()

def start_recording() -> Tuple[bool, str]:
    """Start recording audio"""
    return recorder.start_recording()

def stop_recording() -> Tuple[bool, str]:
    """Stop recording audio"""
    return recorder.stop_recording()

def get_recording_file() -> Optional[str]:
    """Get the current recording file path"""
    return recorder.get_recording_file()

def cleanup():
    """Clean up resources"""
    recorder.cleanup()

# Handle cleanup on exit
def signal_handler(sig, frame):
    """Signal handler for cleanup"""
    logger.info("Received signal to exit, cleaning up...")
    cleanup()
    exit(0)

# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    # Simple test
    print("Starting recording for 5 seconds...")
    success, message = start_recording()
    if success:
        print(f"Recording started: {message}")
        time.sleep(5)
        success, file_path = stop_recording()
        if success:
            print(f"Recording stopped, saved to: {file_path}")
            print(f"File exists: {os.path.exists(file_path)}")
        else:
            print(f"Failed to stop recording: {message}")
    else:
        print(f"Failed to start recording: {message}")
    
    cleanup()
