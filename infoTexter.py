import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from emailServer import sendEmail
import json

load_dotenv() # load .env file
# Variables
weatherKey = os.getenv('WEATHER_API')
stockKey = os.getenv('STOCK_API')
newsKey = os.getenv('NEWS_API')

def readSet(filename):
    with open(f'./data/{filename}', 'r') as infile:
        data = json.load(infile) 

    return data

def writeSet(data, filename):    
    with open(f'./data/{filename}', 'w') as outfile:
        json.dump(data, outfile)

def getNews():
    country = 'us'
    r = requests.get('https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country, newsKey))
    data = r.json()
    # data = readSet('newsData.json')
    my_list = []
    body = "\n"

    for i in range(0,3):
        if data['articles'][i]['url'] == "https://removed.com":
            continue
        my_list.append({'title' : data['articles'][i]['title'], 'url' : data['articles'][i]['url']})
        body += "Title: {title}\nURL: {url}\n\n".format(title = my_list[i]['title'], url = my_list[i]['url'])

    return body

def getStocks():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={key}'.format(key=stockKey)
    r = requests.get(url)
    data = r.json()

    first_entry = next(iter(data['Time Series (5min)']))
    return data['Time Series (5min)'][first_entry]

def getWeather():
    try:
        def tempToF(temp):
            return (temp - 273.15) * (9/5) + 32
        lat, lon = '39.10', '-84.51' #Cincinnati
        # r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'.format(lat = lat, lon = lon, key = weatherKey))
        # data = r.json()
        data = readSet('weatherData.json')

        temp = ('{:.2f}°F').format(tempToF(data['main']['temp']))
        description = data['weather'][0]['description']
        return f'{temp}\n{description}'
    except Exception as e:
        return "Error occured with getting Weather information"

def getTraffic():
    apiKey = 'mdlAqBInDu2FD5pUFvPU4F9n74TwVvCp'
    

def main():
    # tempData = getWeather()
    # pprint(tempData)
    data = getNews() + getWeather()
    # pprint(data)
    sendEmail(data)

main()
