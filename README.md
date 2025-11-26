# Zephyr

A personal AI assistant that combines the speed of a minimal popup interface with the power of a full-featured dashboard. Designed for seamless integration into your daily workflow with voice commands, natural language processing, and intelligent memory.

Built to be your always-accessible companion that remembers, assists, and adapts to your needs.

## Core Features

### Dual Interface System
- **Tiny Zephyr** - Instant access popup (Ctrl+Alt+Z) for quick commands and queries
- **Dashboard** - Full React/Electron interface for advanced features and visual management
- Seamless transition between interfaces with one-click expansion
- System tray integration for background operation

### Intelligent Interaction
- Multi-provider LLM support (Groq, OpenAI, Gemini)
- Natural language command understanding
- Voice input and text-to-speech output
- Context-aware responses with conversation memory
- Streaming responses with real-time feedback

### Smart Memory System
- Persistent fact storage and recall
- Learned context retention
- User preference tracking
- SQLite database for fast retrieval
- Automatic context learning from conversations

### Rich Integrations
- Spotify music control (play, pause, current track)
- Weather information via WeatherAPI
- File search and management
- Project idea tracking
- Calendar event creation (Google Calendar)
- Custom command extensibility

## Architecture

Zephyr uses a three-tier architecture for maximum flexibility:

### Tiny Zephyr (Frontend)
- Minimal Tkinter interface with modern dark theme
- Global hotkey registration (Ctrl+Alt+Z)
- Slide-in animations and smooth transitions
- Voice recording with wake word detection
- Auto-hiding and smart positioning

### API Server (Bridge)
- Flask REST API on port 5000
- Auto-starts with Tiny Zephyr
- Bridges communication between UI and backend
- Handles command routing and execution
- Provides endpoints for dashboard integration

### Dashboard (Full Interface)
- React 18 with Vite for fast development
- Electron for native desktop experience
- TailwindCSS for modern, responsive design
- Framer Motion for smooth animations
- Real-time data synchronization with API server

## Installation

### Prerequisites
- **Python 3.8+** - Core runtime
- **Node.js 16+** - Dashboard frontend
- **Virtual environment** - Recommended for isolation

### Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/RishiShah99/Zephyr.git
cd Zephyr
```

2. **Set up Python environment:**
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. **Set up Dashboard (optional):**
```bash
cd dashboard-app
npm install
cd ..
```

4. **Configure API keys:**

Create `api_keys.py` in the root directory:
```python
# Required for AI features
GROQ_API_KEY = "your_groq_api_key"  # Get from console.groq.com
OPENAI_API_KEY = "your_openai_key"  # Optional, for GPT models

# Optional integrations
WEATHER_API_KEY = "your_weather_key"  # From weatherapi.com
SPOTIFY_CLIENT_ID = "your_spotify_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_secret"
```

5. **Initialize database:**
```bash
python -c "from memory_db import init_db; init_db()"
```

6. **Launch Zephyr:**
```bash
# Windows
start_zephyr.bat

# Or run directly
python app.py
```

## Usage

### Tiny Zephyr (Quick Access)

**Launch:**
- Press `Ctrl+Alt+Z` anywhere on your system
- Click the system tray icon

**Commands:**
```
"what's the weather in New York"
"play some jazz music"
"remember my birthday is June 15"
"what do you remember about me"
"create a calendar event for tomorrow at 2pm"
"find files named report"
```

**Expand to Dashboard:**
- Click the "⛶ Expand" button in the top right
- Tiny Zephyr auto-hides, dashboard opens

### Dashboard (Full Interface)

**Access:**
- Click "Expand" from Tiny Zephyr
- Or run: `cd dashboard-app && npm run dev`

**Features:**
-  **Memory Tab** - View, add, delete stored facts and contexts
-  **Projects Tab** - Track ideas and project details  
-  **Music Controls** - Spotify integration
-  **Test Zone** - Try commands and see responses
-  **Dashboard** - Overview of all features

## Configuration

### Settings File
Edit `config.json` (auto-created on first run):
```json
{
  "hotkey": "ctrl+alt+z",
  "enable_voice": false,
  "enable_gemini": true,
  "wake_word_enabled": false,
  "default_city": "Toronto"
}
```

### Changing AI Provider
In `groq_nlp.py`, modify the model selection:
```python
# Options: llama-3.1-70b-versatile, llama-3.1-8b-instant, mixtral-8x7b
MODEL = "llama-3.1-70b-versatile"
```

### Custom Commands
Add new intents in `assistant.py`:
```python
def handle_custom_command(entities):
    # Your custom logic here
    return "Response message"
```

## Project Structure

```
Zephyr/
├── app.py                  # Main entry point
├── ui.py                   # Tiny Zephyr interface
├── assistant.py            # Command handler
├── groq_nlp.py            # AI/NLP processing
├── api_server.py          # Flask REST API
├── memory_db.py           # Database layer
├── projects.py            # Project management
├── weather.py             # Weather integration
├── spotify.py             # Music control
├── settings.py            # Configuration
├── tray_icon.py          # System tray
├── dashboard-app/        # React dashboard
│   ├── src/
│   │   ├── components/   # React components
│   │   └── App.jsx       # Main app
│   ├── electron/         # Electron main process
│   └── package.json      # Dependencies
├── data/                 # SQLite database
└── requirements.txt      # Python dependencies
```

## API Endpoints

The Flask API server provides the following endpoints:

```
GET  /health              # Health check
POST /command             # Execute Zephyr command
GET  /memory              # Retrieve stored memories
POST /memory              # Add new memory
DELETE /memory            # Remove memory
GET  /projects            # List all projects
POST /projects            # Create new project
GET  /spotify/status      # Current playback
POST /spotify/control     # Control playback
```

**Example:**
```bash
curl -X POST http://localhost:5000/command \
  -H "Content-Type: application/json" \
  -d '{"command": "what is the weather"}'
```

## Development

### Running in Development Mode

**Tiny Zephyr:**
```bash
python app.py
```

**Dashboard:**
```bash
cd dashboard-app
npm run dev  # Starts Vite dev server + Electron
```

**API Server (standalone):**
```bash
python api_server.py
```

### Code Formatting
```bash
# Python (if using black)
black *.py

# JavaScript (if using prettier)  
cd dashboard-app
npm run format
```

### Adding New Features

1. **Backend Integration:**
   - Add function in appropriate module (e.g., `weather.py`)
   - Register in `assistant.py` command handler
   - Add intent to `groq_nlp.py`

2. **UI Component:**
   - Create React component in `dashboard-app/src/components/`
   - Add route/tab in `App.jsx`
   - Connect to API endpoint

## Known Limitations

- **Windows Only**: Global hotkeys require administrator privileges
- **Single Instance**: Only one Zephyr instance can run at a time
- **API Keys Required**: Core AI features need Groq/OpenAI API access
- **Network Dependent**: Weather, music, and some AI features require internet

## Roadmap

- [ ] Multi-platform support (macOS, Linux)
- [ ] Cloud sync for memories and projects
- [ ] Plugin system for custom integrations
- [ ] Mobile companion app
- [ ] Advanced calendar integration
- [ ] Team collaboration features
- [ ] Offline AI model support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Made by Rishi Shah**
