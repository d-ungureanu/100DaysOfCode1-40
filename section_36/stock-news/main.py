import requests
import datetime as dt
import config

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
price_variation = ""
news_list = []
send_sms = False


def is_different(price1, price2):
    global price_variation
    global send_sms
    diff_percentage = round((price2 - price1) * 100 / price2, 2)
    print(diff_percentage)
    if abs(diff_percentage > 5):
        get_three_headlines("Tesla Inc.")
        send_sms = True
        if diff_percentage > 0:
            price_variation += f"TSLA: 🔺{diff_percentage}%"
        else:
            price_variation += f"TSLA: 🔻{diff_percentage}%"


def get_three_headlines(news_subject):
    start_date = f"{dt.datetime.now() - dt.timedelta(30)}"
    news_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": news_subject,
        "from": start_date,
        "sortBy": "publishedAt",
        "language": "en",
        "searchIn": "title",
        "apiKey": config.news_apiKey
    }

    news_raw_data = requests.get(url=news_url, params=news_parameters)
    news_data = news_raw_data.json()
    top_news = news_data["articles"][:3]
    for news_entry in top_news:
        title, text = news_entry["title"].split(": ")
        news_list.append({"title": title, "text": text})


stock_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "interval": "5min",
    "apikey": config.stock_apiKey
}
stock_raw_data = requests.get(url=stock_url, params=stock_parameters)
stock_data = stock_raw_data.json()
daily_data = stock_data["Time Series (Daily)"]
all_dates_list = list(daily_data.keys())
last_2_days = all_dates_list[:2]

yesterday_data = daily_data[last_2_days[0]]
yesterday_price = float(yesterday_data["4. close"])

two_days_before_data = daily_data[last_2_days[1]]
two_days_before_price = float(two_days_before_data["4. close"])
is_different(yesterday_price, two_days_before_price)
print(price_variation)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if send_sms:
    print("wohoo")



# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
