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

📖 See [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) for detailed setup!

---

## 🎮 USAGE

```powershell
# Start Zephyr
python app.py

# You'll see:
"Hotkey registered: ctrl+alt+z"

# Press Ctrl+Alt+Z from anywhere!
# Beautiful holographic interface slides in

# Talk naturally:
"play some music"
"weather in london"  
"create project My Blog"
"tell me about quantum physics"

# Press Escape or Ctrl+Alt+Z to dismiss
```

---

## 📦 FEATURES

✅ Natural language understanding (Gemini AI)  
✅ Holographic transparent UI with animations  
✅ Spotify music control  
✅ Weather for any city  
✅ News & information  
✅ Project tracking  
✅ Memory system  
✅ Google Calendar integration  
✅ Dev workspace launcher  
✅ Automation scenes  
✅ General chat & Q&A  
✅ Privacy-first (local storage)  
✅ Works partially offline  

---

## 🛠️ REQUIREMENTS

- **Python 3.13+**
- **Windows** (PowerShell)
- **Gemini API key** (free!)
- **Optional:** Spotify, WeatherAPI, NewsAPI keys

---

## 📚 DOCUMENTATION

- **[ZEPHYR_CAPABILITIES.md](ZEPHYR_CAPABILITIES.md)** - Complete feature documentation
- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - Detailed setup guide with API keys
- **[START_HERE.md](START_HERE.md)** - Quick reference

---

## 🎯 EXAMPLES

**Natural Conversation:**
```
You: "play some drake"
Zephyr: "Playing Drake on RISHILAPTOP"

You: "what's the weather in toronto?"
Zephyr: "The weather in Toronto is 5°C with partly cloudy skies..."

You: "tell me a joke"
Zephyr: "Why did the developer quit? They didn't get arrays!"

You: "create a project for my portfolio website"
Zephyr: "Created project: Portfolio Website"
```

---

## 🚀 WHY ZEPHYR?

- 🎨 **Beautiful Design** - Holographic UI feels futuristic
- 🧠 **Smart AI** - Understands natural language
- 🔒 **Private** - All data stays local
- ⚡ **Fast** - Instant hotkey access
- 🎵 **Integrated** - Controls Spotify, weather, news, more
- 💬 **Conversational** - Chat naturally like Jarvis

---

## 🤝 CONTRIBUTING

Feel free to:
- Add new commands
- Improve the UI
- Create new scenes
- Add integrations
- Submit PRs!

---

## 📄 LICENSE

MIT License - Feel free to use and modify!

---

## 🎉 ENJOY YOUR AI ASSISTANT!

**Press Ctrl+Alt+Z and experience the future!** 🚀

Made with ❤️ inspired by Iron Man's Jarvis



---## Features

- Overlay UI (bottom-left, always on top) with global hotkey (`Ctrl+Alt+Z`)

## ⚡ QUICK START (30 Seconds)- Wake word using Porcupine (keyword file `Yo_Zephyr.ppn`)

- Spotify controls: play/pause/skip/current song

1. **Run Zephyr:**- Calendar: create event, list upcoming events (Google Calendar)

   ```powershell- Weather: current weather via WeatherAPI

   venv\Scripts\activate- News: RSS-based (no API key) with NewsAPI fallback

   python app.py- Local Projects: quickly log “new project …” to `data/projects.json`

   ```

## Quick start (Windows PowerShell)

2. **Press Ctrl+Alt+Z**

1) Install dependencies (examples):

3. **Try it:**

   - `news about technology`	Optional, you may already have some packages. Install as needed.

   - `new project My Website`

   - `remember I'm building Zephyr`2) Run the app:



---	- Start the overlay/hotkey entrypoint:

	  `python app.py`

## 📖 COMPLETE GUIDE

	- Use the hotkey `Ctrl+Alt+Z` to toggle the overlay.

**👉 Read `COMPLETE_GUIDE.md` for everything you need!**	- Say “Yo Zephyr” to bring up the overlay (Porcupine access key required in `api_keys.py`).



Includes:## Configuration

- ✅ How to get ALL API keys (step-by-step with links!)

- ✅ Natural language usage`config.json` controls:

- ✅ All features & commands- `hotkey`: global hotkey string

- ✅ Troubleshooting- `wake_word_enabled`: whether to start the wake listener

- ✅ Configuration- `offline_mode`: when true, prefer RSS news



---## Notes

- Place API keys in `api_keys.py` as referenced by modules (WeatherAPI, NewsAPI, Spotify, Porcupine, Google Calendar).

## 🔑 GET API KEYS (15-30 Minutes)- If you don’t need a service, run `app.py` directly for an interactive desktop experience.


### Priority 1: **Gemini AI** (5 min - MOST IMPORTANT!)
🔗 https://aistudio.google.com/app/apikey
→ Enables natural language: "play some drake" instead of "play song Drake"

### Priority 2: **WeatherAPI** (5 min - FREE, no credit card!)
🔗 https://www.weatherapi.com/
→ Get weather in any city

### Priority 3: **Spotify** (10 min)
🔗 https://developer.spotify.com/dashboard
→ Control your music

**Full instructions in `COMPLETE_GUIDE.md`!**

---

## 🎯 WHAT WORKS RIGHT NOW (No API Keys!)

- ✅ **News** - RSS feeds (unlimited, free!)
- ✅ **Projects** - Track your work
- ✅ **Memory** - Remember things
- ✅ **Beautiful UI** - Glowing border, animations, scrolling

---

## 🎨 NEW IN VERSION 2.0

- 🧠 **Natural Language** - Talk like a human
- 📜 **Scrollable Responses** - Read long answers
- 🎨 **Glowing UI** - Animated cyan border
- 🔇 **Silent** - No annoying robot voice
- ✨ **Enhanced Sparkles** - Better animations

---

## 💬 TALK NATURALLY (With Gemini API)

```
play some billie eilish
what's the weather in new york?
tell me a joke
I want to build a portfolio website
what should I work on today?
```

---

## 🎮 CONTROLS

- **Ctrl+Alt+Z** - Show/hide Zephyr
- **Enter** - Submit command
- **Escape** - Hide
- **Mouse Wheel** - Scroll responses

---

## 📂 FILES

- **`COMPLETE_GUIDE.md`** - Read this for everything! ⭐
- **`api_keys.py`** - Add your API keys here
- **`config.json`** - Change settings
- **`app.py`** - Main entry point
- **`run.bat`** - Quick launcher

---

## 🚀 ENJOY YOUR JARVIS!

Press **Ctrl+Alt+Z** and start using Zephyr now!

Read **`COMPLETE_GUIDE.md`** for detailed setup and features.
