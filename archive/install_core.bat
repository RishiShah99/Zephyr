@echo off
echo ============================================================
echo Zephyr - Quick Install Script
echo ============================================================
echo.
echo This will install the CORE packages needed for Zephyr:
echo - feedparser (RSS news, no API key needed)
echo - keyboard (global hotkey)
echo - pyttsx3 (text-to-speech)
echo.
echo These packages enable most features without requiring API keys!
echo.
pause

echo.
echo Installing core packages...
echo.
pip install feedparser keyboard pyttsx3

echo.
echo ============================================================
echo Installation complete!
echo ============================================================
echo.
echo Next steps:
echo 1. (Optional) Copy api_keys_example.py to api_keys.py and add your keys
echo 2. Run: python app.py
echo.
echo Try these commands in the overlay:
echo - "new project test app"
echo - "list projects"
echo - "remember my name is Rishi"
echo - "recall"
echo - "wake up" (morning scene)
echo - "i'm home" (evening scene)
echo.
pause
