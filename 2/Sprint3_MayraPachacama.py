# Clases:

# 1. Clase abstracta Jugador:
#    - Implementa el método abstracto `elegir_casilla(self)`.
#    - Posee los atributos `nombre` y `símbolo`.
from abc import ABC, abstractmethod
import random

class Jugador(ABC):
    def __init__(self, nombre, simbolo) -> None:
        self.__nombre=nombre
        self.__simbolo=simbolo

    @abstractmethod
    def elegir_casilla(self)->int:
        pass 

    def __str__(self) -> str:
        return f'jugador {self.__nombre} ({self.__simbolo}) ' 

# 2. Clase JugadorHumano:
#    - Hereda de Jugador.
#    - Su método `elegir_casilla(self)` solicita al usuario ingresar una casilla para marcar con el formato `x, y` (indicando una coordenada).
class JugadorHumano(Jugador):
    def __init__(self, nombre) -> None:
        super().__init__(nombre, simbolo='x')
        self.__nombre=nombre

    def elegir_casilla(self)->int:
        eleccion_x=input("Ingrese el n° de fila entre 1-3: ")
        while not eleccion_x.isdigit() or not (1 <= int(eleccion_x) <=3):
            eleccion_x=input('Ingrese de nuevo, fila entre 1-3:')
        
        eleccion_x=int(eleccion_x)
        eleccion_y=input("Ingrese el n° de columna entre 1-3: ")
        while not eleccion_y.isdigit() or not (1 <= int(eleccion_y) <=3):
            eleccion_y=input('Ingrese de nuevo, columna entre 1-3:')

        eleccion_y=int(eleccion_y)
        return eleccion_x-1,eleccion_y-1

# 3. Clase JugadorPC:
#    - Hereda de Jugador.
#    - Implementa `elegir_casilla(self)`, que elige una coordenada de forma aleatoria.

class JugadorPC(Jugador):
    def __init__(self) -> None:
        super().__init__(nombre="PC",simbolo="o")

    def elegir_casilla(self)->int:
        #3x3
        pos_x=random.randrange(0,3)
        pos_y=random.randrange(0,3)
        # return f'la casilla es: {pos_x}, {pos_y}'
        return pos_x,pos_y
    
# 4. Clase Tablero:
#    - Posee el atributo `casillas`, un diccionario donde las claves son tuplas con dos valores `(x, y)` y los valores son símbolos marcados en esa casilla (inicialmente, todas vacías).
class Tablero():
    #         - Inicializa `casillas` con un string vacío como valor de cada clave.
    def __init__(self) -> None:
        self.__casillas = {(x, y): ' ' for x in range(3) for y in range(3)}

#         - Modifica `casillas` asignando el símbolo a la tupla asociada a las posiciones `x, y`.
    def marcar_casilla(self,x,y,simbolo)->None:
        self.__casillas[(x,y)]=simbolo
        
#         - Verifica que las coordenadas `x, y` del tablero no estén marcadas. Retorna `True` si la casilla no está marcada, caso contrario `False`.
    def es_valida(self,x,y)->bool:
        no_marcada=False 
        if self.__casillas [(x,y)] != " ":
            print("Escoje una casilla vacía !")
        else: 
            no_marcada=True

        return no_marcada        

    def hay_victoria(self) -> bool:
        for i in range(3):
            # Verificación de filas
            if self.__casillas[(i, 0)] != ' ' and self.__casillas[(i, 1)] == self.__casillas[(i, 0)] and self.__casillas[(i, 2)] == self.__casillas[(i, 0)]:
                return True

            # Verificación de columnas
            if self.__casillas[(0, i)] != ' ' and self.__casillas[(1, i)] == self.__casillas[(0, i)] and self.__casillas[(2, i)] == self.__casillas[(0, i)]:
                return True

        # Verificación de diagonal principal
        if self.__casillas[(0, 0)] != ' ' and self.__casillas[(1, 1)] == self.__casillas[(0, 0)] and self.__casillas[(2, 2)] == self.__casillas[(0, 0)]:
            return True

        # Verificación de diagonal secundaria
        if self.__casillas[(2, 0)] != ' ' and self.__casillas[(1, 1)] == self.__casillas[(0, 2)] and self.__casillas[(2, 0)] == self.__casillas[(0, 2)]:
            return True

        return False
    
    def __str__(self) -> str:
        tablero_str = ""
        for i in range(3):
            for j in range(3):
                tablero_str += f"{self.__casillas[(i, j)]}"
                if j < 2:
                    tablero_str += " | "  # Separador entre columnas
            tablero_str += "\n"
            if i < 2:
                tablero_str += "- + - + -\n"  # Línea divisoria entre filas

        return tablero_str
    
    def tablero_lleno(self) ->bool:
        casillas_llenas = sum(1 for valor in self.__casillas.values() if valor != ' ')
        return casillas_llenas == 9  # En un tablero de 3x3 hay un total de 9 casillas     

# Programa Principal:

# - Cree un programa que instancie un `Tablero`.
nuevo_juego=Tablero()
turno =0
ganador=None
print("\nBIENVENIDX AL JUEGO DE TIC-TAC-TOE 🚀")

# print("1. Un jugador ")
# print("2. Dos jugadores")
# modo=1
# modo=input("Escoja el modo de juego: ")
# while not modo.isdigit():
#     modo=input("Escoja el modo de juego: ")

nombre1 = input("Ingrese su nombre: ")
nuevo_jugador = JugadorHumano(nombre1)

while not nuevo_juego.tablero_lleno():
    print("\nVista actual del Tablero:")
    print(nuevo_juego)

    if turno == 0:
        print("//-------------------------------------------------------------------------------------------//")
        print(f" Es turno de {nuevo_jugador}")
        x1, y1 = nuevo_jugador.elegir_casilla()
        while not nuevo_juego.es_valida(x1, y1) and not nuevo_juego.tablero_lleno():
            x1, y1 = nuevo_jugador.elegir_casilla()
        print(f"Casilla: {x1+1}, {y1+1}")
        nuevo_juego.marcar_casilla(x1, y1, 'x')

        if nuevo_juego.hay_victoria():
            ganador = nombre1
            break

        turno = 1
    else:
        jugador_pc = JugadorPC()
        print("//-------------------------------------------------------------------------------------------//")
        print(f" Es turno de {jugador_pc}")
        x_pc, y_pc = jugador_pc.elegir_casilla()
        while not nuevo_juego.es_valida(x_pc, y_pc) and not nuevo_juego.tablero_lleno():
            x_pc, y_pc = jugador_pc.elegir_casilla()
        print(f"Casilla: {x_pc+1}, {y_pc+1}")
        nuevo_juego.marcar_casilla(x_pc, y_pc, 'o')

        if nuevo_juego.hay_victoria():
            ganador = "PC"
            break

        turno = 0

if ganador:
    print(f"\n\n{ganador} ganó!" if ganador == "PC" else f"\n\n Felicidades, {ganador} ganaste!")
else:
    print("\n\nEs un empate")

print(nuevo_juego)

      