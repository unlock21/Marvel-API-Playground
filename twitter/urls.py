from django.urls import path

from . import views

urlpatterns = [
    path('tweets/', views.index, name='index'),
    path('search/', views.search, name='search'),
]