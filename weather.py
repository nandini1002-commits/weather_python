import requests
import tkinter as tk
from tkinter import messagebox
# API endpoint and API key
API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key

def get_weather_data(location):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature
    }
    
    response = requests.get(API_ENDPOINT, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather_data(data):
    try:
        location = data["name"]
        temperature = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        
        weather_info = f"Weather in {location}:\n"
        weather_info += f"Temperature: {temperature}°C\n"
        weather_info += f"Wind Speed: {wind_speed} m/s\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Weather: {weather_description}"
        
        return weather_info
    except KeyError:
        return "Error: Unable to parse weather data."

def get_weather():
    location = location_entry.get()
    
    if location:
        data = get_weather_data(location)
        
        if data:
            weather_info = display_weather_data(data)
            result_label.config(text=weather_info)
        else:
            result_label.config(text="Error: Unable to retrieve weather data.")
    else:
        messagebox.showerror("Error", "Please enter a location.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create the location entry field
location_label = tk.Label(root, text="Enter Location:")
location_label.pack()

location_entry = tk.Entry(root, width=50)
location_entry.pack()

# Create the get weather button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Create the result label
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

root.mainloop()


