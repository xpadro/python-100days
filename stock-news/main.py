import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_VIRTUAL_PHONE = os.environ.get('TWILIO_VIRTUAL_PHONE')
TWILIO_TARGET_PHONE = os.environ.get('TWILIO_TARGET_PHONE')


def get_stock():
    """ Calls the stock API and returns the list of stock prices for Tesla

    :return: list of stock prices
    """
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.environ.get('STOCK_API_KEY')
    }

    response = requests.get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    time_series = response.json()["Time Series (Daily)"]
    return [value for (key, value) in time_series.items()]


def get_top_articles():
    """ Calls the news API and fetches COMPANY_NAME related articles

    :return: the first 3 articles for COMPANY_NAME
    """
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": os.environ.get('NEWS_API_KEY')
    }

    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()['articles'][:3]


def send_sms(message):
    """ Use Twilio API to send an SMS message to the specified phone

    :param message:
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)

    client.messages.create(
        body=message,
        from_=TWILIO_VIRTUAL_PHONE,
        to=TWILIO_TARGET_PHONE
    )


def main():
    stock_list = get_stock()

    yesterday_closing_price = float(stock_list[0]["4. close"])
    day_before_closing_price = float(stock_list[1]["4. close"])
    positive_difference = abs(yesterday_closing_price - day_before_closing_price)
    diff_percentage = (positive_difference / yesterday_closing_price) * 100

    if diff_percentage > 1:
        first_3_articles = get_top_articles()

        first_3_article_summaries = [(item['title'], item['description']) for item in first_3_articles]

        for summary in first_3_article_summaries:
            msg = f"Headline: {summary[0]}.\nBrief: {summary[1]}"
            send_sms(msg)


main()
