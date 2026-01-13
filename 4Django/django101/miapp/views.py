from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Juego

# Create your views here.

videojuegos = [
    {'id':1, 'titulo':'Super Mario Bros', 'categoria':'Aventuras'},
    {'id':2, 'titulo':'Need For Speed', 'categoria':'Carreras'},
    {'id':3, 'titulo':'Pokemon', 'categoria':'Aventuras'},
    {'id':4, 'titulo':'Call of Duty', 'categoria':'Combate'},
    {'id':5, 'titulo':'Resident Evil', 'categoria':'Combate'},
]

def home(request):
    juegos=Juego.objects.all()
    return render(request , 'lista_juegos.html', {'lista_juegos':juegos}) #envio juegos desde la BD

    # return render(request , 'lista_juegos.html', {'lista_juegos':videojuegos}) #envio a renderizar un html con la lista de juegos
    # return HttpResponse("Hola mundo desde Django")

def detalle_juego(request,id):
    try:
        juego=Juego.objects.get(id=id)
    except Juego.DoesNotExist:
            raise Http404('Juego no encontrado') 
    
    ## Usando el arreglo de esta vista
    # juego=None

    # for item in videojuegos:
    #     if item ['id'] == id:
    #         juego=item
    #         break

    # if juego is None:
    #     raise Http404('Juego no encontrado') #tipo plantilla asociada a la respouesta de la peticion


    return render(request, 'detalle_juego.html', {'juego': juego})
