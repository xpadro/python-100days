from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
price_raw = soup.find(name="span", class_="priceToPay").getText()
price = float(price_raw.split("$")[1])
print(price)
