#!/bin/bash
# Quick setup script for AI Learn

echo "🤖 AI Learn - Setup Script"
echo "=========================="

# Check Python version
echo "Checking Python installation..."
python --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application, run:"
echo "  streamlit run app.py"
echo ""
echo "The app will open at http://localhost:8501"
