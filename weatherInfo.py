import requests
from pprint import pprint
import json

def tempToF(temp):
    return (temp - 273.15) * (9/5) + 32

apiKey = '0ca295f5433f830a80307a6e14690a92'
lat = '39.10'; lon = '-84.51' #Cincinnati
r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'.format(lat = lat, lon = lon, key = apiKey))
data = r.json()

with open('./data/weatherData.json', 'r') as infile:
    weatherDataTest = json.load(infile)
temp = ('{:.2f}°F').format(tempToF(weatherDataTest['main']['temp']))
description = weatherDataTest['weather'][0]['description']
pprint(temp)
print(description)

