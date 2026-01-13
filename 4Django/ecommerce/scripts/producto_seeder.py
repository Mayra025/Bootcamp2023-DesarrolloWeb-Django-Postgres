import csv
from store.models import Producto, Categoria

def seed_productos():
    Producto.objects.all().delete()    
    
    with open('data/productos.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        
        for item in csv_dict_reader:
            producto = Producto(nombre=item['nombre'],
                                descripcion=item['descripcion'],
                                precio=item['precio'],
                                imagen= 'productos/' + item['imagen'],
                                activo=(True if item['esta_activo']=='VERDADERO' else False)
                                )
            producto.save()
            categoria = Categoria.objects.get(slug=item['slug_categoria'])
            producto.categorias.add(categoria)
            producto.save()
            print(f'Producto creado: {producto}')
            
def run():
    seed_productos()
        