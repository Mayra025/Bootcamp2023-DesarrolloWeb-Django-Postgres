from abc import ABC, abstractmethod

#HERENCIA Y POLIMORFISMO
class Transporte(ABC):
    @abstractmethod
    def calcular_costo(self):
        pass

class Autobus(Transporte):
    def __init__(self, kilometros) -> None:
        super().__init__()
        self.kilometros=kilometros
    
    def calcular_costo(self):
        TARIFA_KM=2.5
        return f'el costo de viajar en Autobus es: {TARIFA_KM*self.kilometros}'


class Avion(Transporte):
    def __init__(self,horas:int) -> None:
        super().__init__()
        self.horas=horas

    def calcular_costo(self):
        TARIFA_HORA=3.5
        return f'el costo de viajar en Avion es: {TARIFA_HORA*self.horas}'



b1=Autobus(7.6)
b2=Autobus(9.4)
b3=Autobus(10)

a1=Avion(2)
a2=Avion(12)

transportes=[b1, b2, a2, b3]

for t in transportes:
    print(t.calcular_costo())  
