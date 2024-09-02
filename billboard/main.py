from billboard import Billboard
from song_player import SongPlayer


date = input("Insert date (yyyy-mm-dd):")
year = date.split("-")[0]

songs_data = Billboard.get_top_100(date)

player = SongPlayer()
playlist = player.create_playlist(date)

if playlist is not None:
    song_urls = [url for url in (player.get_song_url(name, year) for name in songs_data) if url is not None]
    player.add_to_playlist(playlist, song_urls)
    print("Songs added")
