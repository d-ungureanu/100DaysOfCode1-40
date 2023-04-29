import config
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = config.stock_apiKey
NEWS_API_KEY = config.news_apiKey

# Get yesterday's stock price
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_closing_price = float(day_before_yesterday_data["4. close"])

price_difference = abs(yesterday_closing_price - day_before_closing_price)

difference_percentage = round(price_difference / yesterday_closing_price * 100, 2)

if difference_percentage > 2: #change to 5
    news_params ={
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "searchIn": "title",
        "apiKey": config.news_apiKey
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_articles = news_response.json()["articles"]
    top_news = news_articles[:3]

    print(top_news)