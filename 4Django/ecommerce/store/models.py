from django.db import models

# Create your models here.
class Categoria(models.Model):
    #se genera un campo id automaticamente?? idk
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)  # slug es para ningun caracter especial, excepto -  Con unique para q sea unico
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        # return f'{self.nombre ({self.id})}'
        return f'{self.nombre} ({self.id})'


    class Meta: #el ORM hara esto??, idk
        db_table = 'st_categorias'
        verbose_name = 'Categoria' #label de la tabla
        verbose_name_plural= 'Categorias'
    

class Producto (models.Model):
    categorias=models.ManyToManyField(Categoria,related_name='productos')
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(null=True, blank=True)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    activo=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to='productos/')  #este necesita libreria pillow
    fecha_registro=models.DateTimeField(auto_now_add=True)  #True para activar fecha/hora actual en la insercion
    fecha_ult_actualizacion=models.DateTimeField(auto_now=True) #este es para fecha actual

    def __str__(self)->str:
        return f'{self.nombre}'

    class Meta: #metadatos
            db_table = 'st_productos'
            verbose_name = 'Producto' 
            verbose_name_plural= 'Productos'

