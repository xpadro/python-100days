import requests
from bs4 import BeautifulSoup

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"


def get_song_names(html: BeautifulSoup) -> list:
    return [item.getText().strip() for item in html.select('li ul li h3')]


def get_song_artists(html: BeautifulSoup) -> list:
    return [item.getText().strip() for item in html.select('li ul li span.a-no-trucate')]


def get_songs():
    top_songs = []

    date = input("Insert date (yyyy-mm-dd):")
    response = requests.get(f"{BILLBOARD_BASE_URL}/{date}")

    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    songs = get_song_names(soup)
    artists = get_song_artists(soup)

    for i in range(len(songs)):
        top_songs.append(f"{songs[i]} {artists[i]}")

    return top_songs


songs_data = get_songs()
print(songs_data)
