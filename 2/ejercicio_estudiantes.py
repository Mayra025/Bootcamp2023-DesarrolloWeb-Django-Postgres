from ast import List


class Estudiante:
    def __init__(self,id:int,nombre:str, apellido:str,nacimiento:str) -> None:
        self.__nombre=nombre
        self.__apellido=apellido
        self.__nacimiento=nacimiento
        

class Profesor:
    def __init__(self,nombre:str, apellido:str) -> None:
        self.__nombre=nombre
        self.__apellido=apellido



class Curso:
    def __init__(self,codigo:int,nombre:str,profesor:Profesor) -> None:
        self.__codigo=codigo
        self.__nombre=nombre
        self.__profesor=profesor
        self.__estudiantes=[]

    def agregar_estudiante(self,nuevo:Estudiante):
        self.__estudiantes=nuevo

    def get_codigo(self):
        return(self.__codigo)
    
    def set_codigo(self, nuevo_code:int):
        self.__codigo=nuevo_code

    def get_nombre(self):
        return(self.__nombre)
    
    def set_nombre(self, nuevo:int):
        self.__nombre=nuevo
    
    def get_profesor(self):
        return(self.__profesor)
    
    def set_profesor(self, nuevo:int):
        self.__profesor=nuevo

    def get_estudiantes(self):
        return(self.__estudiantes)
    
    def set_estudiantes(self, nuevo:List[Estudiante]):
        self.__estudiantes=nuevo

    def __str__(self) -> str:
        return f'Curso->(codigo: {self.__codigo}, nombre:{self.__nombre},profesor:{self.__profesor})'