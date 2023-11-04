# Information Centralization Project

The Information Centralization Project is designed to provide users with a single text message in the morning that contains a variety of relevant information, including Stock Prices, Daily News, Local Weather, and daily commute times. With proper configuration, you can streamline the process of accessing these important details.

## Proper Configurations

To make this project work effectively, you need to modify the `.env` file with your own information. Here is a sample configuration that you can use as a template:

```env
STOCK_API = 'your_stock_api_key'
WEATHER_API = 'your_weather_api_key'
NEWS_API = 'your_news_api_key'
PHONE_NUMBERS = ["123456789@vzwpix.com", "123456789@mms.att.net"]
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PWD = "your_email_password"

