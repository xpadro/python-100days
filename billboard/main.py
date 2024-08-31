import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URL")


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


def auth_to_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        cache_path="token.txt"
    ))

    result = sp.current_user()
    print(result)


songs_data = get_songs()
print(songs_data)

auth_to_spotify()
