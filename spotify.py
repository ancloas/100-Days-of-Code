import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from song_extraction import extract_top_100songs_by_date

load_dotenv()

def get_spotify_conn(scope=None):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp
def create_playlist(playlist_name, playlist_desc, conn=None):
    user_id= os.getenv('spotify_user_id')
    scope = "playlist-modify-private playlist-modify-public"
    if conn==None:
        conn=get_spotify_conn(scope)
    return conn.user_playlist_create(user=user_id, name=playlist_name, description=playlist_desc, public=False)['id']


def search_a_song(song_name, conn=None, year=None):
    
    if conn==None:
        conn=get_spotify_conn()   

    search_query= f'track:{song_name} year:{year}'

    results = conn.search(q=search_query, type='track', limit=1)
    try:
        track_uri= results['tracks']['items'][0]['uri']
    except:
        return None
    return track_uri

def add_songs_to_playlist(songnames, playlistid, conn=None, songs_year=None):
    scope = "playlist-modify-private playlist-modify-public"
    user_id= os.getenv('spotify_user_id')
    if conn==None:
        conn=get_spotify_conn()

    track_list=[] 
    for songname in songnames[:10]:    
        song = search_a_song(songname, year=songs_year)
        if song:
            track_list.append(song)

    conn.user_playlist_add_tracks(user_id, playlistid, track_list)

    


    
list_songs= extract_top_100songs_by_date(date='1999-02-09')
play_list_id= create_playlist('Top 10 songs on my birthday', 'top 10 songs on my birthday')
print(add_songs_to_playlist(list_songs, play_list_id, songs_year=1999))