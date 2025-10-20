# Zephyr

Zephyr is a keyboard-activated AI assistant for Windows that provides natural language interaction with your computer. Press Ctrl+Alt+Z from anywhere to open a minimal overlay interface and interact with various system functions through conversation.

## Overview

Zephyr uses Groq's LLM API to understand natural language commands and execute actions like controlling Spotify, checking weather, reading news, and managing projects. The interface is designed to be unobtrusive, appearing only when summoned via hotkey and disappearing after completing a task.

## Architecture

The system consists of several core components:

- `app.py` - Main entry point that registers the global hotkey and manages the UI lifecycle
- `ui.py` - Tkinter-based overlay interface with minimal dark theme
- `assistant.py` - Command router that processes user input and delegates to appropriate handlers
- `groq_nlp.py` - Natural language understanding via Groq's Llama 3.1 8B model
- `gemini_nlp.py` - Alternative NLP backend using Google Gemini (fallback option)

Feature modules handle specific domains:
- `spotify.py` - Music playback control via Spotipy
- `weather.py` - Weather information via WeatherAPI
- `news_rss.py` - News aggregation from RSS feeds
- `planner.py` - Calendar event management via Google Calendar API
- `projects.py` - Local project tracking with JSON storage
- `memory.py` - Simple fact storage and retrieval system
- `workspace.py` - Development workspace launcher
- `scenes.py` - Smart home scene execution

## Setup

Requirements:
- Python 3.8+
- Windows OS (uses keyboard library for global hotkey)
- API keys for Groq and optional services (Spotify, WeatherAPI, etc.)

Installation:
```powershell
git clone https://github.com/RishiShah99/Zephyr.git
cd Zephyr
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Configuration:
- Add your Groq API key to `api_keys.py`
- Optionally add keys for Spotify, WeatherAPI, and other services
- Adjust settings in `config.json` (hotkey, theme, etc.)

## Usage

Run the assistant:
```powershell
python app.py
```

Press Ctrl+Alt+Z to open the interface. Type naturally:
- "play bohemian rhapsody"
- "weather in london"
- "news about technology"
- "create project portfolio website"
- "tell me about quantum computing"

The interface dismisses automatically after responding. Press Escape to close manually.

## Background Execution

To run Zephyr on startup:
1. The included `Zephyr.bat` script handles background execution
2. Place it in your Windows Startup folder: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
3. Uses `pythonw.exe` for windowless operation

## API Integration

Zephyr uses Groq's free tier (14,400 requests/day) for natural language understanding. The `llama-3.1-8b-instant` model provides fast inference suitable for real-time interaction.

Optional integrations:
- Spotify: Requires OAuth setup via developer dashboard
- WeatherAPI: Free tier provides current conditions
- Google Calendar: Requires OAuth credentials
- News: Uses public RSS feeds (no key required)

## Technical Notes

The NLP system uses a structured prompt that teaches the model about available intents and expected JSON response format. Commands are parsed into intent + entities, then routed to appropriate handlers. For simple pattern matching (when AI is disabled), regex-based fallback parsing is available.

The UI uses Tkinter with custom styling to achieve a minimal dark theme. Window positioning, auto-resize, and dynamic scrollbar behavior are handled to maintain a clean appearance.

Data is stored locally in JSON files under the `data/` directory. No cloud storage or telemetry is implemented.

🔗 https://developer.spotify.com/dashboard
→ Control your music

**Optional:** NewsAPI, Google Calendar
