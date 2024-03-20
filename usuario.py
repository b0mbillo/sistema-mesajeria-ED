from fecha import Fecha
from direccion import Direccion
from mensajes import Mensajes

class Usuario:
    def __init__(self, documento: int, nombre: str, fecha_nacimiento: Fecha, ciudad_nacimiento: str, direccion: Direccion , tel: str, email: str, contraseña: str, perfil: str, mensajes: Mensajes) -> None:
        self.documento = documento
        self.nombre = nombre
        self.fecha_nacimento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.direccion = direccion
        self.tel = tel
        self.email = email
        self.password = contraseña
        self.perfil = perfil
        self.mensajes = mensajes

    def toString(self):
        return f"""
{self.documento}
{self.nombre}
{self.fecha_nacimento.toString()}
{self.ciudad_nacimiento}
{self.direccion.toString()}
{self.tel}
{self.email}
{self.perfil}"""

    def exportString(self):
         return f"""
{self.documento}
{self.nombre}
{self.fecha_nacimento.toString()}
{self.ciudad_nacimiento}
{self.direccion.toString()}
{self.tel}
{self.email}
{self.password}
{self.perfil}"""

    def setDocumento(self, documento: int):
        self.documento = documento

    def getPassword(self):
        return self.password

    def getPerfil(self):
        return self.perfil

    def getNombre(self):
        return self.nombre

    def getDocumento(self):
        return self.documento

    def setPassword(self, contraseña: str):
        self.password = contraseña

    def getMensajes(self):
        return self.mensajes