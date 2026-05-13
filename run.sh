#!/bin/bash

# Email Management System - Startup Script

echo "================================"
echo "Email Management System"
echo "================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
if [ ! -d "venv/lib/python3.*/site-packages/flask" ]; then
    echo "Installing dependencies..."
    python3 -m pip install -r requirements.txt
fi

# Run the application
echo ""
echo "Starting Flask application..."
echo "Access the app at: http://localhost:5000"
echo ""
python3 app.py
