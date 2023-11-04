import requests
from pprint import pprint
from emailServer import sendEmail
import datetime


newsAPIKey = '64f44e13e28b4068ab0bbae7d3c074a7'
country = 'us'
r = requests.get('https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country, newsAPIKey))
data = r.json()
my_list = []
body = "\n"


for i in range(0,3):
    my_list.append({'title' : data['articles'][i]['title'], 'url' : data['articles'][i]['url']})
    # print(my_list[i].title)
    body += "Title: {title}\nURL: {url}\n\n".format(title = my_list[i]['title'], url = my_list[i]['url'])
    # body = my_list[i]['title']

# print(body)
sendEmail(body)

vantageAPIKey = 'JFS0LR00E05LA2QI'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={}'.format(vantageAPIKey)
r = requests.get(url)
data = r.json()

# e = datetime.datetime.now()-datetime.timedelta(1)
# time_series = data["Time Series (5min)"][e.strftime("%Y-%m-%d") + " 09:30:00"]

# pprint(time_series)