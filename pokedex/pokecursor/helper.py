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

def filter_pokemon_without_cursor(pokemon_name, type1, type2,hp, attack, defense, sp_attack ,sp_def ,speed , generation, legendary):
    start_time = time.time()
    results = Pokemon.objects.all()
    if pokemon_name:
        results = results.filter(name__icontains=pokemon_name)
    if type1:
        results = results.filter(type_1=type1)
    if type2:
        results = results.filter(type_2=type2)
    if hp:
        results = results.filter(hp__lte=hp)
    if attack:
        results = results.filter(attack__lte=attack)
    if defense:
        results = results.filter(defense__lte=defense)
    if sp_attack:
        results = results.filter(sp_atk__lte=sp_attack)
    if sp_def:
        results = results.filter(sp_def__lte=sp_def)
    if speed:
        results = results.filter(speed__lte=speed)
    if generation:
        results = results.filter(generation=generation)
    list_results = list(results.values())
    if legendary:
            list_results = [res for res in results if res.legendary is True]
    else:
            list_results = [res for res in results if res.legendary is False]

    time_query = time.time() - start_time
    return list_results, round(time_query, 4)