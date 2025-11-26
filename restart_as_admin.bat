@echo off
:: Restart Zephyr with Admin Rights
cd /d "%~dp0"

:: Kill existing Zephyr processes
taskkill /F /IM pythonw.exe /FI "WINDOWTITLE eq Zephyr*" 2>NUL
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Zephyr*" 2>NUL

:: Wait a moment
timeout /t 1 /nobreak >NUL

:: Start Zephyr with admin rights in background
powershell -Command "Start-Process '%~dp0venv\Scripts\pythonw.exe' -ArgumentList '%~dp0app.py' -Verb RunAs -WindowStyle Hidden"

echo Zephyr restarted with admin privileges!
echo Press Ctrl+Alt+Z to test the global hotkey.
pause
