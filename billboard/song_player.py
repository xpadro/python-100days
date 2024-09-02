import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URL")


class SongPlayer:

    def __init__(self):
        self.sp = SongPlayer._auth_to_spotify()
        self.user_id = self.sp.current_user()['id']

    @staticmethod
    def _auth_to_spotify() -> Spotify:
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="playlist-modify-private playlist-read-private",
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            cache_path="token.txt"
        ))

    def get_song_url(self, song, year):
        try:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track", limit=1)

            if len(result['tracks']['items']) == 0:
                # Some songs in billboard's specific year were published in a different year
                result = self.sp.search(q=f"track:{song}", type="track", limit=1)

            uri = result['tracks']['items'][0]['uri']
            print(f"Found uri for {song}")
            return uri
        except IndexError:
            print(f"Ignoring song. '{song}' does not exist")

    def _playlist_exists(self, name):
        pl_id = None

        playlists = self.sp.user_playlists(self.user_id)
        for playlist in playlists['items']:
            if name == playlist['name']:
                pl_id = playlist['id']
                break

        return pl_id

    def create_playlist(self, date):
        list_name = f"{date} Billboard 100"
        playlist_id = self._playlist_exists(list_name)

        if playlist_id is None:
            playlist = self.sp.user_playlist_create(
                user=self.user_id,
                name=list_name,
                public=False,
                description=f"Billboard top 100 songs in {date}")['id']

            print(f"playlist {playlist} created")
            return playlist
        else:
            print(f"Playlist {list_name} already exists")
            return None

    def add_to_playlist(self, pl_id, song_urls):
        self.sp.playlist_add_items(pl_id, song_urls)
