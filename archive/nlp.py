import spacy
from genai_config import get_model, start_chat_session

nlp = spacy.load('en_core_web_sm')
model = get_model()
chat_session = start_chat_session(model)

def parse_command(command):
    doc = nlp(command)
    if any(token.lemma_ == 'weather' for token in doc):
        return 'weather'
    elif any(token.lemma_ == 'calendar' for token in doc):
        return 'calendar'
    elif any(token.lemma_ == 'news' for token in doc):
        return 'news'
    elif any(token.lemma_ == 'spotify' for token in doc):
        return 'spotify'
    else:
        return 'other'

def extract_details(text):
    response = chat_session.send_message(text)
    return response.text