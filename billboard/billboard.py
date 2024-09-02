import requests
from bs4 import BeautifulSoup


BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"


class Billboard:

    @staticmethod
    def get_song_names(html: BeautifulSoup) -> list:
        return [item.getText().strip() for item in html.select('li ul li h3')]

    @staticmethod
    def get_top_100(song_date: str) -> list:
        top_songs = []

        response = requests.get(f"{BILLBOARD_BASE_URL}/{song_date}")
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        song_names = Billboard.get_song_names(soup)

        for i in range(len(song_names)):
            top_songs.append(song_names[i])

        return top_songs
