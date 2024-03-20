from archivo import Archivo
from estructuras_datos import prueba

datos = Archivo("x.txt").leer()
datos = datos.split("_")
print(datos)
datos[0] = datos[0].strip("\n")
capacidad = int(datos.pop(0))
dato = datos[0].lstrip("\n").rstrip("\n").split("\n")
BA = dato[-3].split("*!") #['12/12/2019*correo1*andres*hola como estas??', '13/12/2019*correo2*andres*respondeme']
ML = dato[-2]
B = dato[-1]
print(BA)
for D in BA:
   print(D) #.split("*")

