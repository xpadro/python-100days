from billboard import Billboard
from song_player import SongPlayer


date = input("Insert date (yyyy-mm-dd):")
year = date.split("-")[0]

songs_data = Billboard.get_top_100(date)

player = SongPlayer()
player.create_playlist(date)

songs = []

for song_data in songs_data:
    song_url = player.get_song_url(song_data, year)
    songs.append(song_url)

print(songs)
