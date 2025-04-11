#!/usr/bin/env python3
"""
Run script for the FastAPI backend
"""
import uvicorn
import logging
import argparse
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the FastAPI server"""
    parser = argparse.ArgumentParser(description="Run the Whisper.cpp FastAPI backend")
    parser.add_argument(
        "--host", 
        type=str, 
        default="127.0.0.1", 
        help="Host to bind the server to"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Port to bind the server to"
    )
    parser.add_argument(
        "--reload", 
        action="store_true", 
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()
    
    logger.info(f"Starting FastAPI server at {args.host}:{args.port}")
    uvicorn.run(
        "main:app", 
        host=args.host, 
        port=args.port, 
        reload=args.reload
    )

if __name__ == "__main__":
    main()
