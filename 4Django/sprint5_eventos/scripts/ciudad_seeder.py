import csv
from event.models import Ciudad

def seed_ciudades():
    Ciudad.objects.all().delete()
    
    with open('data/ciudades.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            ciudad = Ciudad(nombre=item['nombre'], slug=item['slug'])
            ciudad.save()
            print(f'Ciudad creada: {ciudad}')
        

def run():
    seed_ciudades()