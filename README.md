# 🚀 Zephyr - Your Personal Jarvis AI Assistant# Zephyr: Personal desktop copilot



# 🚀 Zephyr - Your Personal Jarvis AI Assistant

**Talk to your PC like Iron Man talks to Jarvis!**

Zephyr is a keyboard-activated AI assistant with a **stunning holographic interface**. Press **Ctrl+Alt+Z** from anywhere and watch your personal AI materialize with glowing blue effects, smooth animations, and natural conversation powered by Google Gemini.

---

## ⚡ QUICK START (30 Seconds)

1. **Clone & Setup:**
   ```powershell
   git clone https://github.com/RishiShah99/Zephyr.git
   cd Zephyr
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Add Your Gemini API Key:**
   - Get free key: https://aistudio.google.com/app/apikey
   - Open `api_keys.py`
   - Replace: `GEMINI_API_KEY = "your_key_here"`

3. **Run Zephyr:**
   ```powershell
   python app.py
   ```

4. **Press Ctrl+Alt+Z** and say hello to your AI! ✨

---

## ✨ WHAT IT LOOKS LIKE

- 🔵 **Holographic transparent blue avatar** that pulses
- 💫 **Glowing border effects** that cycle through cyan
- 🌊 **Smooth slide-in animations**
- 📜 **Scrollable responses** with typing effects
- 🎯 **Modern sci-fi interface** inspired by Iron Man

---

## 🎯 WHAT IT CAN DO

### 🧠 Natural Language Understanding
Talk naturally - no rigid commands!
- "play some billie eilish"
- "what's the weather in new york?"
- "tell me a joke"
- "create a project for my portfolio"

### 🎵 Spotify Control
- Play, pause, skip songs
- "what's playing?"
- Hands-free music control

### 🌤️ Weather Information
- Any city worldwide
- Current conditions & temperature

### 📰 News & Information  
- "news about AI"
- Clean responses (no references!)
- Powered by Google News RSS

### 📁 Project Management
- Track your projects locally
- "new project My Website"
- "list projects"

### 🧠 Memory System
- "remember I need to call mom"
- "recall birthday"
- Private, local storage

### 💬 General Chat
- Ask questions
- Get explanations
- Conversational AI (Jarvis-like!)

**📖 See [ZEPHYR_CAPABILITIES.md](ZEPHYR_CAPABILITIES.md) for complete feature list!**

---

## 🔑 API KEYS

### **Priority 1: Gemini AI** (5 min - FREE)
🔗 https://aistudio.google.com/app/apikey
→ **ESSENTIAL** for natural language!

### **Priority 2: WeatherAPI** (5 min - FREE)
🔗 https://www.weatherapi.com/
→ Get weather anywhere

### **Priority 3: Spotify** (10 min - FREE)
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
