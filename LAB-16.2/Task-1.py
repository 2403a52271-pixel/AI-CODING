import requests
import json

def get_weather_details(city_name):
    api_key = 'df8afcace6b1e634119e1ccc754c8e9d'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather_details(city)
