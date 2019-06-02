from django.views.generic import (ListView, DetailView)
from moviesApp.models import myMovie

class MovieList(ListView):
    model = myMovie

class MovieDetail(DetailView):
    queryset = (
            myMovie.objects.all_with_related_persons()
            )



