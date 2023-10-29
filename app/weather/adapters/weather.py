import requests
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API")

class Weather:
    def __init__(self):
        pass
    
    @staticmethod
    def get_weather(city: str):
        s_city = city
        city_id = 0
        appid = token
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                        params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = res.json()
            city = ["{} ({})".format(d['name'], d['sys']['country'])
                    for d in data['list']]
            city_id = data['list'][0]['id']
        except Exception as e:
            print("Exception (find):", e)
            pass

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print(data)
            conditions = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            cityy = data['name']
            country = data['sys']['country']
            humidity = data['main']['humidity']



        except Exception as e:
            print("Exception (weather):", e)
            pass
        data = {
            "country": country,
            "city": cityy,
            "city_id": city_id,
            "conditions": conditions,
            "temp": temp,
            "feels_like": feels_like,
            "humidity": humidity,
        }
        return data