import requests
import json
import os

def display_and_store_weather_details(city_name):
    api_key = 'df8afcace6b1e634119e1ccc754c8e9d'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unknown Error')}")
            return
        weather_json = json.dumps(data, indent=4)
        print(weather_json)
        # Store to text file, appending
        filename = "weather_details.txt"
        with open(filename, "a", encoding='utf-8') as f:
            f.write(weather_json + "\n")
        print(f"Weather details appended to {filename}")
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the weather service: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_and_store_weather_details(city)
