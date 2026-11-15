
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather_data(url, city):
    try:
        response = requests.get(
            url,
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )

        if response.status_code == 404:
            print("City not found. Please enter a valid city.")
            return None

        if response.status_code == 401:
            print("Invalid API key or key not activated yet.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print("Network problem:", error)
        return None


def display_current_weather(city):
    data = get_weather_data(CURRENT_URL, city)

    if not data:
        return False

    print("\n========== CURRENT WEATHER ==========")
    print("City:", data.get("name", city))

    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    wind = data.get("wind", {})

    print("Temperature:", main.get("temp", "N/A"), "°C")
    print("Humidity:", main.get("humidity", "N/A"), "%")
    print("Weather:", weather.get("description", "N/A"))
    print("Wind Speed:", wind.get("speed", "N/A"), "m/s")

    return True


def display_forecast(city):
    data = get_weather_data(FORECAST_URL, city)

    if not data:
        return

    print("\n========== 5-DAY FORECAST ==========")

    daily_forecast = {}

    for item in data.get("list", []):
        date = item.get("dt_txt", "")[:10]

        if date and date not in daily_forecast:
            daily_forecast[date] = item

    for date, item in daily_forecast.items():
        temperature = item.get("main", {}).get("temp", "N/A")
        description = item.get("weather", [{}])[0].get(
            "description", "N/A"
        )

        formatted_date = datetime.strptime(
            date, "%Y-%m-%d"
        ).strftime("%d-%m-%Y")

        print(
            formatted_date,
            "| Temperature:", temperature, "°C",
            "|", description
        )


def main():
    print("====================================")
    print("       LIVE WEATHER APPLICATION")
    print("====================================")

    if not API_KEY:
        print("API key missing! Please add it to your .env file.")
        return

    while True:
        city = input("\nEnter city name (press Enter to exit): ").strip()

        if not city:
            print("Thank you for using the Weather App!")
            break

        if display_current_weather(city):
            display_forecast(city)


if __name__ == "__main__":
    main()
