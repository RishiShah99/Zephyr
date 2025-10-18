@echo off
echo ============================================================
echo Zephyr - Virtual Environment Setup
echo ============================================================
echo.
echo This will:
echo 1. Create a Python virtual environment (venv)
echo 2. Install all required packages
echo 3. Set you up for success!
echo.
pause

echo.
echo [1/3] Creating virtual environment...
C:\Users\shahr\AppData\Local\Programs\Python\Python313\python.exe -m venv venv

echo.
echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/3] Installing packages...
echo Installing core packages (feedparser, keyboard, pyttsx3)...
pip install feedparser keyboard pyttsx3

echo.
echo Installing optional packages (this may take a few minutes)...
pip install requests spotipy

echo.
echo Installing Google packages for Calendar...
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

echo.
echo Installing AI packages...
pip install google-generativeai spacy

echo.
echo Installing News API...
pip install newsapi-python

echo.
echo Installing Speech Recognition...
pip install SpeechRecognition

echo.
echo Note: Porcupine (wake word) and PyAudio require special setup.
echo We'll skip these for now - see API_KEYS_GUIDE.md for instructions.
echo.

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Virtual environment created in: .\venv
echo.
echo To activate it in future sessions:
echo     venv\Scripts\activate
echo.
echo Next steps:
echo 1. Read API_KEYS_GUIDE.md to get your API keys
echo 2. Copy api_keys_example.py to api_keys.py and fill it in
echo 3. Run: python app.py
echo.
pause
