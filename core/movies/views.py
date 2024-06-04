from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Movie, Review
from django.contrib.auth.forms import UserCreationForm
from .utils import get_movies_from_api, get_movie_details_from_api
from .forms import ReviewForm, UserRegistrationForm 
import requests



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
    return render(request, 'movie_detail.html', {'movie': movie})

def get_movie_details_from_api(movie_id):
    api_key = 'YOUR_TMDB_API_KEY' 
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=17bab99ff00134f6961640d0edf32d8e&language=en-US'
    response = requests.get(url)
    return response.json()
    

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
def edit_review(request, movie_id):
    review = get_object_or_404(Review, movie_id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=review.movie.movie_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form})

@login_required
def delete_review(request, movie_id):
    review = get_object_or_404(Review, movie_id=movie_id)
    movie_movie_id = review.movie.movie_id
    review.delete()
    return redirect('movie_detail', movie_id=movie_movie_id)
