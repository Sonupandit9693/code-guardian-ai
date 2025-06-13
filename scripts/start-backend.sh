#!/bin/bash

# Start the backend development server

echo "🚀 Starting AI Code Review Assistant Backend"

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run ./scripts/dev-setup.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Set environment variables for development
export DATABASE_URL="sqlite:///./dev.db"
export MONGODB_URL="mongodb://localhost:27017/codereviewer"
export REDIS_URL="redis://localhost:6379"
export SECRET_KEY="dev-secret-key-change-in-production"
export DEBUG="true"

echo "Starting FastAPI server on http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo "Alternative docs: http://localhost:8000/redoc"
echo ""
echo "Press Ctrl+C to stop the server"

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

