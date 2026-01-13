from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin (admin.ModelAdmin): #el modelo viene de la importacion en la linea 1
    list_display=('id', 'nombre', 'fecha_registro') #muestra las categorias


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'activo', 'fecha_registro')