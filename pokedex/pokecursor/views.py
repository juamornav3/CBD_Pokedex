from django.shortcuts import render
from django.conf import settings
from pokecursor.models import Pokemon
from pokecursor.populate_db import populate_database , populate_database_n, delete_all_pokemons_db
from pokecursor.cursor_helper import *
from pokecursor.helper import *
from memory_profiler import memory_usage
from pokecursor.forms import IntegerForm, FilterForm
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html',{'STATIC_URL':settings.STATIC_URL})

#OPERATIONS FOR DATABASE

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

def delete_all_pokemons(request):
    num_pokemons = delete_all_pokemons_db()
    return render(request, 'populate_db.html', {'titulo':'FIN DE ELIMINACION DE LA BD','num_pokemons': num_pokemons,
                                                'STATIC_URL':settings.STATIC_URL})

#OPERATIONS WITH CURSOR

def list_pokemons_cursor(request):
    memory_usage_result = memory_usage((list_all_pokemon_with_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons,time_query = list_all_pokemon_with_cursor()
    return render(request, 'list_pokemons_cursor.html', {'titulo':'LISTADO DE POKEMONS CON CURSORES','pokemons':pokemons,
                                                         'time_query':time_query,'max_memory_usage':max_memory_usage,
                                                         'STATIC_URL':settings.STATIC_URL})

def list_paginated_pokemons_cursor(request):
    page = int(request.GET.get('page', 1))
    memory_usage_result = memory_usage((paginate_pokemon_with_cursor, (page,)))
    max_memory_usage = max(memory_usage_result)
    has_previous = has_previous_page(page)
    print(has_previous) 
    has_next = has_next_page(page)
    pages = num_pages()
    pokemons,time_query = paginate_pokemon_with_cursor(page)
    return render(request, 'page_pokemons_cursor.html', {'titulo':'LISTADO DE POKEMONS CON CURSORES PAGINADO','pokemons':pokemons,
                                                         'time_query':time_query,'max_memory_usage':max_memory_usage,'page':page,
                                                         'has_previous':has_previous,'has_next':has_next,'pages':pages,
                                                         'STATIC_URL':settings.STATIC_URL})

def filter_pokemons_cursor(request):
    form = FilterForm()
    memory_usage_result = memory_usage((list_all_pokemon_with_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons,time_query = list_all_pokemon_with_cursor()
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name_filter']
            type1 = form.cleaned_data['type1_filter']
            type2 = form.cleaned_data['type2_filter']
            hp = form.cleaned_data['hp_filter']
            attack = form.cleaned_data['attack_filter']
            defense = form.cleaned_data['defense_filter']
            sp_atk = form.cleaned_data['sp_atk_filter']
            sp_def = form.cleaned_data['sp_def_filter']
            speed = form.cleaned_data['speed_filter']
            generation = form.cleaned_data['gen_filter']
            legendary = form.cleaned_data['legendary_filter']
            memory_usage_result = memory_usage((filter_pokemon_with_cursor, (name,type1,type2,hp,attack,defense,sp_atk,sp_def,speed,generation,legendary)))
            max_memory_usage = max(memory_usage_result)
            pokemons, time_query = filter_pokemon_with_cursor(name,type1,type2,hp,attack,defense,sp_atk,sp_def,speed,generation,legendary)
    return render(request, 'filter_pokemons_cursor.html', {'titulo':'FILTRADO DE POKEMONS CON CURSORES','pokemons':pokemons,
                                                  'time_query':time_query,'max_memory_usage':max_memory_usage, 'form':form,'STATIC_URL':settings.STATIC_URL})
    

#OPERATIONS WITHOUT CURSOR

def list_pokemons_without_cursor(request):
    memory_usage_result = memory_usage((list_all_pokemon_without_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons, time_query= list_all_pokemon_without_cursor()
    num_pokemons = len(pokemons)
    return render(request, 'list_pokemons.html', {'titulo':'LISTADO DE POKEMONS SIN CURSORES','pokemons':pokemons,
                                                  'time_query':time_query,'max_memory_usage':max_memory_usage,
                                                    'num_pokemons':num_pokemons,'STATIC_URL':settings.STATIC_URL})

def list_paginated_pokemons_without_cursor(request):
    pokemons, time_query = list_all_pokemon_without_cursor()
    paginator = Paginator(pokemons, 10)
    page = int(request.GET.get('page',1))
    pokemons = paginator.get_page(page)
    current_page = page
    pages = range(1, pokemons.paginator.num_pages+1)
    memory_usage_result = memory_usage((list_all_pokemon_without_cursor,))
    max_memory_usage = max(memory_usage_result)
    return render(request, 'page_pokemons.html', {'titulo':'LISTADO DE POKEMONS SIN CURSORES PAGINADO','pokemons':pokemons,
                                                  'time_query':time_query,'current_page':current_page,'pages':pages,
                                                    'max_memory_usage':max_memory_usage,'STATIC_URL':settings.STATIC_URL})
                                        
def filter_pokemons_without_cusor(request):
    form = FilterForm()
    memory_usage_result = memory_usage((list_all_pokemon_without_cursor,))
    max_memory_usage = max(memory_usage_result)
    pokemons, time_query= list_all_pokemon_without_cursor()
    num_pokemons = len(pokemons)
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name_filter']
            type1 = form.cleaned_data['type1_filter']
            type2 = form.cleaned_data['type2_filter']
            hp = form.cleaned_data['hp_filter']
            attack = form.cleaned_data['attack_filter']
            defense = form.cleaned_data['defense_filter']
            sp_atk = form.cleaned_data['sp_atk_filter']
            sp_def = form.cleaned_data['sp_def_filter']
            speed = form.cleaned_data['speed_filter']
            generation = form.cleaned_data['gen_filter']
            legendary = form.cleaned_data['legendary_filter']
            memory_usage_result = memory_usage((filter_pokemon_without_cursor, (name,type1,type2,hp,attack,defense,sp_atk,sp_def,speed,generation,legendary)))
            max_memory_usage = max(memory_usage_result)
            pokemons, time_query = filter_pokemon_without_cursor(name, type1, type2, hp, attack, defense,sp_atk,sp_def,speed, generation, legendary)
            num_pokemons = len(pokemons)

    return render(request, 'filter_pokemons.html', {'titulo':'FILTRADO DE POKEMONS SIN CURSORES','pokemons':pokemons,
                                                  'time_query':time_query,'form':form,'num_pokemons':num_pokemons,'max_memory_usage':max_memory_usage,'STATIC_URL':settings.STATIC_URL})        
