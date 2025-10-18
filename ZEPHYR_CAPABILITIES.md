# 🚀 ZEPHYR - WHAT IT CAN DO

**Your Personal Jarvis-Style AI Assistant**

---

## ✨ NEW HOLOGRAPHIC INTERFACE!

Zephyr now has a **stunning holographic UI** with:
- 🔵 **Transparent blue holographic avatar** that pulses with life
- 💫 **Glowing border effects** that cycle through cyan/blue
- 🌊 **Smooth slide-in animations** from the right
- 📜 **Scrollable response area** for long answers
- 🎯 **Clean, futuristic design** inspired by sci-fi AI interfaces
- 95% transparency for true hologram feel

Press **Ctrl+Alt+Z** anywhere and watch your AI assistant materialize!

---

## 🎯 CORE CAPABILITIES

### 1. 🧠 **Natural Language Understanding** (Powered by Gemini AI)
Talk to Zephyr like a human - no rigid commands needed!

**Examples:**
- "play some billie eilish" → Understands you want music
- "what's the weather like in new york?" → Gets weather info
- "tell me a joke" → Chats with you naturally
- "I want to create a portfolio website" → Creates a project
- "what should I work on today?" → Gives you suggestions

**What Makes It Smart:**
- Extracts your intent automatically
- Understands vague commands
- Conversational and witty responses
- NO references or citations in responses (clean info only!)

---

### 2. 🎵 **Spotify Music Control**
Control your Spotify playback hands-free!

**Commands:**
- `play some [artist/song]` - Plays music
- `pause` - Pauses playback
- `skip` or `next` - Skips to next song
- `current song` or `what's playing?` - Shows current track

**Requirements:**
- Spotify must be running on a device
- Spotify API keys configured in `api_keys.py`

---

### 3. 🌤️ **Weather Information**
Get instant weather updates for any city worldwide!

**Commands:**
- `weather in [city]`
- `what's the weather in toronto?`
- `how's the weather looking?`

**Features:**
- Current temperature
- Feels-like temperature
- Weather conditions
- Works for any city globally

**Requirements:**
- WeatherAPI key (free, no credit card!)

---

### 4. 📰 **News & Information**
Stay updated with the latest news on any topic!

**Commands:**
- `news about [topic]`
- `what's happening with AI?`
- `latest tech news`

**Features:**
- Google News RSS feed (works without API key!)
- Falls back to NewsAPI for enhanced results
- Top 5 headlines with summaries
- Clean responses without reference links

---

### 5. 📁 **Project Management**
Track all your projects and ideas in one place!

**Commands:**
- `new project [name]` - Creates a new project
- `create project My Portfolio Website` - With custom name
- `list projects` - Shows all your projects
- `what projects do I have?` - Natural query

**Features:**
- Local JSON storage (private, no cloud)
- Timestamps for when projects were created
- Optional descriptions
- Perfect for developers tracking side projects

---

### 6. 🧠 **Memory System**
Zephyr remembers things you tell it!

**Commands:**
- `remember [fact]` - Stores information
  - Example: `remember my birthday is in march`
  - Example: `remember I'm building Zephyr`
- `recall` - Shows recent memories
- `recall [query]` - Search memories
  - Example: `recall birthday`

**Features:**
- Persistent memory storage
- Searchable by keywords
- Timestamps for context
- Private and local (never leaves your machine)

---

### 7. 📅 **Calendar Integration** (Google Calendar)
Manage your schedule with voice commands!

**Commands:**
- `create event [name]` - Creates calendar event
- `list events` or `upcoming events` - Shows future events

**Requirements:**
- Google Calendar API setup
- OAuth authentication (one-time)

---

### 8. 🚀 **Dev Workspace Launcher**
Launch your development environments instantly!

**Commands:**
- `start workspace [name]`
- `open workspace research`

**Features:**
- Opens VS Code in project directories
- Starts development servers
- Launches multiple apps at once
- Configurable in `workspaces.json`

---

### 9. 🎬 **Scenes (Automation Routines)**
Run multi-step routines with one command!

**Built-in Scenes:**
- `wake up` - Morning routine (plays music, daily brief)
- `i'm home` - Evening routine (welcome message, news)

**Features:**
- Chains multiple commands together
- Customizable in `scenes.json`
- Can include: speech, commands, briefs

---

### 10. 💬 **General Chat**
When you're not giving commands, Zephyr can just chat!

**Examples:**
- `tell me a joke`
- `what should I do today?`
- `explain quantum computing`
- `how do I make pasta?`

**Personality:**
- Witty and intelligent
- Slightly sarcastic (like Jarvis!)
- Always helpful
- Concise responses (2-3 sentences)

