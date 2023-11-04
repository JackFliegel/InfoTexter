import requests
from pprint import pprint
from emailServer import sendEmail
import datetime
import json

def readSet(key):
    data = []
    # Reads in the pixel values 
    with open(f'./data/{key}', 'r') as file:
        for currentStep, line in enumerate(file, start=0):
            data.append([float(num) for num in line.strip().split()]) #adds the values all 784 pixels into array (indexed: 0 to 783)
    return data

def writeSet(data, str):    
    with open(f'./data/{str}', 'w') as file:
        for item in data:
            file.write(f'{item}\n')

def getNews():
    newsAPIKey = '64f44e13e28b4068ab0bbae7d3c074a7'
    country = 'us'
    r = requests.get('https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country, newsAPIKey))
    data = r.json()
    my_list = []
    body = "\n"

    for i in range(0,3):
        my_list.append({'title' : data['articles'][i]['title'], 'url' : data['articles'][i]['url']})
        body += "Title: {title}\nURL: {url}\n\n".format(title = my_list[i]['title'], url = my_list[i]['url'])

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
    data = getStocks() + getNews() + getWeather()
    pprint(data)
    #sendEmail(data)
    return 0

main()

