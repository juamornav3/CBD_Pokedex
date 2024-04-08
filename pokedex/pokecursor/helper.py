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

def get_pokemon_by_name_without_cursor(pokemon_name):
    start_time = time.time()
    results = Pokemon.objects.filter(name__icontains=pokemon_name)
    time_query = time.time() - start_time
    return results, round(time_query, 4)