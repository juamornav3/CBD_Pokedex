import csv
from pokecursor.models import Pokemon  

def populate_database():
    Pokemon.objects.all().delete()
    with open('data\\pokemon.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Procesar cada fila y guardarla en la base de datos
            pokemon = Pokemon(
                name=row['Name'],
                type_1=row['Type 1'],
                type_2=row['Type 2'],
                total=int(row['Total']),
                hp=int(row['HP']),
                attack=int(row['Attack']),
                defense=int(row['Defense']),
                sp_atk=int(row['Sp. Atk']),
                sp_def=int(row['Sp. Def']),
                speed=int(row['Speed']),
                generation=int(row['Generation']),
                legendary=row['Legendary'].lower() == 'true'
            )
            pokemon.save()
        num_pokemons = Pokemon.objects.count()
        return num_pokemons

