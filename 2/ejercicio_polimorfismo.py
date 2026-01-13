class Libro:
    def __init__(self,titulo, autor,editorial, paginas) -> None:
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.paginas=paginas


    def __str__(self) -> str:
        return f'El libro {self.titulo} escrito por {self.autor} y publicado por {self.editorial} tiene {self.paginas} páginas'    
    
    def __eq__(self,otro)->bool:
        return self.titulo==otro.titulo and self.autor==otro.autor
    
    def __add__(self,otro):
        if isinstance(otro,Libro):  # si es instancia de Libro
            nuevo_titulo=self.titulo
            nuevo_autor=self.autor
            nuevo_editorial=self.editorial
            nuevo_paginas=self.paginas +otro.paginas

            nuevo_libro=(nuevo_titulo,nuevo_autor,nuevo_editorial,nuevo_paginas)
            return nuevo_libro
        
        else:
            raise ValueError("La concatenacion solo esta permitda entre objetos")
        

lib1=Libro("123","Gabriel","abc",500)
lib2=Libro("456","Mayra", "abc",200)

lib1==lib2

libro_contenado=lib1+lib2

print(libro_contenado)
