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
        path('movie/<int:movie_id>/vote',
            views.CreateVote.as_view(),
            name='CreateVote'),
        path('movie/<int:movie_id>/vote/<int:pk>',
            views.UpdateVote.as_view(),
            name='UpdateVote'),
        path('movie/<int:movie_id>/image/upload',
            views.MovieImageUpload.as_view(),
            name='MovieImageUpload'),
        ]
        
