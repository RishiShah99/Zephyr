"""
Natural language understanding powered by Google Gemini AI.
Converts natural conversation into structured commands that Zephyr can execute.
"""

import json
from typing import Optional, Dict, Any

try:
    import google.generativeai as genai
    from api_keys import GEMINI_API_KEY
    HAS_GEMINI = True
except Exception:
    HAS_GEMINI = False
    GEMINI_API_KEY = None


def configure_gemini():
    """Configure Gemini API if available"""
    if HAS_GEMINI and GEMINI_API_KEY:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            return True
        except Exception as e:
            print(f"Gemini configuration failed: {e}")
            return False
    return False


def understand_command(user_input: str) -> Dict[str, Any]:
    """
    Use Gemini to understand natural language and extract intent + entities.
    
    Returns a structured command with:
    - intent: The action user wants (play_music, get_weather, create_project, etc.)
    - entities: Relevant details (song_name, location, project_name, etc.)
    - natural_response: Whether to use natural language response instead of structured
    """
    
    if not configure_gemini():
        # Fallback to basic pattern matching
        return {"intent": "unknown", "entities": {}, "natural_response": False}
    
    try:
        # Use gemini-1.5-flash (newer, faster model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # System prompt to teach Gemini about Zephyr's capabilities
        system_prompt = """You are a command interpreter for Zephyr, an AI assistant. 
Your job is to understand natural language and convert it to structured commands.

Available intents:
- play_music: User wants to play a song (extract: song_name)
- pause_music: User wants to pause music
- skip_music: User wants to skip to next song
- current_song: User wants to know what's playing
- get_weather: User wants weather info (extract: location)
- create_event: User wants to create a calendar event (extract: event_name, when)
- list_events: User wants to see upcoming events
- get_news: User wants news (extract: topic)
- create_project: User wants to create a project (extract: project_name, description)
- list_projects: User wants to see projects
- remember: User wants to store a memory (extract: fact)
- recall: User wants to recall memories (extract: query)
- start_workspace: User wants to launch a dev workspace (extract: workspace_name)
- run_scene: User wants to run a routine (extract: scene_name like "wake up" or "i'm home")
- chat: General conversation, question, or request that doesn't fit above intents

Examples:
User: "play some drake"
Response: {"intent": "play_music", "entities": {"song_name": "drake"}, "natural_response": false}

User: "what's the weather like in toronto?"
Response: {"intent": "get_weather", "entities": {"location": "toronto"}, "natural_response": false}

User: "remind me that I need to call mom tomorrow"
Response: {"intent": "remember", "entities": {"fact": "I need to call mom tomorrow"}, "natural_response": false}

User: "I want to build a new website for my portfolio"
Response: {"intent": "create_project", "entities": {"project_name": "Portfolio Website", "description": "personal portfolio site"}, "natural_response": false}

User: "what should i work on today?"
Response: {"intent": "chat", "entities": {}, "natural_response": true}

User: "tell me a joke"
Response: {"intent": "chat", "entities": {}, "natural_response": true}

Respond ONLY with valid JSON in the exact format shown above. No markdown, no extra text."""

        # Get Gemini's understanding
        prompt = f"{system_prompt}\n\nUser: \"{user_input}\"\nResponse:"
        response = model.generate_content(prompt)
        
        # Parse JSON response
        result_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.startswith("```"):
            result_text = result_text[3:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]
        
        result = json.loads(result_text.strip())
        
        return result
        
    except Exception as e:
        print(f"Gemini understanding failed: {e}")
        return {"intent": "unknown", "entities": {}, "natural_response": False}


def generate_natural_response(user_input: str, context: str = "") -> str:
    """
    Use Gemini to generate a natural, conversational response.
    Used for general chat when user isn't giving a command.
    """
    
    if not configure_gemini():
        return "I'm here to help! Try commands like 'play music', 'weather in [city]', 'create project [name]', or 'news about [topic]'."
    
    try:
        # Use gemini-1.5-flash (newer, faster model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        personality_prompt = """You are Zephyr, a helpful AI assistant inspired by Jarvis from Iron Man.
You are witty, intelligent, slightly sarcastic but always helpful. Keep responses concise (2-3 sentences max).
You can help with: Spotify music control, weather, calendar, news, project management, memories, and dev workspace launching.

When answering questions, be conversational and natural. Don't just list capabilities unless asked."""

        prompt = f"{personality_prompt}\n\n"
        if context:
            prompt += f"Context: {context}\n\n"
        prompt += f"User: {user_input}\nZephyr:"
        
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        print(f"Gemini response generation failed: {e}")
        return "I'm having trouble thinking right now. Try a specific command like 'play song [name]' or 'weather in [city]'."


def chat(user_input: str) -> str:
    """Simple chat interface using Gemini"""
    return generate_natural_response(user_input)


if __name__ == "__main__":
    # Test the NLP
    test_inputs = [
        "play some billie eilish",
        "what's the weather in new york?",
        "create a project for my portfolio website using next.js",
        "what should i work on?",
        "tell me a joke",
        "remember that my birthday is in march",
    ]
    
    print("Testing Gemini NLP:")
    for inp in test_inputs:
        result = understand_command(inp)
        print(f"\nInput: {inp}")
        print(f"Result: {json.dumps(result, indent=2)}")
