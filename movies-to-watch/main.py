import requests
import re
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Movies are shown in this format: 1) Movie name
# However, movie number 12, is incorrectly formatted as 12: Movie name
NUM_AND_TITLE = r'\)|: '


def format_movie_name(tag):
    movie_name_and_index = re.split(NUM_AND_TITLE, tag.getText())
    num = movie_name_and_index[0]
    name = movie_name_and_index[1].strip()
    return f"{num}) {name}"


response = requests.get(URL)

soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
movies = [format_movie_name(tag) for tag in reversed(soup.find_all(name="h3", class_="title"))]

with open('movies.txt', 'w', encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
