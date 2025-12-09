#!/bin/bash

# Yí Restaurant Website Launch Script

echo "🍽️  Starting Yí Restaurant Website..."
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies. Please check the error messages above."
    exit 1
fi

# Start the server
echo "🚀 Starting FastAPI server..."
echo "Website will be available at: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 main.py
