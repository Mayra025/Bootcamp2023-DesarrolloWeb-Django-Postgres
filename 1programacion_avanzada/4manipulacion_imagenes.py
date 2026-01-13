from PIL import Image  #importe de clase Image

#Cargar la imagen
im = Image.open("p1.jpg")

#cambiar tamaño de la img    ancho x alto
nuevo_tam=(500,300)  #pixeles
img_redim=im.resize(nuevo_tam)
# img_redim.show()

#guardar img
img_redim.save('p1-redim.jpg')  #C:\\Users\\.....

#Mostrar la img
im.show()

