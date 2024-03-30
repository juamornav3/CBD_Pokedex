
from django.contrib import admin
from django.urls import path
from pokecursor import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('populate/', views.populate),
    path('listAllCursor/', views.list_pokemons_cursor),
    path('listAll/', views.list_pokemons_without_cursor),
    path('populate_n/', views.populate_n),
    path('delete_all/', views.delete_all_pokemons),
    path('pageAllCursor/', views.list_paginated_pokemons_cursor),
    path('pageAll/', views.list_paginated_pokemons_without_cursor),
]
