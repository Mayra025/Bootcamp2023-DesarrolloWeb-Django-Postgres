import csv

#lista de diccionarios
# [{'nombre': 'Joshua', 'edad':'20',
#   'puntuacion':'90', 'asistencia':'75'},
#   {'nombre': 'Maria', 'edad':'18',
#   'puntuacion':'95', 'asistencia':'80'}
#  ]  

#retornar el contenido del archivo en una lista de diccionarios
def leer_csv(nombre_archivo):
    try: #control de errores
        with open(nombre_archivo, 'r',encoding='UTF-8') as archivo:
            lector = csv.DictReader(archivo)   #dictReader lee el archivo y retorna como Diccionario
            return list(lector)
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no existe')
        return[]

"""
    def filtrar_datos(lista, puntuac):
    filtrados=[]
    for d in lista:
        if (int(d.get('puntuacion')) >= puntuac):  #los valores estan tipo strings, soo cast para hacerlo int
            filtrados.append(d)
    
    return filtrados
"""

def filtrar_datos(lista,puntuac):
    return[e for e in lista if int(e.get('puntuacion'))>=puntuac]

#Guarda la lista de estudiantes filtrada en un nuevo archivo       
def guardar_csv(lista_a_guardar,nombre_archivo):
    try:
        with open(nombre_archivo,'w',newline='', encoding='UTF-8') as archivo:  #newline para no \n
            escritor=csv.DictWriter(archivo, fieldnames=['nombre', 'edad','puntuacion',
                                                'asistencia']) #hay q enviar los nombres de los campos
            escritor.writeheader()
            escritor.writerows(lista_a_guardar)
            print(f'Los datos filtrados se han guardado correctamente en {nombre_archivo}')


    except IOError:
        return print(f'No se pudo escribir sobre el archivo {nombre_archivo}')
    

########################################
lista=leer_csv('alumnos.csv')
lista_filtrada=filtrar_datos(lista,80)
for e in lista_filtrada:
    print(e)

guardar_csv(lista_filtrada, 'resultados_filtrados.csv')
