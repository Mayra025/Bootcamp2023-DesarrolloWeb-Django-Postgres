#%% Ejercicio 1_ Evaluar que una cadena tenga almenos una @
import re

cadena='Hola a tod@s'

if re.search('@+',cadena):
    print('se encontró la @')
else:
    print('no se encontró')

# %%Ejer 2: si contiene al menos un digito
import re
cadena = 'Mayra123'

# if re.search('[0-9]+',cadena):
#     print('se encontró al menos un digito')
# else:
#     print('no se encontró')

#operador ternario
res='Match' if re.search('\d',cadena) else 'No Match'
print (res)


# %% un digito y una mayuducla

import re
cadena = 'Mayra123'


res='Match' if re.search('\d.*[A-Z]|[A-Z].*\d',
    cadena) else 'No Match'
print (res)

# %%
import re

def existeSaludo(text):
    patron='ho+la+'
    res='True' if re.search(patron,text) else 'False'
    return res 

# print (existeSaludo('hooooola'))


def esArchivo(nombreArchivo):
    patron='\.(csv|txt|tsv)$'
    res=re.search(patron,nombreArchivo) 
    return bool(res) 


nombre_archivo=input('Ingrese el nombre del archivo: ')
esValido=esArchivo(nombre_archivo)

#operador ternario .. solo para condiciones true o false
print(f"El archivo {nombre_archivo}{' es' if esValido else ' no es'} de texto")

# %%
