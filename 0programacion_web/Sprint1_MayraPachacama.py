# Ejercicio 1: Conteo de Letras Mayúsculas y Minúsculas.
# Escribe un programa que cuente cuántas letras mayúsculas y cuántas letras minúsculas hay en una cadena
# de texto que sea ingresada por el usuario.
# Ejemplo:
# Cadena => “Hola mundo, soy de Ecuador y mi lenguaje favorito es Python”
# Resultado => 3 letras mayúsculas y 45 letras minúsculas

#%%
print('Ejercicio 1: Conteo de Letras Mayúsculas y Minúsculas\n')
cadena=input("Ingrese una frase: ")
mayus=0
mins=0

for caracter in cadena:  #for itera por elemento,no por indice
    if caracter.islower():
        mins=mins+1
    elif caracter.isupper():
        mayus=mayus+1

print(cadena)
print("Mayusculas presentes: ", mayus)
print("Minusculas presentes: ", mins)


# Ejercicio 2: Es Palíndromo o no
# Realice un programa que determine si una frase ingresada es un palíndromo, ignorando espacios,
# mayúsculas/minúsculas y signos de puntuación.
# Ejemplo:
# Frase => “"Anita lava la tina"
# Si lees esta frase de izquierda a derecha o de derecha a izquierda, obtendrás la misma secuencia de letras,
# lo que la convierte en una frase palíndroma.
#%%
print('Ejercicio 2: Es Palíndromo o no\n')
frase=input("Ingrese una frase: ")
print(frase)
frase=frase.lower()
frase=frase.replace(" ","")
frase=frase.replace(",","")
frase=frase.replace(".","")
frase=frase.replace("á","a")
frase=frase.replace("é","e")
frase=frase.replace("í","i")
frase=frase.replace("ó","o")
frase=frase.replace("ú","u")

if frase == frase[::-1]:  # es una operación de slicing que invierte la cadena
   print(" es Palindroma")
else:
   print(" no es Palindroma")

# Ejercicio 3: Año Bisiesto
# Escribe un programa que determine si un año ingresado por el usuario es un año bisiesto o no.
# Las reglas para determinar si un año es bisiesto son las siguientes:
# • Un año es bisiesto si es divisible por 4.
# • Sin embargo, si ese año también es divisible por 100, no es bisiesto, a menos que:
# • El año sea divisible por 400, en cuyo caso sí es bisiesto.
#%%
print('Ejercicio 3: Año Bisiesto\n')
year=int(input("Ingrese un año: "))
bisiesto =False

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    bisiesto = True

print(year, "es bisiesto?", bisiesto)


# Ejercicio 4: Números Consecutivos en una lista
# Asuma que existe una lista l1 con números en ella. Escriba un programa que encuentre cuántas veces hay
# 3 números consecutivos en la lista.
# Ejemplo:
# Lista predefinida => l1 = [4, 3, 1, 2, 3, 0, 8, 9, 10, 11,12]
# Resultado => Veces en que hay 3 consecutivos = 4 veces
# Explicación => (Vez 1 => 1-2-3, Vez 2 => 8-9-10, Vez 3=> 9-10-11, Vez 4=>10-11-12). El programa solo debe
# mostrar las veces en que encuentra 3 consecutivos, no es necesario indicar las secuencias.

#%%
print('Ejercicio 4: Números Consecutivos en una lista\n')
l1 = [4, 3, 1, 2, 3, 0, 8, 9, 10, 11,12]
consec=0

for i in range(len(l1)-2):
    aux=l1[i:i+3]   #no incluye el ultimo
    if(len(aux)==3):
        if aux[1] - aux[0] == 1 and aux[2] - aux[1] == 1:
            consec += 1

print(l1)
print("  Veces en que hay 3 consecutivos =", consec)
# %%
