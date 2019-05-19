from django.shortcuts import render
from moviesApp.models import myMovie

class MovieList(ListView):
    model = myMovie
