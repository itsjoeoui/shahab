import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("OPENWEATHER")
serviceurl = "https://api.openweathermap.org/data/2.5/weather?"


def get_weather(city):
    r = requests.get(serviceurl,
                     params={
                         "q": city,
                         "appid": TOKEN,
                         "units": "metric"
                     })
    return r.json()
