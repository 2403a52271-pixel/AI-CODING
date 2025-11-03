import requests
import json

def display_weather(city: str, api_key: str, units: str = "metric", lang: str = "en") -> None:
    """
    Fetch and print current weather for a city from OpenWeatherMap as pretty JSON.
    No error handling by design (per prompt).
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,         # city name (e.g., "London" or "London,GB")
        "appid": api_key,  # your OpenWeatherMap API key
        "units": units,    # "standard" (default), "metric", or "imperial"
        "lang": lang       # response language (e.g., "en", "hi", etc.)
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))

if __name__ == "__main__":   # ✅ FIXED HERE
    API_KEY = "9431a24295d3090f9fd28868aa4f9822"
    city_name = input("Enter city name: ").strip()
    display_weather(city_name, API_KEY)
