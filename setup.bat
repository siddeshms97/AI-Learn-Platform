@echo off
REM Quick setup script for AI Learn (Windows)

echo 🤖 AI Learn - Setup Script
echo ==========================

echo Checking Python installation...
python --version

echo.
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo To start the application, run:
echo   streamlit run app.py
echo.
echo The app will open at http://localhost:8501
