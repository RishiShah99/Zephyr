"""
Zephyr API Server - Bridge between Electron dashboard and Python backend
Provides REST API endpoints for the dashboard to interact with Zephyr's features
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import Zephyr modules
try:
    from groq_nlp import understand_command, generate_natural_response
    from memory_db import get_user_facts, store_user_fact
    ZEPHYR_MODULES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import Zephyr modules: {e}")
    ZEPHYR_MODULES_AVAILABLE = False

app = Flask(__name__)
CORS(app)  # Enable CORS for Electron app

# Paths
MEMORY_FILE = "memory.json"
PROJECTS_FILE = "projects.json"

# Helper Functions
def execute_intent(intent: str, entities: dict, original_command: str) -> str:
    """Execute the actual Zephyr command based on intent"""
    try:
        # Import action modules dynamically
        if intent == "play_music":
            from spotify import play_song
            song = entities.get("song_name") or entities.get("genre") or "music"
            result = play_song(song)
            return f"🎵 Playing: {song}\n{result}"
        
        elif intent == "pause_music":
            from spotify import pause_song
            result = pause_song()
            return f"⏸️ Music paused\n{result}"
        
        elif intent == "current_song":
            from spotify import get_current_song
            result = get_current_song()
            return f"🎵 Currently playing: {result}"
        
        elif intent == "remember":
            fact = entities.get("fact", "")
            if fact:
                store_user_fact("general", "user_info", fact)
                return f"✓ Remembered: {fact}"
            return "What would you like me to remember?"
        
        elif intent == "recall":
            facts = get_user_facts()
            if facts:
                fact_list = "\n".join([f"• {fact['key']}: {fact['value']}" for fact in facts])
                return f"📝 Here's what I remember:\n{fact_list}"
            return "I don't have any memories stored yet."
        
        elif intent == "find_file":
            from file_search import search_files_by_name, format_files_for_display
            query = entities.get("query", "")
            if query:
                files = search_files_by_name(query, max_results=10)
                if files:
                    formatted = format_files_for_display(files)
                    return f"🔍 Found files matching '{query}':\n{formatted}"
                else:
                    return f"No files found matching '{query}'"
            return "What files should I search for?"
        
        elif intent == "get_weather":
            from weather import get_weather
            # Get location from entities, or use default
            location = entities.get("location")
            if not location or location == "unknown":
                location = "Toronto"  # Your default city
            weather = get_weather(location)
            return f"🌤️ Weather for {location}:\n{weather}"
        
        elif intent == "get_news":
            from news_rss import get_news_rss
            topic = entities.get("topic", "latest news")
            limit = entities.get("limit", 5)
            news = get_news_rss(topic, limit)
            return f"📰 {news}"
        
        elif intent == "list_project_ideas":
            from projects import list_projects
            projects_list = list_projects()
            if projects_list:
                project_text = "\n".join([f"• {p['name']}: {p.get('description', 'No description')}" 
                                         for p in projects_list])
                return f"💡 Your projects:\n{project_text}"
            return "No projects found. Try creating one with 'idea for [project name]'"
        
        elif intent == "create_project_idea":
            from projects import create_project
            project_name = entities.get("project_name", "New Project")
            description = entities.get("description", "")
            result = create_project(project_name, description)
            return f"✨ Created project: {result['name']}\n{result.get('description', '')}"
        
        elif intent == "create_calendar_event":
            from planner import create_event
            event_name = entities.get("event_name", "New Event")
            location = entities.get("location")
            description = entities.get("description")
            try:
                result = create_event(event_name, location, description)
                return f"📅 Created calendar event: {event_name}"
            except Exception as e:
                return f"❌ Could not create calendar event: {str(e)}\n(You may need to set up Google Calendar API credentials)"
        
        elif intent == "open_application":
            app_name = entities.get("app_name", "")
            if app_name:
                try:
                    import subprocess
                    subprocess.Popen(app_name, shell=True)
                    return f"🚀 Opening {app_name}..."
                except Exception as e:
                    return f"❌ Could not open {app_name}: {str(e)}"
            return "❌ No application name provided"
        
        elif intent == "set_timer":
            duration = entities.get("duration", 60)
            return f"⏱️ Timer set for {duration} seconds\n(Timer functionality requires implementation in UI)"
        
        elif intent == "calculate":
            expression = entities.get("expression", "")
            if expression:
                try:
                    # Safe eval for basic math
                    result = eval(expression, {"__builtins__": {}}, {})
                    return f"🧮 {expression} = {result}"
                except Exception as e:
                    return f"❌ Could not calculate: {str(e)}"
            return "❌ No expression provided"
        
        else:
            # Unknown intent - return intent info for debugging
            return f"🤖 Intent detected: {intent}\nEntities: {json.dumps(entities, indent=2)}\n\n(Action handler not implemented yet)"
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        return f"❌ Error executing {intent}: {str(e)}\n\nDetails:\n{error_details}"

def load_memory():
    """Load memory from file"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_memory(memory_data):
    """Save memory to file"""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory_data, f, indent=2)

