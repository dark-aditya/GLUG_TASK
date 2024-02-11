import requests
from bs4 import BeautifulSoup
from config import API_KEY
import json

def get_weather_data(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    # Make a request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response with BeautifulSoup (not the typical use case)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Convert the JSON data from a string to a dictionary
        weather_data = json.loads(str(soup))

        # Extract temperature, humidity, and wind speed information
        temperature_celsius = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        return temperature_celsius, humidity, wind_speed
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None, None, None

def main():
    api_key = API_KEY
    city = input("Enter the city name: ")
    temperature, humidity, wind_speed = get_weather_data(api_key, city)

    if temperature is not None:
        print(f"The current temperature in {city} is {temperature:.2f} degrees Celsius.")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    main()
