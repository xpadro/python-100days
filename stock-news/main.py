import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


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


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def main():
    stock_list = get_stock()

    yesterday_closing_price = float(stock_list[0]["4. close"])
    day_before_closing_price = float(stock_list[1]["4. close"])
    positive_difference = abs(yesterday_closing_price - day_before_closing_price)
    diff_percentage = (positive_difference / yesterday_closing_price) * 100

    if diff_percentage > 5:
        first_3_articles = get_top_articles()
        print(first_3_articles)


main()
