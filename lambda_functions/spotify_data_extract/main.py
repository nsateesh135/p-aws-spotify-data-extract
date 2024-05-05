import json
import os 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import configuration as config
import boto3
from datetime import datetime


SPOTIFY_APP_NAME = config.SPOTIFY_APP_NAME
client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
spotify_top_50_songs = f"https://open.spotify.com/playlist/{config.SPOTIFY_TOP_50_SONGS_URL}?si=1333723a6eff4b7f" 

def authenticate_spotify_api(client_id,client_secret):
    """
    This function is used to authenticate sptify API
    Args : 
    client_id : Obtained from the Spotify App 
    client_secret : Obtained from the Spotify App 
    Output:
    sp : spotify client used to interact with the API
    """
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp
    except Exception as e :
        print(f"{SPOTIFY_APP_NAME} : has resulted in the following error {e}")
        
