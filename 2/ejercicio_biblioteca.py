from ast import List


class Libro:
    def __init__(self,titulo:str,autor:str,genero:str) -> None:
        self.__titulo=titulo
        self.__autor=autor
        self.__genero=genero

    def get_titulo(self):
        return(self.__titulo)
    
    def set_titulo(self, nuevo:str):
        self.__titulo=nuevo

    def get_autor(self):
        return(self.__autor)
    
    def set_autor(self, nuevo:str):
        self.__autor=nuevo

    def get_genero(self):
        return(self.__genero)
    
    def set_genero(self, nuevo:str):
        self.__genero=nuevo

    def __str__(self) -> str:
        return f'Libro->(titulo: {self.__titulo}, autor:{self.__autor},genero:{self.__genero})'
        

class Biblioteca:
    def __init__(self) -> None:
        self.__libros=[]

    def agregar_libro(self,nuevo:Libro):
        self.__libros.append(nuevo)
    
    def eliminar_libro(self, anterior:Libro):
        self.__libros.remove(anterior)

    def mostrar_libros(self):
        return f'B->(Libros: {self.__libros})'
    


class Prestamo:
    def __init__(self,libro_prestado:str,nombre_prestamista:str, fecha_prestamo:str ) -> None:
        self.__prestado=libro_prestado
        self.__nombrep=nombre_prestamista
        self.__fecha=fecha_prestamo

    def devolver_libro(self, libro:Libro):
        self.__libros=libro


l1=Libro("Antes de Diciembre", "Joanna Marcús", "Romance")
l2=Libro("El Arte de la Guerra", "Sun Tzu", "Romance")

l2.set_genero("No ficción")
print(l2.get_genero())

biblioteca1=Biblioteca()
biblioteca1.agregar_libro(l1)
biblioteca1.mostrar_libros()
# print(biblioteca1)