# API endpoints
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'message': 'Zephyr API Server is running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/command', methods=['POST'])
def execute_command():
    """Execute a Zephyr command"""
    try:
        data = request.json
        command = data.get('command', '')
        
        if not command:
            return jsonify({'error': 'No command provided'}), 400
        
        # Use actual Zephyr NLP if available
        if ZEPHYR_MODULES_AVAILABLE:
            try:
                intent, entities, natural_response = understand_command(command)
                
                if natural_response:
                    # Chat response
                    response = generate_natural_response(command)
                else:
                    # Execute the actual command based on intent
                    response = execute_intent(intent, entities, command)
                
            except Exception as e:
                response = f"Zephyr NLP Error: {str(e)}"
        else:
            response = f"Received command: {command}\n(Zephyr modules not loaded)"
        
        return jsonify({
            'success': True,
            'command': command,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/memory', methods=['GET'])
def get_memory():
    """Get all memory entries from database (both facts and learned contexts)"""
    try:
        from memory_db import get_user_facts
        
        # Get facts
        facts = get_user_facts()
        
        # Format facts for frontend
        formatted_memory = []
        for fact in facts:
            formatted_memory.append({
                'id': fact.get('id'),
                'key': fact['key'],
                'value': fact['value'],
                'category': fact.get('category', 'personal'),
                'timestamp': fact.get('created_at', 'Stored in database'),
                'type': 'fact'
            })
        
        # Add learned contexts from database
        try:
            import sqlite3
            conn = sqlite3.connect('data/zephyr_memory.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, context_type, content, importance, created_at 
                FROM learned_context 
                ORDER BY importance DESC, created_at DESC
                LIMIT 20
            """)
            for row in cursor.fetchall():
                formatted_memory.append({
                    'id': row[0],
                    'key': row[1],  # context_type
                    'value': row[2],  # content
                    'category': row[1],
                    'timestamp': row[4],
                    'type': 'context',
                    'importance': row[3]
                })
            conn.close()
        except Exception as e:
            print(f"Could not load contexts: {e}")
        
        return jsonify({
            'success': True,
            'memory': formatted_memory,
            'count': len(formatted_memory)
        })
    
    except Exception as e:
        import traceback
        print(f"Memory endpoint error: {traceback.format_exc()}")
        return jsonify({
            'success': False,
            'error': str(e),
            'details': traceback.format_exc()
        }), 500

@app.route('/memory', methods=['POST'])
def add_memory():
    """Add a new memory entry to database"""
    try:
        from memory_db import store_user_fact
        data = request.json
        key = data.get('key', '')
        value = data.get('value', '')
        category = data.get('category', 'personal')
        
        if not key or not value:
            return jsonify({'error': 'Key and value required'}), 400
        
        store_user_fact(category, key, value)
        
        return jsonify({
            'success': True,
            'message': f'Remembered: {key} = {value}'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/memory', methods=['DELETE'])
def delete_memory():
    """Delete a memory entry (fact or context)"""
    try:
        from memory_db import delete_user_fact, delete_learned_context
        data = request.json
        
        # Check if deleting a fact or context
        if data.get('type') == 'fact':
            category = data.get('category', 'personal')
            key = data.get('key', '')
            
            if delete_user_fact(category, key):
                return jsonify({
                    'success': True,
                    'message': f'Deleted: {key}'
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Fact not found'
                }), 404
        
        elif data.get('type') == 'context':
            context_id = data.get('id')
            if context_id and delete_learned_context(context_id):
                return jsonify({
                    'success': True,
                    'message': 'Context deleted'
                })
            else:
                return jsonify({
                    'success': False,
                    'error': 'Context not found'
                }), 404
        
        else:
            return jsonify({
                'success': False,
                'error': 'Must specify type (fact or context) and identifier'
            }), 400
    
    except Exception as e:
        import traceback
        return jsonify({
            'success': False,
            'error': str(e),
            'details': traceback.format_exc()
        }), 500

@app.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects from database"""
    try:
        from projects import list_projects
        projects_list = list_projects()
        
        # Format projects for frontend
        formatted_projects = []
        for project in projects_list:
            formatted_projects.append({
                'name': project.get('name', 'Unnamed Project'),
                'description': project.get('description', 'No description'),
                'created': project.get('created_at', 'Unknown'),
                'status': 'Planning',  # Can enhance this later
                'tech_stack': []  # Can enhance this later
            })
        
        return jsonify({
            'success': True,
            'projects': formatted_projects,
            'count': len(formatted_projects)
        })
    
    except Exception as e:
        import traceback
        return jsonify({
            'success': False,
            'error': str(e),
            'details': traceback.format_exc()
        }), 500

@app.route('/projects', methods=['POST'])
def create_project_endpoint():
    """Create a new project in database"""
    try:
        from projects import create_project
        data = request.json
        name = data.get('name', '')
        description = data.get('description', '')
        
        if not name:
            return jsonify({'error': 'Project name required'}), 400
        
        result = create_project(name, description)
        
        return jsonify({
            'success': True,
            'message': f'Created project: {name}',
            'project': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/spotify/status', methods=['GET'])
def spotify_status():
    """Get current Spotify playback status"""
    try:
        # This will be implemented with actual Spotify integration
        return jsonify({
            'success': True,
            'playing': False,
            'track': None,
            'artist': None
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/spotify/control', methods=['POST'])
def spotify_control():
    """Control Spotify playback"""
    try:
        data = request.json
        action = data.get('action', '')
        
        # This will integrate with actual Spotify commands
        return jsonify({
            'success': True,
            'action': action,
            'message': f'Spotify {action} command executed'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/test', methods=['POST'])
def run_test():
    """Run a test command"""
    try:
        data = request.json
        test_type = data.get('type', '')
        
        result = {
            'success': True,
            'type': test_type,
            'timestamp': datetime.now().isoformat(),
            'message': f'Test {test_type} executed successfully'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    import sys
    import io
    
    # Fix Windows encoding issues
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    print("=" * 50)
    print("ZEPHYR API SERVER v3.0")
    print("=" * 50)
    print(f"Server: http://localhost:5000")
    print(f"Status: http://localhost:5000/health")
    print("Dashboard ready to connect")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
