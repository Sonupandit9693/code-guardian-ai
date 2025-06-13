#!/bin/bash

# AI Code Review Assistant - Local Development Setup

echo "🚀 Setting up AI Code Review Assistant for local development"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo -e "${RED}Error: Please run this script from the project root directory${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Installing backend dependencies...${NC}"
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${GREEN}✅ Backend dependencies installed${NC}"

# Go back to root and setup frontend
cd ..
echo -e "${YELLOW}📦 Installing frontend dependencies...${NC}"
cd frontend

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo -e "${RED}Error: Node.js is not installed. Please install Node.js 18 or later.${NC}"
    exit 1
fi

# Install npm dependencies
npm install

echo -e "${GREEN}✅ Frontend dependencies installed${NC}"

# Go back to root
cd ..

echo -e "${GREEN}🎉 Setup complete!${NC}"
echo -e "${YELLOW}To start the development servers:${NC}"
echo "1. Backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo -e "${YELLOW}Or use the provided scripts:${NC}"
echo "./scripts/start-backend.sh"
echo "./scripts/start-frontend.sh"

