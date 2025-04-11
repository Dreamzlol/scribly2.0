#!/bin/bash

# Start script for Scribly 2.0
# This script starts both the backend and frontend

# Function to handle cleanup on exit
cleanup() {
    echo "Shutting down..."
    
    # Kill the backend process
    if [ ! -z "$BACKEND_PID" ]; then
        echo "Stopping backend (PID: $BACKEND_PID)"
        kill $BACKEND_PID 2>/dev/null
    fi
    
    # Kill the frontend process
    if [ ! -z "$FRONTEND_PID" ]; then
        echo "Stopping frontend (PID: $FRONTEND_PID)"
        kill $FRONTEND_PID 2>/dev/null
    fi
    
    exit 0
}

# Register the cleanup function for SIGINT and SIGTERM
trap cleanup SIGINT SIGTERM

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is required but not installed. Please install Node.js and try again."
    exit 1
fi

# Check if SoX is installed
if ! command -v sox &> /dev/null; then
    echo "SoX is required but not installed. Please install SoX using 'brew install sox' and try again."
    exit 1
fi

# Check if the backend directory exists
if [ ! -d "backend" ]; then
    echo "Backend directory not found. Make sure you're running this script from the project root."
    exit 1
fi

# Check if the frontend directory exists
if [ ! -d "frontend" ]; then
    echo "Frontend directory not found. Make sure you're running this script from the project root."
    exit 1
fi

# Start the backend
echo "Starting backend..."
cd backend
python3 run.py &
BACKEND_PID=$!
cd ..

# Wait a moment for the backend to start
sleep 2

# Check if the backend is running
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo "Failed to start the backend. Check the backend logs for errors."
    exit 1
fi

echo "Backend started with PID: $BACKEND_PID"

# Start the frontend
echo "Starting frontend..."
cd frontend
npm run tauri dev &
FRONTEND_PID=$!
cd ..

# Wait for the frontend to exit
wait $FRONTEND_PID

# Clean up when the frontend exits
cleanup