---

## 🎮 HOW TO USE ZEPHYR

### Step 1: Launch
```powershell
cd C:\Users\shahr\Documents\GitHub\Zephyr
venv\Scripts\activate
python app.py
```

You'll see: `Hotkey registered: ctrl+alt+z`

### Step 2: Summon Your AI
Press **Ctrl+Alt+Z** from anywhere!

Watch the **holographic interface slide in** with:
- Glowing blue avatar pulsing
- Smooth animations
- Transparent futuristic design

### Step 3: Talk Naturally
Type your request like you're talking to a person:
- "play some music"
- "weather in london"
- "tell me about quantum physics"
- "create a project for my blog"

### Step 4: Get Results
Zephyr will:
- Show a **holographic processing indicator** (◉ Processing...)
- Type out the response with smooth animation
- Auto-scroll for long responses
- Keep responses clean (no references!)

### Step 5: Hide It
Press **Escape** or **Ctrl+Alt+Z** again to dismiss!

---

## 🔑 REQUIRED API KEYS

### **Priority 1: Gemini AI** ⭐ (ESSENTIAL!)
**Why:** Enables natural language understanding
**Cost:** FREE (generous limits)
**Get it:** https://aistudio.google.com/app/apikey
**Time:** 5 minutes

### **Priority 2: WeatherAPI** 🌤️
**Why:** Weather information for any city
**Cost:** FREE (no credit card!)
**Get it:** https://www.weatherapi.com/
**Time:** 5 minutes

### **Priority 3: Spotify** 🎵
**Why:** Music control
**Cost:** FREE (Spotify account needed)
**Get it:** https://developer.spotify.com/dashboard
**Time:** 10 minutes

### **Optional: NewsAPI** 📰
**Why:** Enhanced news (RSS works without it!)
**Cost:** FREE tier available
**Get it:** https://newsapi.org/
**Time:** 5 minutes

---

## 💡 WHAT MAKES ZEPHYR SPECIAL?

### ✅ Natural Language Processing
- Talk like a human, not a robot
- Vague commands work perfectly
- Context-aware responses

### ✅ Beautiful Holographic UI
- Futuristic transparent design
- Smooth animations
- Glowing effects
- Feels like Iron Man's AI!

### ✅ Privacy-First
- All data stored locally
- No cloud sync required
- Your memories stay on your machine
- API calls only when needed

### ✅ Modular & Extensible
- Easy to add new commands
- Configurable scenes and workspaces
- Fallback to regex if Gemini unavailable
- Graceful degradation

### ✅ Works Offline (Partially)
- Project management works offline
- Memory system works offline
- Scenes work offline
- News via RSS (no API key needed!)

---

## 🎯 TYPICAL USE CASES

### **As a Developer:**
```
"create project My New App"
"remember to add authentication tomorrow"
"start workspace development"
"what's the weather?" (checking before commute)
"play some lo-fi" (coding music)
```

### **For Productivity:**
```
"create event Team Meeting"
"news about technology"
"recall what I was working on"
"list projects"
"what should I focus on?"
```

### **Just for Fun:**
```
"tell me a joke"
"play some drake"
"what's happening in the world?"
"explain black holes"
"current song"
```

---

## 🚀 FUTURE POSSIBILITIES

Things you could add:
- ⏰ Wake word: "Hey Zephyr" or "Yo Zephyr"
- 🎤 Voice input button
- 🔔 System tray icon
- 🔐 Presence detection (unlock to show overlay)
- 📊 Task tracking with deadlines
- 🎨 Theme customization
- 🔊 Custom notification sounds
- 📱 Mobile app integration
- 🤖 More AI models (Claude, GPT, etc.)

---

## 📊 TECHNICAL SPECS

**Built With:**
- Python 3.13
- Tkinter (UI framework)
- Google Gemini AI (natural language)
- Spotipy (Spotify control)
- Feedparser (RSS news)
- Keyboard module (global hotkeys)

**Architecture:**
- Event-driven overlay system
- Threaded command processing
- Lazy-loaded dependencies
- Modular command routing
- JSON-based local storage

**Performance:**
- Instant hotkey response
- Smooth 60 FPS animations
- Non-blocking UI (threaded operations)
- Low memory footprint (~50MB)

---

## 🎉 YOU NOW HAVE:

✅ A beautiful holographic AI assistant
✅ Natural language understanding
✅ Music, weather, news, projects, memory
✅ Global hotkey access from anywhere
✅ Smooth animations and modern design
✅ Clean responses without references
✅ Privacy-first local storage
✅ Extensible and customizable

**Press Ctrl+Alt+Z and experience the future!** 🚀
