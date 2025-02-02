# A simple script to download movie posters from IMDB
import requests
import os
from imdb import IMDb

def download(movie_id):
    id = IMDb()
    movie = id.get_movie(movie_id)
    title = movie['title']
    poster_url = movie['full-size cover url']
    poster = requests.get(poster_url)
    poster.raise_for_status()
    with open(f'{title}.jpg', 'wb') as f:
        f.write(poster.content)
    print(f'{title} poster downloaded')
    
def main():
    movie_id = input('Enter IMDB movie ID: ')
    download(movie_id)
    
if __name__ == '__main__':
    main()