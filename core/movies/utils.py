import requests

API_KEY = 'YOUR_TMDB_API_KEY'  # Substitua pelo seu API Key do TMDb

def get_movies_from_api(query=None):
    if query:
        url = f'https://api.themoviedb.org/3/search/movie?api_key=17bab99ff00134f6961640d0edf32d8e&language=en-US&query={query}'
    else:
        url = f'https://api.themoviedb.org/3/movie/popular?api_key=17bab99ff00134f6961640d0edf32d8e&language=en-US&page=1'
    response = requests.get(url)
    data = response.json()
    return data['results']

def get_movie_details_from_api(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=17bab99ff00134f6961640d0edf32d8e&language=en-US'
    response = requests.get(url)
    return response.json()
