import speech_recognition as sr
import pyttsx3
from weather import get_weather
from planner import create_event, see_future_events
from news import get_top_news, get_everything_news
from nlp import parse_command, extract_details
    
def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command:
            perform_command(command)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except Exception as e:
            print(e)
            speak("Sorry, I didn't catch that.")
            return None

def perform_command(command):
    parsedcommand = parse_command(command)
    if parsedcommand == "weather":
        speak("What is your location?")
        location = listen()
        if location:
            location_details = extract_details(location)
            if location_details:
                weather = get_weather(location_details)
                speak(weather)
            else:
                speak("I'm sorry, I didn't understand that.")

    elif parsedcommand == "calendar":
        speak("What would you like to do with your calendar?")
        action = listen()
        if action:
            action_details = extract_details(action)
            if "create" in action_details:
                speak("What is the name of the event?")
                name = listen()
                if name:
                    create_event(name)
                    speak(f"Event {name} has been created.")
            elif "events" in action_details:
                events = see_future_events()
                speak(events)

    elif parsedcommand == "news":
        speak("What topic are you interested in?")
        topic = listen()
        if topic:
            topic_details = extract_details(topic)
            print(topic_details)
            speak ("What type of news would you like to hear? Top news or everything?")
            news_type = listen()
            if news_type == "top news":
                print("Getting top news")
                news = get_top_news(topic_details)
                speak(news)
            elif news_type == "everything":
                print("Getting everything news")
                news = get_everything_news(topic_details)
                speak(news)
            else:
                speak("I'm sorry, I didn't understand that.")

    else:
        speak("I'm sorry, I didn't understand that.")

def speak(text):
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
