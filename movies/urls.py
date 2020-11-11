from django.urls import path

from . import views


urlpatterns = [
   path("", views.MovieView.as_view(), name='movies'),
   path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail')
]
