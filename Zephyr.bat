@echo off
:: Zephyr - Silent Background Launcher with Admin Rights
:: This starts Zephyr completely in the background

cd /d "%~dp0"

:: Check if already running
tasklist /FI "IMAGENAME eq pythonw.exe" 2>NUL | find /I "pythonw.exe">NUL
if "%ERRORLEVEL%"=="0" (
    exit /b
)

:: Start with admin rights, completely hidden
powershell -WindowStyle Hidden -Command "Start-Process '%~dp0venv\Scripts\pythonw.exe' -ArgumentList '%~dp0app.py' -Verb RunAs -WindowStyle Hidden"

exit
