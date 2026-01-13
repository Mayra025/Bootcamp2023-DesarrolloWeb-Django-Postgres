from django.contrib import admin

# Register your models here.
from .models import Categoria, Evento, Ciudad

@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin): #el modelo viene de la importacion en la linea 1
    list_display=('id', 'nombre') #muestra las categorias


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'estado', 'fecha')


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')