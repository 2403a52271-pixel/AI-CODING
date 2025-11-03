import requests

# Hardcode your API key here (replace with your real key).
API_KEY = "9431a24295d3090f9fd28868aa4f9822"

class WeatherError(Exception):
    pass

def display_weather_summary(city: str, api_key: str) -> None:
    """
    Fetch current weather for a city from OpenWeatherMap and print:
    City, Temperature (°C), Humidity (%), Weather (description).
    """
    if not city or not city.strip():
        print("Error: City not found. Please enter a valid city.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,          # e.g., "London" or "London,GB"
        "appid": api_key,   # required API key parameter
        "units": "metric",  # Celsius
        "lang": "en"
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
    except requests.RequestException:
        print("Error: Unable to reach weather service. Please try again.")
        return

    # Handle common API error statuses (both HTTP and 'cod' in JSON)
    try:
        payload = resp.json()
    except ValueError:
        print("Error: Invalid response from weather service.")
        return

    cod = str(payload.get("cod", resp.status_code))  # 'cod' may be int or str

    if cod == "404":
        print("Error: City not found. Please enter a valid city.")
        return
    if cod == "401":
        print("Error: Unauthorized. Check your API key.")
        return
    if cod == "429":
        print("Error: Too many requests. Please wait and try again.")
        return
    if resp.status_code >= 500:
        print("Error: Weather service is temporarily unavailable.")
        return

    # Extract fields safely per API schema
    name = payload.get("name") or city
    main = payload.get("main") or {}
    weather_list = payload.get("weather") or []
    temp_c = main.get("temp")
    humidity = main.get("humidity")
    description = (weather_list[0].get("description") if weather_list else "N/A")

    if temp_c is None or humidity is None:
        print("Error: Weather data incomplete for this location.")
        return

    print(f"City: {name}")
    print(f"Temperature: {round(float(temp_c))}°C")
    print(f"Humidity: {int(humidity)}%")
    print(f"Weather: {description.capitalize()}")

if __name__ == "__main__":
    # Direct function calls (no console input)
    display_weather_summary("New York", API_KEY)
    # Uncomment to test invalid city handling:
    # display_weather_summary("xyz123", API_KEY)