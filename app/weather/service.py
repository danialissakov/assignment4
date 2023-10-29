import os

from dotenv import load_dotenv
from .adapters.weather import Weather
load_dotenv()


class Service:
    def __init__(self,weather_service):
        self.weather_service = weather_service


def get_service():
    weather_servce = Weather()
    svc = Service(weather_servce)
    return svc
