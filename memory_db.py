"""
Persistent memory system for Zephyr using SQLite
Stores user facts, preferences, and conversation history
"""
import sqlite3
import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "zephyr_memory.db"

def init_db():
    """Initialize the database with required tables"""
    DB_PATH.parent.mkdir(exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Table for user facts/preferences
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(category, key)
        )
    """)
    
    # Table for conversation history
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Table for learned context (things Zephyr learns over time)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learned_context (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context_type TEXT NOT NULL,
            content TEXT NOT NULL,
            importance INTEGER DEFAULT 5,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"[OK] Memory database initialized at {DB_PATH}")


def store_user_fact(category, key, value):
    """Store or update a user fact"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO user_facts (category, key, value, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(category, key) DO UPDATE SET
            value = excluded.value,
            updated_at = CURRENT_TIMESTAMP
    """, (category, key, value))
    
    conn.commit()
    conn.close()


def delete_user_fact(category, key):
    """Delete a specific user fact"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM user_facts 
        WHERE category = ? AND key = ?
    """, (category, key))
    
    conn.commit()
    rows_deleted = cursor.rowcount
    conn.close()
    return rows_deleted > 0


def delete_learned_context(context_id):
    """Delete a learned context by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM learned_context 
        WHERE id = ?
    """, (context_id,))
    
    conn.commit()
    rows_deleted = cursor.rowcount
    conn.close()
    return rows_deleted > 0


def get_user_facts(category=None):
    """Get all user facts, optionally filtered by category"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if category:
        cursor.execute("""
            SELECT category, key, value FROM user_facts
            WHERE category = ?
            ORDER BY updated_at DESC
        """, (category,))
    else:
        cursor.execute("""
            SELECT category, key, value FROM user_facts
            ORDER BY updated_at DESC
        """)
    
    facts = cursor.fetchall()
    conn.close()
    
    # Return as dict
    return [{"category": f[0], "key": f[1], "value": f[2]} for f in facts]


def add_to_conversation(role, message):
    """Add a message to conversation history"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO conversation_history (role, message)
        VALUES (?, ?)
    """, (role, message))
    
    conn.commit()
    conn.close()


def get_recent_conversation(limit=20):
    """Get recent conversation history"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT role, message, timestamp FROM conversation_history
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    
    messages = cursor.fetchall()
    conn.close()
    
    # Return in chronological order (oldest first)
    return [{"role": m[0], "message": m[1], "timestamp": m[2]} for m in reversed(messages)]


def clear_old_conversations(keep_last=100):
    """Keep only the most recent N conversations to prevent DB bloat"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM conversation_history
        WHERE id NOT IN (
            SELECT id FROM conversation_history
            ORDER BY timestamp DESC
            LIMIT ?
        )
    """, (keep_last,))
    
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    
    return deleted


def store_learned_context(context_type, content, importance=5):
    """Store something Zephyr learned (for long-term memory)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO learned_context (context_type, content, importance)
        VALUES (?, ?, ?)
    """, (context_type, content, importance))
    
    conn.commit()
    conn.close()


def get_learned_context(context_type=None, min_importance=3):
    """Get learned context, optionally filtered"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if context_type:
        cursor.execute("""
            SELECT context_type, content, importance, created_at
            FROM learned_context
            WHERE context_type = ? AND importance >= ?
            ORDER BY importance DESC, created_at DESC
        """, (context_type, min_importance))
    else:
        cursor.execute("""
            SELECT context_type, content, importance, created_at
            FROM learned_context
            WHERE importance >= ?
            ORDER BY importance DESC, created_at DESC
        """, (min_importance,))
    
    contexts = cursor.fetchall()
    conn.close()
    
    return [{"type": c[0], "content": c[1], "importance": c[2], "created_at": c[3]} for c in contexts]


def build_context_for_ai():
    """Build a context string to send to the AI with each request"""
    facts = get_user_facts()
    recent_convo = get_recent_conversation(limit=3)  # Only last 3 exchanges to avoid confusion
    learned = get_learned_context(min_importance=7)
    
    context_parts = []
    
    # User facts organized by category
    if facts:
        facts_str = "=== ABOUT USER ===\n"
        
        # Organize by category
        categories = {}
        for fact in facts:
            cat = fact['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(f"{fact['key']}: {fact['value']}")
        
        for category, items in categories.items():
            facts_str += f"\n{category.upper()}:\n"
            for item in items:
                facts_str += f"  • {item}\n"
        
        context_parts.append(facts_str.strip())
    
    # Important learned context
    if learned:
        learned_str = "\n=== LEARNED ABOUT USER ===\n"
        for item in learned[:8]:  # Top 8 most important
            learned_str += f"  • {item['content']}\n"
        context_parts.append(learned_str.strip())
    
    # Recent conversation (for continuity)
    if recent_convo:
        convo_str = "\n=== RECENT CONVERSATION ===\n"
        for msg in recent_convo[-6:]:  # Last 6 messages
            role = "User" if msg['role'] == 'user' else "Zephyr"
            convo_str += f"{role}: {msg['message']}\n"
        context_parts.append(convo_str.strip())
    
    return "\n\n".join(context_parts)


def get_memory_stats():
    """Get statistics about stored memory"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM user_facts")
    fact_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM conversation_history")
    convo_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM learned_context")
    learned_count = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        "user_facts": fact_count,
        "conversations": convo_count,
        "learned_items": learned_count
    }


# Initialize on import
init_db()


if __name__ == "__main__":
    # Test the memory system
    print("Testing Zephyr Memory System...")
    print()
    
    # Store some facts
    store_user_fact("personal", "name", "Rishi")
    store_user_fact("personal", "occupation", "Developer")
    store_user_fact("preferences", "language", "Python")
    store_user_fact("preferences", "ai_model", "Groq")
    
    # Add conversation
    add_to_conversation("user", "Hello Zephyr!")
    add_to_conversation("assistant", "Hi Rishi! How can I help you today?")
    add_to_conversation("user", "What's my name?")
    add_to_conversation("assistant", "Your name is Rishi!")
    
    # Store learned context
    store_learned_context("habit", "User prefers working late at night", importance=8)
    store_learned_context("project", "Currently building Zephyr AI assistant", importance=9)
    
    # Build context
    context = build_context_for_ai()
    print("Context for AI:")
    print("=" * 50)
    print(context)
    print("=" * 50)
    print()
    
    # Stats
    stats = get_memory_stats()
    print("Memory Stats:")
    print(f"  User Facts: {stats['user_facts']}")
    print(f"  Conversations: {stats['conversations']}")
    print(f"  Learned Items: {stats['learned_items']}")
