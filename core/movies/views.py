from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Movie, Review
from django.contrib.auth.forms import UserCreationForm
from .utils import get_movies_from_api, get_movie_details_from_api
from .forms import ReviewForm, UserRegistrationForm 
import requests
from django.http import HttpResponseForbidden
from dotenv import load_dotenv
import os

# Carregando variáveis de ambiente do arquivo .env
load_dotenv()

# Obtendo a chave da API
api_key = os.environ.get('TMDB_API_KEY')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def movie_list(request):
    query = request.GET.get('query')
    movies = get_movies_from_api(query)
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_movie_details_from_api(movie_id)
    trailer_url = get_trailer(movie_id)
    reviews = Review.objects.filter(movie_id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'trailer_url': trailer_url})

def get_movie_details_from_api(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR'
    response = requests.get(url)
    movie = response.json()
    movie['id'] = movie_id  # Certifique-se de que o movie_id está presente
    return movie

def get_trailer(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=pt-BR'
    response = requests.get(url)
    videos = response.json().get('results', [])
    for video in videos:
        if video['site'] == 'YouTube' and video['type'] == 'Trailer':
            return f'https://www.youtube.com/embed/{video["key"]}'
    return None

@login_required
def add_review(request, movie_id):
    movie = get_movie_details_from_api(movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie_id = movie_id  
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user and not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=review.movie_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user and not request.user.is_staff:
        return HttpResponseForbidden()
    movie_id = review.movie_id
    review.delete()
    return redirect('movie_detail', movie_id=movie_id)
