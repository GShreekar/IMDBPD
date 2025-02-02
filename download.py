import requests
from imdb import IMDb
from imdb.Movie import Movie
from requests.exceptions import RequestException

def download(movie_id):
    try:
        id = IMDb()
        try:
            movie = id.get_movie(movie_id)
            if not movie:
                raise ValueError("Movie not found")
            
            title = movie.get('title')
            poster_url = movie.get('full-size cover url')
            
            if not poster_url:
                raise ValueError("No poster available for this movie")
            
            try:
                poster = requests.get(poster_url)
                poster.raise_for_status()
            except RequestException as e:
                raise ValueError(f"Failed to download poster: {e}")
            
            try:
                with open(f'{title}.jpg', 'wb') as f:
                    f.write(poster.content)
                print(f'{title} poster downloaded')
            except IOError as e:
                raise ValueError(f"Failed to save poster: {e}")
                
        except Exception as e:
            raise ValueError(f"Error fetching movie data: {e}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def main():
    while True:
        movie_id = input('Enter IMDB movie ID (or q to quit): ')
        if movie_id.lower() == 'q':
            break
        if not movie_id.strip().isdigit():
            print("Error: Please enter a valid numeric ID")
            continue
        download(movie_id)

if __name__ == '__main__':
    main()