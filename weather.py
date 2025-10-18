import requests

try:
    from api_keys import WEATHER_API_KEY
except Exception:
    WEATHER_API_KEY = None

def get_weather(location):
    if not WEATHER_API_KEY:
        return "Weather API not configured. Get a free key from https://www.weatherapi.com/ and add it to api_keys.py"
    
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}"
    response = requests.get(url)
    data = response.json()
    print(data)
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    response = f"The weather in {location} is {temperature} degrees Celsius with {condition}. It feels like {data['current']['feelslike_c']} degrees Celsius."
    return response
