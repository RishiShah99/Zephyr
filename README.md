# 🚀 Zephyr - Your Personal Jarvis AI Assistant# Zephyr: Personal desktop copilot



**Talk to your PC like Iron Man talks to Jarvis!**Zephyr is a keyboard- or wake-word-activated desktop copilot. Hit a global hotkey and a small overlay pops up in the bottom-left so you can type a command, or say “Yo Zephyr” to bring it up hands‑free.



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
