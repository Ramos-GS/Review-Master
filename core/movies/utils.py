import requests
from .models import Movie
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('TMDB_API_KEY')

def get_movies_from_api(query=None):
    if query:
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=pt-BR&query={query}'
    else:
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=pt-BR&page=1'
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    
    # Salvar os filmes no banco de dados local
    for movie_data in movies:
        # Verificar se o filme já existe no banco de dados
        movie_id = movie_data['id']
        if not Movie.objects.filter(id=movie_id).exists():
            # Se o filme não existir, criar um novo registro no banco de dados
            movie = Movie.objects.create(
                id=movie_id,
                title=movie_data['title'],
                description=movie_data['overview']
            )
    
    return movies


def get_movie_details_from_api(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR'
    response = requests.get(url)
    return response.json()
