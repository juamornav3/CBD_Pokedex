import time
from django.http import JsonResponse
from pokecursor.models import Pokemon
from django.db import connection
from pymongo import MongoClient

def list_all_pokemon_with_cursor():
    start_time = time.time()
    client = MongoClient('localhost', 27017)
    db = client['pokemon_db']
    collection = db['pokecursor_pokemon']
    cursor = collection.find({})
    time_query = time.time() - start_time
    return cursor, round(time_query, 4)

def paginate_pokemon_with_cursor(page, limit):
    start_time = time.time()
    client = MongoClient('localhost', 27017)
    db = client['pokemon_db']
    collection = db['pokecursor_pokemon']
    cursor = collection.find({}).skip((page - 1) * limit).limit(limit)
    time_query = time.time() - start_time
    return cursor, round(time_query, 4)
