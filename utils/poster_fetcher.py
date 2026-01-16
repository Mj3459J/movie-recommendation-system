import requests
import os

API_KEY=os.getenv("TMDB_API_KEY")
BASE_URL="https://api.themoviedb.org/3"

def fetch_poster(movie_id):
    url=f"{BASE_URL}/movie/{movie_id}"
    params={
        "api_key":API_KEY,
        "language":"en-US"
    }
    response=requests.get(url,params=params)
    data=response.json()
    poster_path=data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    # return "https://image.tmdb.org/t/p/w500" + poster_path