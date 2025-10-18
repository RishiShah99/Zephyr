# 🚀 ZEPHYR - YOUR JARVIS AI ASSISTANT

**Complete Guide - Everything You Need in One Place**

---

## 📋 TABLE OF CONTENTS
1. [What is Zephyr?](#what-is-zephyr)
2. [Quick Start (5 Minutes)](#quick-start)
3. [Get API Keys (15-30 Minutes)](#get-api-keys)
4. [How to Use Zephyr](#how-to-use)
5. [Features & Commands](#features)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 WHAT IS ZEPHYR?

Zephyr is your personal Jarvis-like AI assistant for Windows. Talk to it naturally like ChatGPT, but it controls your PC!

### ✨ What Makes Zephyr Special:
- 🎨 **Beautiful glowing UI** - Slides in from bottom-right with animations
- 🧠 **Natural language** - Talk like a human, not a robot
- 📜 **Scrollable responses** - Read long answers easily
- 🔇 **Silent by default** - No annoying robot voice
- 🎮 **Global hotkey** - Press Ctrl+Alt+Z from anywhere
- 🎵 **Spotify control** - "play some drake"
- 🌤️ **Weather** - "what's the weather in toronto?"
- 📰 **News** - "what's happening with AI?"
- 📁 **Project tracking** - "create a project for my website"
- 🧠 **Memory** - "remember my birthday is in march"
- 📅 **Calendar** - "create event Team Meeting"

---

## ⚡ QUICK START (5 MINUTES)

### Step 1: Run Zephyr
```powershell
cd C:\Users\shahr\Documents\GitHub\Zephyr
venv\Scripts\activate
python app.py
```

You should see: `Hotkey registered: ctrl+alt+z`

### Step 2: Try It!
1. **Press Ctrl+Alt+Z**
2. Watch the beautiful overlay slide in! ✨
3. Type: `help`
4. Press Enter

### Step 3: Test Features (Work WITHOUT API Keys!)
```
new project My Portfolio Website
list projects
remember I'm building Zephyr
recall
news about technology
```

### Step 4: Get API Keys (Next Section!)
To unlock Spotify, Weather, and Smart AI - you need API keys!

---

## 🔑 GET API KEYS (Step-by-Step)

### 🎯 PRIORITY 1: Gemini AI (FREE - 5 minutes)
**THIS IS THE MOST IMPORTANT ONE!** Enables natural language understanding.

#### Steps:
1. Go to: **https://aistudio.google.com/app/apikey**
2. Click "Create API Key"
3. Copy the key
4. Open `api_keys.py` in Zephyr folder
5. Replace:
   ```python
   GEMINI_API_KEY = "paste_your_key_here"
   ```
6. Save and restart Zephyr

**Free Tier**: 60 requests/minute (more than enough!)

**Now you can talk naturally:**
- "play some billie eilish"
- "what's the weather like in new york?"
- "tell me a joke"
- "I want to build a portfolio website"

---

### 🌤️ PRIORITY 2: WeatherAPI (FREE - 5 minutes)
**No credit card needed!**

#### Steps:
1. Go to: **https://www.weatherapi.com/**
2. Click "Sign Up Free"
3. Go to dashboard: https://www.weatherapi.com/my/
4. Copy your API Key
5. In `api_keys.py`:
   ```python
   WEATHER_API_KEY = "paste_your_key_here"
   ```

**Free Tier**: 1 million calls/month

**Test**: `what's the weather in toronto?`

---

### 🎵 PRIORITY 3: Spotify (FREE - 10 minutes)
**Control your music!**

#### Steps:
1. Go to: **https://developer.spotify.com/dashboard**
2. Log in with Spotify account
3. Click "Create App"
   - App name: `Zephyr`
   - Description: `Personal AI assistant`
   - Redirect URI: `http://localhost:8888/callback`
   - Check "Web API"
4. Copy **Client ID** and **Client Secret**
5. In `api_keys.py`:
   ```python
   SPOTIFY_CLIENT_ID = "paste_client_id_here"
   SPOTIFY_CLIENT_SECRET = "paste_client_secret_here"
   SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"
   ```

**First run**: Opens browser for authorization, then automatic!

**Test**: `play some drake`

---

### 📅 OPTIONAL: Google Calendar (FREE - 20 minutes)

#### Steps:
1. Go to: **https://console.cloud.google.com/**
2. Create new project: "Zephyr"
3. Enable Calendar API:
   - https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
   - Click "Enable"
4. Create credentials:
   - APIs & Services → Credentials
   - Create OAuth 2.0 Client ID
   - Application type: Desktop app
   - Name: "Zephyr"
5. Download `credentials.json`
6. Move to Zephyr folder
7. First run opens browser for authorization

**Test**: `create event Team Meeting`

---

### 🎤 OPTIONAL: Porcupine Wake Word (FREE - 10 minutes)
**Say "Yo Zephyr" to activate!**

#### Steps:
1. Go to: **https://console.picovoice.ai/**
2. Sign up free
3. Click "AccessKey" → Copy
4. In `api_keys.py`:
   ```python
   ACCESS_KEY = "paste_your_key_here"
   ```
5. In `config.json`:
   ```json
   "wake_word_enabled": true
   ```
6. Install: `pip install pvporcupine pyaudio`

---

### 📰 NEWS (Already Works!)
**RSS feeds - NO API KEY NEEDED!** ✅

Test: `news about microsoft`

---

## 🎮 HOW TO USE ZEPHYR

### Controls:
- **Ctrl+Alt+Z**: Show/hide Zephyr
- **Enter**: Submit command
- **Escape**: Hide Zephyr
- **Mouse Wheel**: Scroll through long responses

### Talk Naturally (With Gemini API):
```
play some music
what's the weather like?
tell me a joke
I want to create a new website project
what should I work on today?
remember I have a meeting friday
what's happening with AI?
```

### Specific Commands (Without Gemini):
```
play song Drake
weather in Toronto
new project Portfolio Site: Next.js app
create event Team Meeting
news about technology
remember my birthday is March 15
```

---

## 🎯 FEATURES & COMMANDS

### 🎵 Spotify Control
```
play some drake
play song Blinding Lights
pause
skip
what song is playing?
```
**Requires**: Spotify API keys

---

### 🌤️ Weather
```
what's the weather in new york?
weather in toronto
how's the weather looking?
```
**Requires**: WeatherAPI key

---

### 📰 News (FREE - No API Key!)
```
news about AI
what's happening with microsoft?
show me tech news
news about tesla
```
**Uses**: Google News RSS (unlimited!)

---

### 📁 Projects
```
create a project for my portfolio website
new project Mobile App: React Native shopping app
list projects
show my projects
```
**Saves to**: `data/projects.json` (local, private!)

---

### 🧠 Memory
```
remember I love coding in python
remember my birthday is march 15
don't forget I have a meeting friday
recall
what did I tell you?
```
**Saves to**: `data/memory.json` (local, private!)

---

### 📅 Calendar
```
create event Team Meeting
create event Doctor Appointment
see upcoming events
what's on my calendar?
```
**Requires**: Google Calendar setup

---

### 💬 Chat
```
tell me a joke
what should I work on?
how are you?
what can you help me with?
```
**Requires**: Gemini API for smart responses

---

## ⚙️ CONFIGURATION

### config.json Settings:
```json
{
  "hotkey": "ctrl+alt+z",           // Change hotkey
  "wake_word_enabled": false,        // Enable "Yo Zephyr"
  "enable_voice": false,             // Text-to-speech (monotone)
  "enable_gemini": true,             // Natural language AI
  "offline_mode": false,             // Allow internet features
  "ui": {
    "position": "bottom-right",      // Window position
    "theme": "dark-glassmorphism"    // UI theme
  }
}
```

### api_keys.py Template:
```python
# Get from: https://aistudio.google.com/app/apikey
GEMINI_API_KEY = None

# Get from: https://www.weatherapi.com/
WEATHER_API_KEY = None

# Get from: https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = None
SPOTIFY_CLIENT_SECRET = None
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# Get from: https://console.picovoice.ai/
ACCESS_KEY = None  # For wake word

# Optional: Get from https://newsapi.org/ (RSS works without this!)
NEWS_API_KEY = None
```

---

## 🎨 UI FEATURES

### Glowing Border
- Animated cyan pulse: #00D9FF → #00B8E6 → #0099CC
- Smooth color transitions
- Stops when hidden

### Enhanced Sparkles
- Bigger icon (24pt)
- Color cycling: cyan → bright cyan → gold
- Variations: ✨⭐💫🌟🌠

### Scrollable Responses
- Mouse wheel to scroll
- Auto-scrolls to bottom
- Read long responses easily

### Animations
- Smooth slide-in from right
- Fade in/out effects
- Typing animation (10ms/char)
- Thinking indicator with sparkles

---

## 🐛 TROUBLESHOOTING

### "Hotkey doesn't work"
1. Make sure app is running (see "Hotkey registered" message)
2. Try pressing Ctrl+Alt+Z firmly
3. Restart Zephyr:
   ```powershell
   venv\Scripts\activate
   python app.py
   ```

### "Old UI showing instead of new one"
1. Clear Python cache:
   ```powershell
   Remove-Item -Path __pycache__ -Recurse -Force
   ```
2. Restart Zephyr

### "Commands not working"
- Check if API key is needed
- With Gemini: Talk naturally
- Without Gemini: Be specific ("play song Drake")

### "Can't scroll responses"
- Use mouse wheel
- Click and drag scrollbar on right side

### "Voice is annoying"
- It's disabled by default!
- Check `config.json`: `"enable_voice": false`

### "Natural language not working"
- Get Gemini API key (Priority 1!)
- Check `config.json`: `"enable_gemini": true`
- Restart Zephyr after adding key

### "Spotify not working"
1. Spotify app must be open somewhere
2. Check API keys in `api_keys.py`
3. First run opens browser for authorization

---

## 📂 FILE STRUCTURE

### Essential Files (Don't Delete!):
```
app.py                 # Main entry point
ui.py                  # Beautiful overlay interface
assistant.py           # Command routing
gemini_nlp.py          # Natural language AI
api_keys.py            # Your API keys ⭐
config.json            # Settings ⭐
settings.py            # Config loader
```

### Feature Modules:
```
spotify.py             # Music control
weather.py             # Weather info
news_rss.py            # News feeds (no API key!)
projects.py            # Project tracking
memory.py              # Memory storage
planner.py             # Google Calendar
wake_word_listener.py  # "Yo Zephyr"
scenes.py              # Routines
workspace.py           # Dev workspace launcher
briefing.py            # Daily brief
```

### Data Storage (Your Private Data):
```
data/
  projects.json        # Your projects
  memory.json          # Your memories
  workspaces.json      # Dev workspaces
```

### Scripts:
```
run.bat                # Quick launcher
setup_venv.bat         # Environment setup
```

---

## 🎉 YOU'RE READY!

### Recommended Order:
1. ✅ Run Zephyr (works now with RSS news, projects, memory!)
2. 🔑 Get Gemini API key (5 min) → Natural language
3. 🌤️ Get WeatherAPI key (5 min) → Weather queries
4. 🎵 Get Spotify keys (10 min) → Music control
5. 📅 Optional: Google Calendar (20 min)
6. 🎤 Optional: Wake word (10 min)

### Start Using Now:
1. Press **Ctrl+Alt+Z**
2. Try: `news about technology`
3. Try: `new project Test App`
4. Try: `remember I'm building Zephyr`
5. Get Gemini key → Talk naturally!

---

## 💡 PRO TIPS

1. **Start with Gemini** - Makes everything 10x better
2. **WeatherAPI is easiest** - No credit card, 5 minutes
3. **RSS news works now** - No API key needed!
4. **Scroll responses** - Mouse wheel or scrollbar
5. **Escape to hide** - Quick exit anytime
6. **Talk naturally** - With Gemini, no need to be precise

---

## 🚀 QUICK REFERENCE

### Most Used Commands:
```
# Music (need Spotify keys)
play some [artist/song]

# Weather (need WeatherAPI key)
what's the weather in [city]?

# News (FREE - works now!)
news about [topic]

# Projects (FREE - works now!)
create a project for [description]

# Memory (FREE - works now!)
remember [fact]

# Chat (need Gemini key)
tell me a joke
what should I work on?
```

### API Key Priority:
1. **Gemini** - Natural language (MOST IMPORTANT!)
2. **WeatherAPI** - Weather queries (easiest!)
3. **Spotify** - Music control
4. **Calendar** - Event management
5. **Wake word** - Voice activation

---

**That's it! Press Ctrl+Alt+Z and enjoy your Jarvis! 🎉**

For questions or issues, all features gracefully degrade - you'll get helpful messages about what needs configuration!
