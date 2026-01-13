#     #Apertura de archivos
# file = open('alumnos.txt', 'r+')

#     #Lectura del contenido del archivo
# # print(file.read())

# #lee 1 linea, la primera del archivo
# # print(file.readline())

# for linea in file:
#     # print(linea) #asi imprime con doble salto de linea
#     linea=linea.strip()  #strip  remueve saltos de linea al incio o final de la cadena
#     print (linea)

#     #Escribir en el archivo
# file.write('\nWilson Fustillos')


###############################################
file = open('alumnos.txt', 'a+')  #el append apunta al final , soo por eso no puede leer linea a linea
# file=open('D:\\alumnos.txt','r')

file.seek(0)  #ahi es necesario  seek
for linea in file:
    linea=linea.strip()  #strip  remueve saltos de linea al incio o final de la cadena
    print (linea)

    #Escribir en el archivo
file.write('\nWilson Fustillos')



#######################3
