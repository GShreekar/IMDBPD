# IMDb Poster Downloader

A simple Python script to download movie posters from IMDb.

## Requirements

```python
pip install requests imdbpy
```

## Usage

1. Run the script:
```python
python download.py
```

2. Enter the IMDb movie ID when prompted (the number in the movie's IMDb URL)
3. The poster will be downloaded as `[movie title].jpg` in the current directory

## Example
For the movie "The Matrix" (IMDb ID: 0133093):
```
Enter IMDB movie ID: 0133093
The Matrix poster downloaded
```

## References
- [IMDbPY Documentation](https://imdbpy.readthedocs.io/)
