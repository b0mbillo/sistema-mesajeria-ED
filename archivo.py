class Archivo:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def leer(self):
        with open(self.nombre,"r") as archivo:
            contenido = archivo.read()
        return contenido

    def escribir(self, registro):
        with open(self.nombre,"w") as archivo:
            archivo.write(registro)
        return True