
# Weather App with Live OpenWeather API

## Project Description
A Python-based weather application that fetches real-time weather information and a 5-day forecast for any valid city using the OpenWeather API.

## Technologies Used
- Python
- Requests
- OpenWeather API
- Python Dotenv
- JSON

## Features
- Displays current temperature.
- Shows humidity and weather description.
- Displays wind speed.
- Provides a 5-day weather forecast.
- Handles invalid cities and API errors.
- Keeps the API key secure using an environment file.

## Installation

Install the required libraries:

pip install requests python-dotenv

## How to Run

Run the application:

python weather_app.py

## API Key Setup

Create a .env file and add:

OPENWEATHER_KEY=your_api_key_here

Never upload the .env file to GitHub.

## Data Source
https://openweathermap.org/
