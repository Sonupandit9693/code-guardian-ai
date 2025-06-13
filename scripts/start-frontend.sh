#!/bin/bash

# Start the frontend development server

echo "🚀 Starting AI Code Review Assistant Frontend"

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Node modules not found. Please run ./scripts/dev-setup.sh first"
    exit 1
fi

# Set environment variables for development
export NEXT_PUBLIC_API_URL="http://localhost:8000"
export NODE_ENV="development"

echo "Starting Next.js development server on http://localhost:3000"
echo "Backend API should be running on http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"

# Start the development server
npm run dev

