import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
# -------------------------------
# OpenWeather API
# -------------------------------

API_KEY = " "
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# -------------------------------
# WINDOW
# -------------------------------
root = Tk()
root.title("Weather Dashboard")
root.geometry("1500x850")
root.resizable(False, False)

# -------------------------------
# BACKGROUND IMAGE
# -------------------------------
bg = Image.open("assets/background.png")
bg = bg.resize((1500, 850))

bg_photo = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# -------------------------------
# TITLE
# -------------------------------
title = Label(
    root,
    text="☁ WEATHER DASHBOARD",
    font=("Segoe UI", 30, "bold"),
    fg="white",
    bg="#0D2346"
)
title.place(x=120, y=40)

subtitle = Label(
    root,
    text="Your Weather, Your Way",
    font=("Segoe UI", 18),
    fg="#B8D8FF",
    bg="#0D2346"
)
subtitle.place(x=130, y=95)

# -------------------------------
# DATE
# -------------------------------
date_label = Label(
    root,
    font=("Segoe UI", 18),
    fg="white",
    bg="#0D2346"
)
date_label.place(x=1120, y=50)

# -------------------------------
# TIME
# -------------------------------
time_label = Label(
    root,
    font=("Segoe UI", 28, "bold"),
    fg="white",
    bg="#0D2346"
)
time_label.place(x=1120, y=90)

# -------------------------------
# CLOCK
# -------------------------------
def update_time():
    now = datetime.now()

    date = now.strftime("%A, %d %B %Y")
    current_time = now.strftime("%I:%M:%S %p")

    date_label.config(text=date)
    time_label.config(text=current_time)

    root.after(1000, update_time)

update_time()

# -------------------------------
# SEARCH FRAME
# -------------------------------
search_frame = Frame(
    root,
    bg="#173D7A"
)

search_frame.place(
    x=300,
    y=180,
    width=600,
    height=70
)

# -------------------------------
# CITY ENTRY
# -------------------------------
city_entry = Entry(
    search_frame,
    font=("Segoe UI", 18),
    bd=0,
    fg="white",
    bg="#173D7A",
    insertbackground="white"
)

city_entry.place(
    x=20,
    y=18,
    width=550
)

city_entry.insert(0, "Enter City Name")

def remove_text(event):
    if city_entry.get() == "Enter City Name":
        city_entry.delete(0, END)

city_entry.bind("<FocusIn>", remove_text)

# -------------------------------
# SEARCH BUTTON
# -------------------------------
search_button = Button(
    root,
    text="🔍 Search",
    font=("Segoe UI", 16, "bold"),
    bg="#1F6BFF",
    fg="white",
    bd=0,
    cursor="hand2"
)

search_button.place(
    x=930,
    y=180,
    width=180,
    height=70
)

# -------------------------------
# CLEAR BUTTON
# -------------------------------
def clear():
    city_entry.delete(0, END)

clear_button = Button(
    root,
    text="Clear",
    font=("Segoe UI", 16, "bold"),
    bg="#203A63",
    fg="white",
    bd=0,
    cursor="hand2",
    command=clear
)

clear_button.place(
    x=1130,
    y=180,
    width=150,
    height=70
)

# -------------------------------
# WEATHER CARD
# -------------------------------
weather_card = Frame(
    root,
    bg="#163A73",
    bd=0
)

weather_card.place(
    x=170,
    y=300,
    width=1160,
    height=360
)

# -------------------------------
# WEATHER ICON
# -------------------------------
icon = Label(
    weather_card,
    text="☁",
    font=("Segoe UI Emoji", 90),
    fg="white",
    bg="#163A73"
)

icon.place(x=60, y=30)

# -------------------------------
# TEMPERATURE
# -------------------------------
temperature = Label(
    weather_card,
    text="--°C",
    font=("Segoe UI", 56, "bold"),
    fg="white",
    bg="#163A73"
)

temperature.place(x=50, y=170)

# -------------------------------
# CONDITION
# -------------------------------
condition = Label(
    weather_card,
    text="Weather Condition",
    font=("Segoe UI", 22),
    fg="white",
    bg="#163A73"
)

condition.place(x=60, y=260)

# -------------------------------
# LOCATION
# -------------------------------
location = Label(
    weather_card,
    text="City, Country",
    font=("Segoe UI", 18),
    fg="#B8D8FF",
    bg="#163A73"
)

location.place(x=60, y=310)
# -------------------------------
# FEELS LIKE
# -------------------------------
feels_title = Label(weather_card,text="Feels Like",
font=("Segoe UI",18),fg="white",bg="#163A73")
feels_title.place(x=500,y=40)

feels_value = Label(weather_card,text="--°C",
font=("Segoe UI",18),fg="#B8D8FF",bg="#163A73")
feels_value.place(x=700,y=40)

# -------------------------------
# HUMIDITY
# -------------------------------
humidity_title = Label(weather_card,text="Humidity",
font=("Segoe UI",18),fg="white",bg="#163A73")
humidity_title.place(x=500,y=90)

humidity_value = Label(weather_card,text="--%",
font=("Segoe UI",18),fg="#B8D8FF",bg="#163A73")
humidity_value.place(x=700,y=90)

# -------------------------------
# WIND SPEED
# -------------------------------
wind_title = Label(weather_card,text="Wind Speed",
font=("Segoe UI",18),fg="white",bg="#163A73")
wind_title.place(x=500,y=140)

