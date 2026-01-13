import csv
from event.models import Evento, Categoria, Ciudad
from datetime import datetime
from django.utils import timezone

def seed_eventos():
    Evento.objects.all().delete()    
    
    with open('data/eventos.csv') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')
        
        for item in csv_dict_reader:
            fecha_str = item['fecha']
            hora_str = item['hora']

    # Convertir la cadena de fecha y hora en un objeto datetime ingenuo
            fecha_hora_ingenua = datetime.strptime(fecha_str + ' ' + hora_str, '%Y-%m-%d %H:%M')

    # Convertir el objeto datetime ingenuo en un objeto datetime consciente de la zona horaria
            fecha_hora_consciente = timezone.make_aware(fecha_hora_ingenua, timezone.get_current_timezone())

            evento = Evento(nombre=item['nombre'],
                                descripcion=item['descripcion'],
                                precio=item['precio'],
                                imagen= 'eventos/' + item['imagen'],
                                estado=(True if item['esta_activo']=='VERDADERO' else False),
                                fecha=fecha_hora_ingenua,
                                hora=fecha_hora_consciente

                                )
            evento.save()
            categoria = Categoria.objects.get(slug=item['slug_categoria'])
            evento.categorias.add(categoria)
            ciudad = Ciudad.objects.get(slug=item['slug_ciudad'])
            evento.ciudades.add(ciudad)
            evento.save()
            print(f'Evento creado: {evento}')
            
def run():
    seed_eventos()
        