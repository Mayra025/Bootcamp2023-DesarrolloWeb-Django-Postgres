from django.db import models

# Create your models here.
class Categoria(models.Model):
    #se genera un campo id automaticamente?? idk
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)  # slug es para ningun caracter especial, excepto -  Con unique para q sea unico
    
    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'


    class Meta: 
        db_table = 'st_categorias'
        verbose_name = 'Categoria' #label de la tabla
        verbose_name_plural= 'Categorias'

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)  # slug es para ningun caracter especial, excepto -  Con unique para q sea unico
    
    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'


    class Meta: 
        db_table = 'st_ciudades'
        verbose_name = 'Ciudad' #label de la tabla
        verbose_name_plural= 'Ciudades'

class Evento (models.Model):
    categorias=models.ManyToManyField(Categoria,related_name='eventos')
    ciudades=models.ManyToManyField(Ciudad,related_name='eventos')
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField(null=True, blank=True)
    precio=models.TextField(null=True, blank=True)
    estado=models.BooleanField(default=True)
    # estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('cancelado', 'Cancelado')], default='activo')
    imagen=models.ImageField(upload_to='eventos/')  #este necesita libreria pillow
    fecha=models.DateTimeField()  
    hora = models.TimeField()

    def __str__(self)->str:
        return f'{self.nombre}'

    class Meta: #metadatos
            db_table = 'st_eventos'
            verbose_name = 'Evento' 
            verbose_name_plural= 'Eventos'

