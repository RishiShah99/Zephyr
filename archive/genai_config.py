import os
import google.generativeai as genai

try:
    from api_keys import GEMINI_API_KEY
except Exception:
    GEMINI_API_KEY = None

def get_model():
    if not GEMINI_API_KEY:
        return None
    
    genai.configure(api_key=GEMINI_API_KEY)
    
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="I want you to extract key details from any sentence given to you but only give that key detail.",
    )
    
    return model

def start_chat_session(model):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": ["My name is Rishi Shah."],
            },
            {
                "role": "model",
                "parts": ["Rishi Shah"],
            },
            {
                "role": "user",
                "parts": ["I live in London Ontario"],
            },
            {
                "role": "model",
                "parts": ["London, Ontario"],
            },
            {
                "role": "user",
                "parts": ["Tell me all about the news regarding Microsoft"],
            },
            {
                "role": "model",
                "parts": ["Microsoft"],
            },
            {
                "role": "user",
                "parts": ["I live in Toronto Canada"],
            },
            {
                "role": "model",
                "parts": ["Toronto, Canada"],
            },
            {
                "role": "user",
                "parts": ["I want to create a new event on my calendar"],
            },
            {
                "role": "model",
                "parts": ["Create calendar event"],
            },
            {
                "role": "user",
                "parts": ["I want to skip this song"],
            },
            {
                "role": "model",
                "parts": ["Skip song"],
            },
            {
                "role": "user",
                "parts": ["Repeat this song"],
            },
            {
                "role": "model",
                "parts": ["Repeat song"],
            },
        ]
    )
    
    return chat_session

# Usage
if __name__ == "__main__":
    model = get_model()
    chat_session = start_chat_session(model)
    response = chat_session.send_message("INSERT_INPUT_HERE")
    print(response.text)
