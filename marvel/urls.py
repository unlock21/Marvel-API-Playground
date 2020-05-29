from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/marvel/characters', views.characters, name="characters"),
    # path('api/marvel/character/search', views.characterSearch, name="characterSearch"),
    path('api/marvel/comics', views.comics, name="comics"),
    # path('api/marvel/comics/search', views.comicsSearch, name="comicsSearch"),
]