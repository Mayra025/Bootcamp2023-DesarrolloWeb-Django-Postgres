from django.contrib import admin
from .models import Juego   #importo modelo

# Register your models here.
admin.site.register(Juego)  #register para registrar el modelo, y tenemos la interfaz en el admin
