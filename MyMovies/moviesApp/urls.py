from django.urls import path 
from . import views

app_name = 'moviesApp'
urlpatterns = [
        path('myMovies',
            views.MovieList.as_view(),
            name='MovieList'),
        path('myMovies/<int:pk>',
            views.MovieDetail.as_view(),
            name='MovieDetail'),
        ]
