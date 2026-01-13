import csv
import re

estudiantes=[]

# Solicita al usuario 3 datos del estudiante: el nombre (¡solo letras y espacios, por favor!), la edad y el curso (un código de curso).
# Valida el nombre utilizando expresiones regulares. 
def agregar_estudiante():
    name=input('Ingresar el nombre del estudiante: ')
    patron = "^[a-zA-Z.\s]+$"
    if not re.search(patron, name):
        print(f' {name} es un nombre inválido')
        return 0
    
    age=int(input('Ingresar la edad del estudiante: '))
    course=input('Ingresar el código del curso del estudiante: ')

    # estudiante:{'nombre':name,   ###OJOO esto no vale xq aqui la sintaxis del code importa
    #             'edad':age,
    #             'curso':course}
    
    estudiante = {
        'nombre': name,
        'edad': age,
        'curso': course
    }

    estudiantes.append(estudiante)
    print(" Agregado!")
   

# Permite buscar estudiantes por su nombre. 
def buscar_estudiante():
    nombre=input('Ingrese el Nombre del estudiante a buscar: ')
    res=[e for e in estudiantes if e.get('nombre').lower() == nombre.lower()]

    if res :
        print(" Resultados de la búsqueda:")
        for r in res:
            print (r)
            # print(f"Nombre: {resultado['nombre']}, Edad: {resultado['edad']}, Curso: {resultado['curso']}")
    else:
        print( f' {nombre} no existe en la lista de estudiantes')
        return 0


# Da al usuario la capacidad de despedir a un estudiante. 
def eliminar_estudiante():
    nombre=input('Ingrese el Nombre del estudiante a eliminar: ') #suponiendo q el nombre es unico
    for e in estudiantes: #el estudiante existe
        if e.get('nombre').lower() == nombre.lower():
            estudiantes.remove(e)
            print(" ¡Adiós, querido estudiante! 😢")
        else:
            print(f' No es posible eliminar: {nombre}, no existe en el registro')
            return 0


# Crea una función para exportar todos los estudiantes a un archivo CSV. Organiza la información de manera ordenada (exportar el listado de estudiantes en orden alfabético).
def exportar_csv():
    nombre_archivo=input('Ingrese el nombre del archivo, agrega .csv: ')
    lista_ordenada=sorted(estudiantes,key=lambda e: e.get('nombre').lower())  # .get  xq estudiantes es una lista de diccionarios?
    try:
        with open(nombre_archivo,'w',newline='',encoding='UTF-8') as archivo:
            escritor=csv.DictWriter(archivo,fieldnames=['nombre', 'edad', 'curso'])
            escritor.writeheader()
            escritor.writerows(lista_ordenada)
            print(f' Los datos se han guardado correctamente en: {nombre_archivo}')

    except IOError:
        return print(f' No se pudo escribir sobre el archivo {nombre_archivo}')


# ¡Agrega una función que cuente y muestre cuántos estudiantes hay por cada curso!
def numero_estudiantes_por_curso():
    cursos={}

    for e in estudiantes:
        curso = e.get('curso') #key
        cursos[curso] = cursos.get(curso, 0) + 1 # key:valor

    if cursos:
        print(" Número de estudiantes por curso:")
        for curso, cant in cursos.items():
            print(f"Curso {curso}: {cant} estudiante/s")
    else:
        print(" No se encontraron resultados")


#MENÚ
continuar='y'
while (continuar=='y'):
    print ('\nBIENVENIDX AL 🚀 ¡Sistema de Registro de Estudiantes! 🚀')
    print('1. Agregar Estudiante')
    print('2. Buscar Estudiante')
    print('3. Eliminar Estudiante')
    print('4. Exportar Estudiantes')
    print('5. Contar Estudiantes por curso')
    opcion=int(input('Ingresa el número de opcion escogida: '))

    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        buscar_estudiante()
    elif opcion == 3:
        eliminar_estudiante()
    elif opcion == 4:
        exportar_csv()
    elif opcion == 5:
        numero_estudiantes_por_curso()
    else:
        print('opción inválida! ')
    continuar=input('Deseas continuar (y/n)?')

print(' Gracias por usar nuestro sistema 🤓')
