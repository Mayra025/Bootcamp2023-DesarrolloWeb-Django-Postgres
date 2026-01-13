#%% 3. calculadora con funciones aritmeticas

def sumar(n1,n2):
    suma = n1+ n2
    return suma

def restar (n1, n2):
    resta=n1-n2
    return resta

def multiplicar (n1,n2):  #parametros
    return n1*n2
    
def dividir(n1,n2):
    return n1/n2

n1=int(input("Ingresa un numero entero: "))
n2=int(input("Ingresa otro numero entero: "))

operacion=input("Ingrese la operacion [+, -, *, /] ")

if operacion =='+':
    res=sumar(n1,n2)   #argumentos
elif operacion == '-':
    res=restar(n1,n2)
elif operacion == '*':
    res=multiplicar(n1,n2)
elif operacion == '/':
    res=dividir(n1,n2)
else:
    print('opeación inválida! ')


#Formateo de string(F-string)
print(f'el resultado es:{res}')


# %%
