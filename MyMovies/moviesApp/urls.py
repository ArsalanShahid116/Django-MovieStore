from django.urls import path 
from . import views

app_name = 'moviesApp'
urlpatterns = [
        path('myMovies',
            views.MovieList.as_view(),
            name='MovieList'),
        ]
