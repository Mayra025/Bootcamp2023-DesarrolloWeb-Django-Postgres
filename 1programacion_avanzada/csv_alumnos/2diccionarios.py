import csv

#%%
#DICCIONARIO
persona={'nombre':"Mayra", 
         'apellido':"Pachacama",
         'edad':"23"
         }
print(persona.get('nombre'))  ##se llama por la   clave
print(persona['nombre']) 


for i in persona.items():  #keys(), values(), items() -> devuelve como tupla
    print (i)

for i,j in persona.items():
    print(i,j)

#Añadiendo una clave y su valor
persona['ciudad']='Quito'

for i,j in persona.items():
    print(f'{i}: {j}')
# %%
