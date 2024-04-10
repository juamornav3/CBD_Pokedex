import time
from django.http import JsonResponse
from pokecursor.models import Pokemon
from pymongo import MongoClient



def list_all_pokemon_without_cursor():
    start_time = time.time()
    client = MongoClient('localhost', 27017)
    db = client['pokemon_db']
    collection = db['pokecursor_pokemon']
    results = list(collection.find({}))
    time_query = time.time() - start_time
    return results, round(time_query, 4)

from django.db.models import Q

def filter_pokemon_without_cursor(pokemon_name, type1, type2, generation, legendary):
    start_time = time.time()
    results = Pokemon.objects.all()
    if pokemon_name:
        results = results.filter(name__icontains=pokemon_name)
    if type1:
        results = results.filter(type_1=type1)
    if type2:
        results = results.filter(type_2=type2)
    if generation:
        results = results.filter(generation=generation)
    list_results = list(results.values())
    if legendary:
            print("Entro")
            list_results = [res for res in results if res.legendary is True]
    else:
            list_results = [res for res in results if res.legendary is False]

    time_query = time.time() - start_time
    return list_results, round(time_query, 4)