import requests
import json

def display_weather(city: str, api_key: str, units: str = "metric", lang: str = "en", timeout: tuple = (5, 10)) -> None:
    """
    Fetch and print current weather for a city from OpenWeatherMap as pretty JSON.
    Prints a generic error message on any error (invalid URL, timeout, bad API key, etc.).
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,         # city name, e.g., "Chennai,IN"
        "appid": api_key,  # your OpenWeatherMap API key
        "units": units,    # "standard" (default), "metric", or "imperial"
        "lang": lang       # response language code
    }
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
    except (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.InvalidURL,
        requests.exceptions.HTTPError,
        requests.exceptions.RequestException,
    ):
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    API_KEY = "9431a24295d3090f9fd28868aa4f9822"
    city_name = input("Enter city name: ").strip()
    display_weather(city_name, API_KEY)