from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/news"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
article_spans = soup.find_all(name="span", class_="titleline")

for article_span in article_spans:
    article = article_span.find('a')
    if article is not None:
        print(f"{article.getText()} - {article.get('href')}")
