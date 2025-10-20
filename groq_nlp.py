"""
Groq-based NLP for intent recognition and natural conversation
"""
import json
from groq import Groq
from api_keys import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

# System prompt to teach Groq about Zephyr's intents
SYSTEM_PROMPT = """You are Zephyr, a personal AI assistant. Analyze user commands and respond with JSON.

Available intents:
- play_music: Play a song on Spotify
- pause_music: Pause current song
- skip_music: Skip to next song
- current_song: Check what's playing
- get_weather: Get weather for a location
- create_event: Create calendar event
- list_events: Show upcoming events
- get_news: Fetch news about a topic
- create_project: Create a new project
- list_projects: List all projects
- remember: Store a fact in memory
- recall: Retrieve stored facts
- start_workspace: Open a development workspace
- run_scene: Execute a smart home scene
- chat: General conversation (default)

If the user wants structured action, respond with:
{
  "intent": "<intent_name>",
  "entities": {"key": "value"},
  "natural_response": false
}

If it's casual conversation (greetings, jokes, questions), respond with:
{
  "intent": "chat",
  "entities": {},
  "natural_response": true
}

Examples:
User: "play never gonna give you up"
{"intent": "play_music", "entities": {"song_name": "never gonna give you up"}, "natural_response": false}

User: "weather in Toronto"
{"intent": "get_weather", "entities": {"location": "Toronto"}, "natural_response": false}

User: "hi"
{"intent": "chat", "entities": {}, "natural_response": true}

User: "tell me a joke"
{"intent": "chat", "entities": {}, "natural_response": true}

Only respond with valid JSON."""

conversation_history = []

def understand_command(command: str) -> tuple:
    """
    Parse user command and return (intent, entities, natural_response)
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": command}
            ],
            temperature=0.3,
            max_tokens=200
        )
        
        result = response.choices[0].message.content.strip()
        
        # Parse JSON response
        data = json.loads(result)
        intent = data.get("intent", "unknown")
        entities = data.get("entities", {})
        natural = data.get("natural_response", False)
        
        return intent, entities, natural
        
    except Exception as e:
        print(f"Groq understanding failed: {e}")
        return "unknown", {}, False


def generate_natural_response(command: str, context: str = "") -> str:
    """Generate a natural language response for the user"""
    try:
        messages = [
            {"role": "system", "content": "You are Zephyr, a helpful and friendly AI assistant. Be concise and natural."}
        ]
        
        # Add conversation history (last 10 messages)
        messages.extend(conversation_history[-10:])
        
        # Add current command
        if context:
            messages.append({"role": "user", "content": f"{command}\n\nContext: {context}"})
        else:
            messages.append({"role": "user", "content": command})
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        
        reply = response.choices[0].message.content.strip()
        
        # Update conversation history
        conversation_history.append({"role": "user", "content": command})
        conversation_history.append({"role": "assistant", "content": reply})
        
        return reply
        
    except Exception as e:
        print(f"Groq response generation failed: {e}")
        return "I'm having trouble responding right now."


def chat(message: str) -> str:
    """Handle general conversation"""
    return generate_natural_response(message)
