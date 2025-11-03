import json
import requests
from typing import Any, Dict, List

# Put your OpenWeather API key here (required by the 'appid' parameter on each request).
API_KEY = "9431a24295d3090f9fd28868aa4f9822"

class WeatherError(Exception):
    pass

def display_and_store_weather(city: str, *, api_key: str = API_KEY, out_path: str = "results.json", lang: str = "en") -> None:
    """
    Fetch current weather for a city from OpenWeather and:
      1) print a single JSON object to the console, and
      2) append the same record to a local JSON file (results.json by default).
    """
    if not city or not city.strip():
        print(json.dumps({"error": "City not found. Please enter a valid city."}, ensure_ascii=False))
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,          # city name (e.g., "London" or "London,GB")
        "appid": api_key,   # API key must be passed as 'appid' on every call
        "units": "metric",  # Celsius
        "lang": lang        # description language
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
    except requests.RequestException:
        print(json.dumps({"error": "Unable to reach weather service. Please try again."}, ensure_ascii=False))
        return
    except ValueError:
        print(json.dumps({"error": "Invalid response from weather service."}, ensure_ascii=False))
        return

    # 'cod' can be int or string in responses; also check HTTP status.
    cod = str(data.get("cod", resp.status_code))
    if cod == "404":
        print(json.dumps({"error": "City not found. Please enter a valid city."}, ensure_ascii=False))
        return
    if cod == "401":
        print(json.dumps({"error": "Unauthorized. Check your API key."}, ensure_ascii=False))
        return
    if cod == "429":
        print(json.dumps({"error": "Too many requests. Please wait and try again."}, ensure_ascii=False))
        return
    if resp.status_code >= 500:
        print(json.dumps({"error": "Weather service is temporarily unavailable."}, ensure_ascii=False))
        return

    # Extract required fields from the documented schema
    name = data.get("name") or city
    main = data.get("main") or {}
    weather_list = data.get("weather") or []
    temp = main.get("temp")
    humidity = main.get("humidity")
    description = (weather_list[0].get("description") if weather_list else None)

    if temp is None or humidity is None or description is None:
        print(json.dumps({"error": "Weather data incomplete for this location."}, ensure_ascii=False))
        return

    record = {
        "city": name,
        "temp": round(float(temp)),
        "humidity": int(humidity),
        "weather": description.capitalize()
    }

    # 1) Print JSON to console
    print(json.dumps(record, ensure_ascii=False))

    # 2) Append to local JSON file
    try:
        existing: List[Dict[str, Any]] = []
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
                if not isinstance(existing, list):
                    existing = []
        except FileNotFoundError:
            existing = []
        except json.JSONDecodeError:
            existing = []

        existing.append(record)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
    except Exception:
        # Non-fatal: keep console output even if file write fails
        print(json.dumps({"warning": f"Could not write to {out_path}."}, ensure_ascii=False))

if __name__ == "__main__":
    # Example calls (edit API_KEY above and run)
    display_and_store_weather("London")
    # display_and_store_weather("New York")
    # display_and_store_weather("xyz123")  # shows JSON error