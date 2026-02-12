import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()


#######web  scraping
#date=functions.date_format()
#print(type(date),date)
def creating_playlist(date):
    ###web scrapping
    url=f'https://www.billboard.com/charts/hot-100/{date}'
    response=requests.get(url)
    response.raise_for_status()
    html_site=response.text
    #print(html_site)
    soup=BeautifulSoup(html_site,'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    #print(song_names)

    #######spotify

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://localhost:5000/callback",
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            show_dialog=True,
            cache_path=os.getenv("CACHE_PATH"),
            username=os.getenv("USERNAME"),
        )
    )
    user_id = sp.current_user()["id"]
    song_uris = [] #we add all the songs that we found on spotify
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")


    playlist = sp.user_playlist_create(user=user_id, name=f"{date} most listened 100", public=False)
    # print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)