wind_value = Label(weather_card,text="-- m/s",
font=("Segoe UI",18),fg="#B8D8FF",bg="#163A73")
wind_value.place(x=700,y=140)

# -------------------------------
# PRESSURE
# -------------------------------
pressure_title = Label(weather_card,text="Pressure",
font=("Segoe UI",18),fg="white",bg="#163A73")
pressure_title.place(x=500,y=190)

pressure_value = Label(weather_card,text="---- hPa",
font=("Segoe UI",18),fg="#B8D8FF",bg="#163A73")
pressure_value.place(x=700,y=190)

# -------------------------------
# VISIBILITY
# -------------------------------
visibility_title = Label(weather_card,text="Visibility",
font=("Segoe UI",18),fg="white",bg="#163A73")
visibility_title.place(x=500,y=240)

visibility_value = Label(weather_card,text="-- km",
font=("Segoe UI",18),fg="#B8D8FF",bg="#163A73")
visibility_value.place(x=700,y=240)
# -------------------------------
# SUNRISE
# -------------------------------
sunrise_title = Label(
    weather_card,
    text="Sunrise",
    font=("Segoe UI",18),
    fg="white",
    bg="#163A73"
)
sunrise_title.place(x=850,y=40)

sunrise_value = Label(
    weather_card,
    text="--:--",
    font=("Segoe UI",18),
    fg="#B8D8FF",
    bg="#163A73"
)
sunrise_value.place(x=980,y=40)

# -------------------------------
# SUNSET
# -------------------------------
sunset_title = Label(
    weather_card,
    text="Sunset",
    font=("Segoe UI",18),
    fg="white",
    bg="#163A73"
)
sunset_title.place(x=850,y=90)

sunset_value = Label(
    weather_card,
    text="--:--",
    font=("Segoe UI",18),
    fg="#B8D8FF",
    bg="#163A73"
)
sunset_value.place(x=980,y=90)

# -------------------------------
# MIN TEMP
# -------------------------------
min_title = Label(
    weather_card,
    text="Min Temp",
    font=("Segoe UI",18),
    fg="white",
    bg="#163A73"
)
min_title.place(x=850,y=140)

min_value = Label(
    weather_card,
    text="--°C",
    font=("Segoe UI",18),
    fg="#B8D8FF",
    bg="#163A73"
)
min_value.place(x=980,y=140)

# -------------------------------
# MAX TEMP
# -------------------------------
max_title = Label(
    weather_card,
    text="Max Temp",
    font=("Segoe UI",18),
    fg="white",
    bg="#163A73"
)
max_title.place(x=850,y=190)

max_value = Label(
    weather_card,
    text="--°C",
    font=("Segoe UI",18),
    fg="#B8D8FF",
    bg="#163A73"
)
max_value.place(x=980,y=190)

# -------------------------------
# LAST UPDATED
# -------------------------------
updated_title = Label(
    weather_card,
    text="Updated",
    font=("Segoe UI",18),
    fg="white",
    bg="#163A73"
)
updated_title.place(x=850,y=240)

updated_value = Label(
    weather_card,
    text="--:--",
    font=("Segoe UI",18),
    fg="#B8D8FF",
    bg="#163A73"
)
updated_value.place(x=980,y=240)

# -------------------------------
# GET WEATHER FUNCTION
# -------------------------------
def get_weather():

    city = city_entry.get().strip()

    if city == "" or city == "Enter City Name":
        condition.config(text="Please enter a city")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(BASE_URL, params=params)

        data = response.json()

        if response.status_code != 200:
            condition.config(text="City Not Found")
            return

        temperature.config(
            text=f"{data['main']['temp']:.1f}°C"
        )

        condition.config(
            text=data["weather"][0]["description"].title()
        )

        location.config(
            text=f"{data['name']}, {data['sys']['country']}"
        )

        feels_value.config(
            text=f"{data['main']['feels_like']:.1f}°C"
        )

        humidity_value.config(
            text=f"{data['main']['humidity']}%"
        )

        wind_value.config(
            text=f"{data['wind']['speed']} m/s"
        )

        pressure_value.config(
            text=f"{data['main']['pressure']} hPa"
        )

        visibility_value.config(
            text=f"{data['visibility']/1000:.1f} km"
        )


        # -------------------------------
        # SUNRISE AND SUNSET
        # -------------------------------

        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"]
        ).strftime("%I:%M %p")

        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"]
        ).strftime("%I:%M %p")


        sunrise_value.config(
            text=sunrise
        )

        sunset_value.config(
            text=sunset
        )


        # -------------------------------
        # MIN AND MAX TEMPERATURE
        # -------------------------------

        min_value.config(
            text=f"{data['main']['temp_min']:.1f}°C"
        )

        max_value.config(
            text=f"{data['main']['temp_max']:.1f}°C"
        )


        # -------------------------------
        # UPDATED TIME
        # -------------------------------

        updated_value.config(
            text=datetime.now().strftime("%I:%M:%S %p")
        )


    except Exception:
        condition.config(text="Network Error")


# -------------------------------
# CONNECT SEARCH BUTTON
# -------------------------------
search_button.config(command=get_weather)

# -------------------------------
# START APPLICATION
# -------------------------------
root.mainloop()