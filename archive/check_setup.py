"""
Zephyr Setup Checker
Validates installed packages and API keys before running the full app.
"""
import sys
import importlib
from pathlib import Path

print("=" * 60)
print("Zephyr Setup Checker")
print("=" * 60)

# Check Python version
print(f"\n✓ Python version: {sys.version}")

# Required packages for minimal demo
CORE_PACKAGES = {
    "tkinter": "Built-in (GUI)",
    "threading": "Built-in (concurrency)",
    "json": "Built-in (config)",
}

OPTIONAL_PACKAGES = {
    "keyboard": "Global hotkey support",
    "pyttsx3": "Text-to-speech",
    "feedparser": "RSS news (offline)",
    "spotipy": "Spotify control",
    "requests": "HTTP requests (weather/news)",
    "newsapi": "News API fallback",
    "google.api_python_client": "Google Calendar",
    "pvporcupine": "Wake word detection",
    "pyaudio": "Audio input for wake word",
    "speech_recognition": "Voice input",
}

print("\n" + "=" * 60)
print("CHECKING PACKAGES")
print("=" * 60)

installed = []
missing = []

for pkg, desc in CORE_PACKAGES.items():
    try:
        if pkg == "tkinter":
            import tkinter
        else:
            importlib.import_module(pkg)
        print(f"✓ {pkg:30} - {desc}")
        installed.append(pkg)
    except Exception as e:
        print(f"✗ {pkg:30} - {desc} (ERROR: {e})")
        missing.append(pkg)

print("\nOptional packages:")
for pkg, desc in OPTIONAL_PACKAGES.items():
    try:
        importlib.import_module(pkg)
        print(f"✓ {pkg:30} - {desc}")
        installed.append(pkg)
    except Exception:
        print(f"✗ {pkg:30} - {desc} (not installed)")
        missing.append(pkg)

# Check API keys
print("\n" + "=" * 60)
print("CHECKING API KEYS")
print("=" * 60)

api_keys_exist = Path("api_keys.py").exists()
if not api_keys_exist:
    print("✗ api_keys.py not found")
    print("\n  Create api_keys.py with your keys:")
    print("  ACCESS_KEY = 'your_porcupine_key'")
    print("  WEATHER_API_KEY = 'your_weather_key'")
    print("  NEWS_API_KEY = 'your_news_key'")
    print("  SPOTIFY_CLIENT_ID = 'your_spotify_id'")
    print("  SPOTIFY_CLIENT_SECRET = 'your_spotify_secret'")
    print("  SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'")
    print("  GEMINI_API_KEY = 'your_gemini_key'")
else:
    print("✓ api_keys.py exists")
    try:
        import api_keys
        keys = [k for k in dir(api_keys) if not k.startswith('_')]
        print(f"  Found keys: {', '.join(keys)}")
    except Exception as e:
        print(f"  ⚠ Error importing api_keys: {e}")

# Recommendations
print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)

if missing:
    print("\nTo install missing packages:")
    print("\npip install feedparser keyboard pyttsx3")
    print("\nFor full features:")
    print("pip install -r requirements.txt")

print("\n✓ Minimal demo can run with: tkinter, threading, json")
print("  These are built-in and already available!")

print("\n" + "=" * 60)
print("NEXT STEPS")
print("=" * 60)
print("\n1. Install core packages:")
print("   pip install feedparser keyboard pyttsx3")
print("\n2. Create api_keys.py (optional for demo)")
print("\n3. Run minimal demo:")
print("   python demo_minimal.py")
print("\n4. Run full app:")
print("   python app.py")
print("\n" + "=" * 60)
