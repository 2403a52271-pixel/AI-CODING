import requests
import json

def display_city_weather(city_name):
    api_key = 'df8afcace6b1e634119e1ccc754c8e9d'  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        if weather_data.get("cod") != 200:
            print(f"Error: {weather_data.get('message', 'Unknown Error')}")
        else:
            print(json.dumps(weather_data, indent=4))
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the weather service: {e}")

# Example usage:
if __name__ == "__main__":
    city = input("Enter city name: ")
    display_city_weather(city)
