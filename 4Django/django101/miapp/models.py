from django.db import models

# Create your models here.
#Para modelado de datos

class Juego(models.Model):
    #de forma implicita, se genera automaticamente un id
    titulo=models.CharField(max_length=100)
    categoria=models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.titulo
    
    


