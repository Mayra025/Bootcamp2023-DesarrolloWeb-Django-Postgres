class Computadora:

    def __init__(self,procesador, ram, tipo,conectividad, esta_pagada,precio):
        self.procesador=procesador
        self.ram=ram
        self.tipo=tipo
        self.conectividad=conectividad
        self.esta_pagada=esta_pagada
        self.precio=precio


pc1=Computadora("Core i5","8GB","desktop","wifi",True,1500)     #contructor
print(pc1.precio)