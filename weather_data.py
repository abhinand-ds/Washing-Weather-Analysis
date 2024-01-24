import requests as rq
import json
import config

API_KEY = config.API_KEY
ZIPCODE = 'FK9 5AL'
URL = f'https://api.openweathermap.org/data/2.5/weather?q=Stirling,UK&appid={API_KEY}&units=metric'

def data():
    response = rq.get(URL)
    value = response.json()
    temprature = value['main']['temp']
    feel_like = value['main']['feels_like']
    pressure = value['main']['pressure']
    wind_speed = value['wind']['speed']
    return [f'{temprature} C',f'{feel_like} C',f'{pressure} hPa ',f'{wind_speed} m/s']

