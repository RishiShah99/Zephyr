import spotipy
from spotipy.oauth2 import SpotifyOAuth
from api_keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

scope = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))

def play_song(song_name):
    results = sp.search(q=song_name, limit=1, type='track')
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        return f"Playing {song_name}"
    else:
        return "Song not found."

def pause_song():
    sp.pause_playback()
    return "Playback paused."

def skip_song():
    sp.next_track()
    return "Skipped to the next song."

def get_current_song():
    current = sp.current_playback()
    if current and current['is_playing']:
        song = current['item']['name']
        artists = ', '.join([artist['name'] for artist in current['item']['artists']])
        return f"Currently playing {song} by {artists}."
    else:
        return "No song is currently playing."
