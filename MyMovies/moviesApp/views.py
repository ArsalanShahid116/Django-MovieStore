from django.views.generic import (ListView, DetailView)
from moviesApp.models import myMovie

class MovieList(ListView):
    model = myMovie

class MovieDetail(DetailView):
        model = myMovie


