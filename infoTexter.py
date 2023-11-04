import requests
from pprint import pprint
from emailServer import sendEmail
import datetime
import json

def readSet(filename):
    with open(f'./data/{filename}', 'r') as infile:
        data = json.load(infile) 

    return data

def writeSet(data, filename):    
    with open(f'./data/{filename}', 'w') as outfile:
        json.dump(data, outfile)

def getNews():
    newsAPIKey = '64f44e13e28b4068ab0bbae7d3c074a7'
    country = 'us'
    # r = requests.get('https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country, newsAPIKey))
    # data = r.json()
    data = readSet('newsData.json')
    my_list = []
    body = "\n"

    for i in range(0,3):
        my_list.append({'title' : data['articles'][i]['title'], 'url' : data['articles'][i]['url']})
        body += "Title: {title}\nURL: {url}\n\n".format(title = my_list[i]['title'], url = my_list[i]['url'])

    return data

def getStocks():
    vantageAPIKey = 'JFS0LR00E05LA2QI'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={key}'.format(key=vantageAPIKey)
    r = requests.get(url)
    data = r.json()

    first_entry = next(iter(data['Time Series (5min)']))
    pprint(data['Time Series (5min)'][first_entry])
    return data['Time Series (5min)'][first_entry]

def getWeather():
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
    return temp + '\n' + description

def main():
    tempData = getWeather()
    pprint(tempData)
    writeSet(tempData, 'newsData.json')
    # data = getStocks() + getNews() + getWeather()
    # pprint(data)
    #sendEmail(data)

main()
