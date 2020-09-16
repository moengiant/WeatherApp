import tkinter as tk
import sqlite3
import pathlib
import sys
import requests
import json
from PIL import ImageTk, Image


class cipher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        height = 700
        width = 800
        global label
        
        self.title("Weather App")
        pic1 = "1.jpg"

        canvas = tk.Canvas(self, height = height , width = width)
        canvas.pack()
        
        bg_image = ImageTk.PhotoImage(Image.open(pic1).resize((width, height), Image.ANTIALIAS))
        canvas.background = bg_image
        canvas.create_image(0,0, anchor=tk.NW, image = bg_image)
        
        frame = tk.Frame(canvas, bg = '#80c1FF', bd=5)
        frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor="n")
        
        entry = tk.Entry(frame, font = ("arial", 18))
        entry.place(relwidth=.65, relheight = 1)

        button = tk.Button(frame, text = "submit", font = ("arial", 18), command=lambda: self.get_weather(entry.get()))
        button.place(relx = .7, relwidth = .3, relheight = 1)

        lower_frame = tk.Frame(canvas, bg = '#80c1FF', bd=5) 
        lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor="n")

        label = tk.Label(lower_frame, font = ("arial", 28))
        label.place(relwidth = 1, relheight = 1)

    # Function to return values from json
    def format_response(self, weather):
        try:
            temp = weather['list'][0]['main']['temp']
            condition = weather['list'][0]['weather'][0]['description']
            return_str = "Condition: " + str(condition) + "\n Temperature: " + str(round(temp)) + "\u00b0 F"
        except:
            return_str = "City not found"

        return return_str
           
    # function to call open weather map api
    def get_weather(self, city):
        # Sign up at open weather map to get an api key
        #api.openweathermap.org/data/2.5/forecast?q={city}&appid={api key}
        api_key = " " # add api key between the quotes
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {'q' : city, 'appid' : api_key, 'units' : 'imperial'}
        response = requests.get(url, params = params)
        weather = response.json()
        # print(json.dumps(weather, indent=1))
        label['text'] = self.format_response(weather)

app = cipher()
app.mainloop()

