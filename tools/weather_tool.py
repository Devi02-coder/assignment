import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    """
    Get current weather for a city using OpenWeatherMap API
    
    Args:
        city: City name (e.g., "Bangalore", "Delhi")
    
    Returns:
        Dictionary with weather information
    """
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except Exception as e:
        return {"error": f"Weather API error: {str(e)}"}
