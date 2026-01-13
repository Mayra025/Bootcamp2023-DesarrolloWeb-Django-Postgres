class Persona:
    def __init__(self, cedula:str,nombre:str,apellido:str) -> None:
        self.__cedula=cedula   #usar siempre para proteger los  tipos de datos
        self.__nombre=nombre
        self.__apellido=apellido

    def get_cedula(self) -> str:  # str xq retorna un String
        return self.__cedula
    
    def set_cedula(self,cedula) -> None:  #None porq no retorna nada
        self.__cedula=cedula

    def get_nombre(self) ->str:
        return self.__nombre
    
    def set_nombre(self,nombre) -> None:
        self.__nombre=nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self,apellido) -> None:
        self.__apellido=apellido

    def __str__(self) -> str: # no print xq el tostring retorna necesariamente str
        return f'Persona -> (cedula: {self.__cedula}, nombre: {self.__nombre}, apellido: {self.__apellido})'
    
class Cuenta:
    def __init__(self, titular:Persona, monto:float, nrocuenta:str) -> None:
        self.__nro=nrocuenta
        self.__titular=titular
        self.__monto=monto

    def get_nrocuenta(self) ->str:
        return self.__nro
    
    def set_nrocuenta(self,nro) -> None:
        self.__nro=nro

    def get_titular(self) ->Persona:
        return self.__titular
    
    def set_titular(self,titular) -> None:
        self.__titular=titular

    def get_monto(self) -> float:   #get monto
        return self.__monto
    
    def set_monto (self,monto) -> None:
        self.__monto=monto

    def __str__(self) -> str:
        return f'Cuenta -> (nro: {self.__nro}, titular: {self.__titular}, monto:{self.__monto})'

    def ingresar(self,cantidad:float) -> None:  #set_monto
        self.__monto = self.__monto+cantidad

    def retirar(self, cantidad:float) -> None:
        if cantidad <= self.__monto:
            self.__monto -= cantidad
        else:
            print (f"Tienes {self.__monto}, NO puedes retirar {cantidad}")


class CuentaAhorros(Cuenta):
    COMISION= 1.0
    
    #redefiniendo un metodo
    def ingresar(self, cantidad: float) -> None:
        if (cantidad > self.COMISION):
            #self.monto -= self.COMISION .. NO ES POSIBLE porq monto no pertenece a CuentaAhorros
            super().ingresar(cantidad-self.COMISION)
        else:
            print(f'La cantidad a ingresar de ser mayor que {self.COMISION}')
    
    def retirar(self, cantidad: float) -> None:
        return super().retirar(cantidad+self.COMISION)   #obs: el retorno esta demas xq no retorna nada
    
    @staticmethod
    def mostrar_politicas()->None:
        print("Cuenta de Ahorros: se cobra 1$ por comision de retiro o ingreso")


class CuentaCorriente(Cuenta):
    TASA=0.01

    def ingresar(self, cantidad: float) -> None:
        if cantidad >= 100:
            cantidad -=  self.TASA*cantidad
        super().ingresar(cantidad)
    
    def retirar(self, cantidad: float) -> None:
        if cantidad >= 100:
            cantidad += self.TASA*cantidad   
        super().retirar(cantidad)

##METODO ESTATICO
    @staticmethod
    def mostrar_politicas()->None:
        print("Cuenta Corriente: se cobra 1$ por comision si el ingreso/retiro es mayor a ")
   



titular1=Persona("123456789", "Mayra", "Pachacama")
cuenta1=CuentaAhorros(titular1,100,"0001")
cuenta2=CuentaCorriente(titular1,50,"002")

#mostrar politicas
CuentaAhorros.mostrar_politicas()
CuentaCorriente.mostrar_politicas()


cuenta1.ingresar(150)
print(f'Saldo en ahorros:{cuenta1.get_monto()}')

cuenta2.ingresar(150)
print(f'Saldo en corriente:{cuenta2.get_monto()}')

cuenta2.retirar(200)
print(f'Saldo en corriente: {cuenta2.get_monto()}')