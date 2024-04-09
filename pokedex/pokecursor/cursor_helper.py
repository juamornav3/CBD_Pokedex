import time
from django.http import JsonResponse
from pokecursor.models import Pokemon
from django.db import connection
from pymongo import MongoClient

def connect_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client['pokemon_db']
    collection = db['pokecursor_pokemon']
    return collection

def list_all_pokemon_with_cursor():
    start_time = time.time()
    collection = connect_to_mongo()
    cursor = collection.find({})
    time_query = time.time() - start_time
    return cursor, round(time_query, 4)

def paginate_pokemon_with_cursor(page, limit = 10):
    start_time = time.time()
    collection = connect_to_mongo()
    cursor = collection.find({}).skip((page - 1) * limit).limit(limit)
    time_query = time.time() - start_time
    return cursor, round(time_query, 4)

def num_pages(limit = 10):
    collection = connect_to_mongo()
    num_pokemon = collection.count_documents({})
    return num_pokemon // limit + 1 if num_pokemon % limit != 0 else num_pokemon // limit

def has_next_page(page, limit=10):
    collection = connect_to_mongo()
    num_pokemon = collection.count_documents({})
    return (page * limit) < num_pokemon

def has_previous_page(page):
    return page > 1

def get_pokemon_by_name_with_cursor(name):
    start_time = time.time()
    collection = connect_to_mongo()
    cursor = collection.find({"name": {"$regex": name, "$options": "i"}})
    time_query = time.time() - start_time
    return cursor, round(time_query, 4)

def get_type_with_cursor():
    collection = connect_to_mongo()
    cursor = collection.find({}, {'type_1': 1})
    types = {doc['type_1'] for doc in cursor}
    type_choices = [(type, type.capitalize()) for type in types]   
    type_choices.insert(0, ('', ''))
    return type_choices


