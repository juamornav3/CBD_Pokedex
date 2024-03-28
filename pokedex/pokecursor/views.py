from django.shortcuts import render
from django.conf import settings
from pokecursor.models import Pokemon
from pokecursor.populate_db import populate_database , populate_database_n
from pokecursor.cursor_helper import *
from pokecursor.helper import *
from memory_profiler import memory_usage
from pokecursor.forms import IntegerForm


def index(request):
    return render(request, 'index.html',{'STATIC_URL':settings.STATIC_URL})

def populate(request):
    num_pokemons = populate_database()
    return render(request, 'populate_db.html', {'titulo':'FIN DE CARGA DE LA BD','num_pokemons': num_pokemons,
                                                'STATIC_URL':settings.STATIC_URL})

def populate_n(request):
    num_times = 0
    form = IntegerForm()
    if request.method == 'POST':
        form = IntegerForm(request.POST)
        if form.is_valid():
            num_times = form.cleaned_data['num_times']
    num_pokemons = populate_database_n(num_times)
    return render(request, 'populate_db_n.html', {'titulo':'FIN DE CARGA DE LA BD','num_pokemons': num_pokemons,
                                                'STATIC_URL':settings.STATIC_URL, 'form':form})

def list_pokemons_cursor(request):
    memory_usage_result = memory_usage((list_all_pokemon_with_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons,time_query = list_all_pokemon_with_cursor()
    return render(request, 'list_pokemons_cursor.html', {'titulo':'Listado de pokemons con cursores','pokemons':pokemons,
                                                         'time_query':time_query,'max_memory_usage':max_memory_usage,
                                                         'STATIC_URL':settings.STATIC_URL})


def list_pokemons_without_cursor(request):
    memory_usage_result = memory_usage((list_all_pokemon_without_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons, time_query= list_all_pokemon_without_cursor()
    num_pokemons = len(pokemons)
    return render(request, 'list_pokemons.html', {'titulo':'Listado de pokemons sin cursores','pokemons':pokemons,
                                                  'time_query':time_query,'max_memory_usage':max_memory_usage,
                                                    'num_pokemons':num_pokemons,'STATIC_URL':settings.STATIC_URL})

