import requests

def display_city_weather_details(city_name):
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
        if data.get("cod") == "404":
            print("Error: City not found. Please enter a valid city.")
            return
        elif data.get("cod") != 200:
            print(f"Error: {data.get('message', 'Unknown Error')}")
            return
        city = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "Unknown")
        temp = data.get("main", {}).get("temp")
        humidity = data.get("main", {}).get("humidity")
        weather_desc = ""
        if data.get("weather") and isinstance(data["weather"], list) and len(data["weather"]) > 0:
            weather_desc = data["weather"][0].get("description", "")
        
        print(f"Weather Details for {city}, {country}:")
        if temp is not None:
            print(f"  Temperature: {temp}°C")
        else:
            print("  Temperature: Data not available")
        if humidity is not None:
            print(f"  Humidity: {humidity}%")
        else:
            print("  Humidity: Data not available")
        print(f"  Condition: {weather_desc.capitalize() if weather_desc else 'Data not available'}")
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the weather service: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_city_weather_details(city)
