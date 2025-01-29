#!/usr/bin/env python
import requests

def main(city):
    # Your main code goes here
    API_KEY = "your_actual_api_key"  # Make sure to replace this with your actual API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}  # Use "imperial" for Fahrenheit
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"The temperature in {city} is {temp}°C with {weather}.")
    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'City not found. Please check the name.')}")

if __name__ == "__main__":
    city_name = input("Enter a city: ")
    main(city_name)