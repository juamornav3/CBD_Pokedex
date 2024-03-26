from django.shortcuts import render
from django.conf import settings
from pokecursor.models import Pokemon
from pokecursor.populate_db import populate_database


def index(request):
    return render(request, 'index.html',{'STATIC_URL':settings.STATIC_URL})

def populate(request):
    num_pokemons = populate_database()
    return render(request, 'populate_db.html', {'titulo':'FIN DE CARGA DE LA BD','num_pokemons': num_pokemons,'STATIC_URL':settings.STATIC_URL})