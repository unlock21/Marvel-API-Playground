from django.urls import path
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/twitter/search/', views.search, name='search'),
]