import requests

def display_weather_summary(city: str, api_key: str) -> None:
    """
    Fetch current weather for a city from OpenWeatherMap and print:
    City, Temperature (°C), Humidity (%), Weather (description).
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,         # city name (e.g., "London" or "London,GB")
        "appid": api_key,  # your OpenWeatherMap API key
        "units": "metric", # Celsius per Task 3 expected output
        "lang": "en"
    }
    data = requests.get(url, params=params).json()
    city_name = data.get("name", city)
    temp_c = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"City: {city_name}")
    print(f"Temperature: {temp_c}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description.capitalize()}")

if __name__ == "__main__":
    API_KEY = "9431a24295d3090f9fd28868aa4f9822"
    city_name = input("Enter city name: ").strip()
    display_weather_summary(city_name, API_KEY)