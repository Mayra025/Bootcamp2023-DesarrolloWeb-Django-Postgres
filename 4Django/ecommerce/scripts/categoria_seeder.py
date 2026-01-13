import csv
from store.models import Categoria

def seed_categorias():
    Categoria.objects.all().delete()
    
    with open('data/categorias.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        for item in csv_dict_reader:
            categoria = Categoria(nombre=item['nombre'], slug=item['slug'])
            categoria.save()
            print(f'Categoria creada: {categoria}')
        

def run():
    seed_categorias()