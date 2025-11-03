import requests

def display_weather_info(city_name):
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
        temp = data.get('main', {}).get('temp')
        humidity = data.get('main', {}).get('humidity')
        desc = data.get('weather', [{}])[0].get('description', '')
        print(f"City: {city_name}")
        if temp is not None:
            print(f"Temperature: {temp}°C")
        else:
            print("Temperature: Data not available")
        if humidity is not None:
            print(f"Humidity: {humidity}%")
        else:
            print("Humidity: Data not available")
        print(f"Weather: {desc.capitalize() if desc else 'Data not available'}")
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the weather service: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather_info(city)
