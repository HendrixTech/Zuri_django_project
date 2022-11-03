from django.urls import path, URLPattern
from .views import SongList, SongDetail, ArtisteList, ArtisteDetail
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("song/<int:pk>/", SongDetail.as_view(), name="song_detail"),
    path("song/", SongList.as_view(), name="song_list"),
    path("artiste/<int:pk>", ArtisteDetail.as_view(), name="artiste_detail"),
    path("artiste/", ArtisteList.as_view(), name="artiste_list"),
]