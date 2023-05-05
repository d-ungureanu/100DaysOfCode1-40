import requests
import datetime as dt
import config
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
price_variation = ""
news_list = []
send_sms = False

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


def is_different(price1, price2):
    global price_variation
    global send_sms
    diff_percentage = round((price2 - price1) * 100 / price2, 2)
    print("% difference: ", diff_percentage)  # delete
    if abs(diff_percentage) > 5:
        get_three_headlines("Tesla Inc.")
        print(news_list)  # delete
        send_sms = True
        if diff_percentage > 0:
            price_variation += f"TSLA: 🔺{diff_percentage}%"
            print("Variation: ", price_variation)  # delete
        else:
            price_variation += f"TSLA: 🔻{diff_percentage}%"
            print("Variation: ", price_variation)  # delete
    else:
        print("No dif > or < than 5%")


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


def send_message(newslist: list):
    client = Client(account_sid, auth_token)
    for index, entry in enumerate(newslist):
        message = client.messages.create(
            body=f"{price_variation}" + "\n" + f"Headline: {entry['title']}" + "\n" + f"Brief: {entry['text']}",
            from_="+16813076724",
            to="+447455414104"
        )
        print(f"message {index + 1} status: {message.status}")


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

print(send_sms)  # delete
if send_sms:
    send_message(news_list)

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
