import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URL")


def get_song_names(html: BeautifulSoup) -> list:
    return [item.getText().strip() for item in html.select('li ul li h3')]


def get_songs(song_date: str) -> list:
    top_songs = []

    response = requests.get(f"{BILLBOARD_BASE_URL}/{song_date}")
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    song_names = get_song_names(soup)

    for i in range(len(song_names)):
        top_songs.append(song_names[i])

    return top_songs


def auth_to_spotify() -> Spotify:
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        cache_path="token.txt"
    ))


def get_song_url(spotify, song, year):
    try:
        result = spotify.search(q=f"track:{song} year:{year}", type="track", limit=1)
        return result['tracks']['items'][0]['uri']
    except IndexError:
        print(f"Ignoring song. '{song}' does not exist")


date = input("Insert date (yyyy-mm-dd):")
year = date.split("-")[0]

songs_data = get_songs(date)

sp = auth_to_spotify()
songs = []

for song_data in songs_data:
    song_url = get_song_url(sp, song_data, year)
    songs.append(song_url)

print(songs)
