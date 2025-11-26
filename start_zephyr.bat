@echo off
echo ===================================
echo     Starting Zephyr System
echo ===================================
echo.

REM Kill any existing Python processes to prevent duplicates
echo Cleaning up old processes...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM pythonw.exe >nul 2>&1
timeout /t 2 /nobreak >nul

REM Start Tiny Zephyr (API server starts automatically)
echo Starting Tiny Zephyr...
echo - Press Ctrl+Alt+Z to open popup
echo - Click "Expand" button to launch dashboard
echo.

REM Check if venv exists
if exist venv\Scripts\pythonw.exe (
    start "" venv\Scripts\pythonw.exe app.py
) else if exist venv\Scripts\python.exe (
    start "" venv\Scripts\python.exe app.py
) else (
    echo WARNING: Virtual environment not found!
    echo Trying system Python...
    start "" pythonw.exe app.py
)

timeout /t 3 /nobreak >nul

echo.
echo ===================================
echo  Zephyr is now running!
echo ===================================
echo.
echo  Quick Guide:
echo   - Press Ctrl+Alt+Z anywhere to open Zephyr
echo   - Click "Expand" to launch full dashboard
echo   - API Server: http://localhost:5000
echo   - Check system tray for Zephyr icon
echo.
echo ===================================
echo.
echo Press any key to close this window...
pause >nul
