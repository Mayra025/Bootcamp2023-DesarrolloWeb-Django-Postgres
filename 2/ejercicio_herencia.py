class Vehiculo:
    def __init__(self, marca,modelo,color) -> None:
        self.marca=marca
        self.modelo=modelo
        self.color=color

    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
        
class Carro(Vehiculo): #herencia
    def __init__(self,marca, modelo,color,numero_puertas) -> None:
        super().__init__(marca,modelo,color)   #herencia
        self.num_puertas=numero_puertas

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, tipo_moto) -> None:
        super().__init__(marca,modelo,color)


moto1=Moto("KTM","Enduro 5600","Rojo","endro")
print(moto1.get_marca())
print(moto1.get_modelo())