import json
import boto3 
from datetime import datetime
from io import StringIO
import pandas as pd

def album(data):
    album_list = []
    for album in data['items']: 
        album_id = album['track']['album']['id']
        album_name = album['track']['album']['name']
        album_release_date = album['track']['album']['release_date']
        album_total_tracks = album['track']['album']['total_tracks']
        album_url = album['track']['album']['external_urls']['spotify']
        album_dict = {'album_id':album_id,'name':album_name,'release_date':album_release_date,'total_tracks':album_total_tracks
                    ,'url':album_url}
        album_list.append(album_dict)

    album_data = pd.DataFrame.from_dict(album_list)
    album_data['release_date'] = pd.to_datetime(album_data['release_date'])
    album_data.drop_duplicates(subset = 'album_id',inplace=True)
    return album_data
    
def artist(data):
    artist_list = []
    for artist_l1 in data['items']:
        for key,value in artist_l1.items():
            if key == "track":
                for artist in value['artists']:
                    artist_dict = {'artist_id':artist['id'],'artist_name':artist['name'],'external_url':artist['href']}
                    artist_list.append(artist_dict)

    artist_data = pd.DataFrame.from_dict(artist_list)