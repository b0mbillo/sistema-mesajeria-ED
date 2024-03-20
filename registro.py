from archivo import Archivo
from usuario import Usuario
from direccion import Direccion
from fecha import Fecha
from mensajes import Mensajes
import numpy as np

class Registro:
    def __init__(self, capacidad: int) -> None:
        self.capacidad = capacidad
        self.registro = np.empty(capacidad,dtype=Usuario)
        self.no_usuarios = 0

    def buscarUsuario(self, documento: int):
        for i in range(self.no_usuarios):
            if self.registro[i].getDocumento() == documento:
                return self.registro[i], i
        return False, None

    def buscarUsuarioNombre(self, nombre: str):
        for i in range(self.no_usuarios):
            if self.registro[i].getNombre() == nombre:
                return self.registro[i]
        return False

    def registrarUsuario(self, usuario: Usuario):
        if self.no_usuarios == self.capacidad: return #no deberia nunca cumplirse (validado antes de metodo)

        busqueda, indice = self.buscarUsuario(usuario.documento)
        if busqueda: return False

        self.registro[self.no_usuarios] = usuario
        self.no_usuarios += 1
        self.organizarRegistro()
        return True
    
    def eliminarUsuario(self, documento: str):
        busqueda, indice = self.buscarUsuario(documento)

        if not busqueda:
            return False
        
        self.registro[indice].setDocumento(self.registro[self.no_usuarios - 1].getDocumento() + 1)
        self.organizarRegistro()
        self.registro[self.no_usuarios - 1] = None
        self.no_usuarios -= 1
        return True

    def mostrarRegistro(self):
        if self.no_usuarios == 0:
            return
        for i in range(self.no_usuarios):
            usuario = self.registro[i]
            print(usuario.toString())
    
    def organizarRegistro(self): #insertionsort
        if self.no_usuarios <= 1:
            return
 
        for i in range(1, self.no_usuarios): 
            key = self.registro[i]
            j = i - 1
            while j >= 0 and key.documento < self.registro[j].documento:
                self.registro[j + 1] = self.registro[j] #mover el de la izquierda a la posicion de key
                j -= 1
            self.registro[j + 1] = key

    def exportarRegistro(self, nombre_txt: str):
        archivo = Archivo(nombre_txt)
        texto = """""" + str(self.capacidad) + "\n_"
        for i in range(self.no_usuarios):
            usuario = self.registro[i]
            mensajes = usuario.getMensajes()
            bandeja = mensajes.getBandeja()
            borradores = mensajes.getBorradores()
            leidos = mensajes.getLeidos()
            texto_bandeja = ""
            texto_borradores = ""
            texto_leidos = ""

            if not bandeja.isEmpty(): 
                for i in range(bandeja.getSize()):
                    if i != 0:
                        texto_bandeja += "*!" + str(bandeja.removeFirst())
                    else:
                        texto_bandeja += str(bandeja.removeFirst())
                texto_bandeja += "\n"
            else: texto_bandeja += "null\n"

            if not leidos.isEmpty():
                for i in range(leidos.getSize()):
                    if i != 0:
                        texto_leidos += "*!" + str(leidos.removeFirst())
                    else:
                        texto_leidos+= str(leidos.removeFirst())
                texto_leidos += "\n"
            else: texto_leidos += "null\n"

            if not borradores.isEmpty(): 
                for i in range(borradores.getSize()):
                    if i != 0:
                        texto_borradores += "*!" + str(borradores.removeFirst())
                    else:
                        texto_borradores += str(borradores.removeFirst())
            else: texto_borradores += "null"

            texto_usuario = usuario.exportString() + "\n" + texto_bandeja + texto_leidos + texto_borradores

            if i != self.no_usuarios - 1:
                texto += texto_usuario + "\n_"
            else:
                texto += texto_usuario
        archivo.escribir(texto)
        return True

    def cargarRegistro(nombre_txt: str):
        try:
            datos = Archivo(nombre_txt).leer()
        except FileNotFoundError:
            return False
        
        datos = datos.split("_")
        datos[0] = datos[0].strip("\n")

        capacidad = int(datos.pop(0))
        registro = Registro(capacidad)

        for dato in datos:
            temp = dato.lstrip("\n").rstrip("\n").split("\n")
            bandeja = temp[-3].split("*!")
            leidos = temp[-2].split("*!")
            borradores = temp[-1].split("*!")
            usuario = Usuario(int(temp[0]), temp[1], Fecha(temp[2]), temp[3], Direccion(temp[4]), temp[5], temp[6], temp[7], temp[8], Mensajes(bandeja,leidos,borradores))
            registro.registrarUsuario(usuario)

        return registro

    def getCapacidad(self): 
        return self.capacidad
    
    def getUsuarios(self): 
        return self.no_usuarios
