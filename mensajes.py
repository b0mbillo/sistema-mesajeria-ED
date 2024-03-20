from estructuras_datos import *

class Mensajes:
    def __init__(self, bandeja: list = ["null"], leidos: list = ["null"], borradores: list = ["null"]) -> None:
        self.bandeja = DoubleList()
        self.leidos = Queue()
        self.borradores = Stack()

        if bandeja[0] != "null": 
            for mensaje in bandeja:
                self.bandeja.addLast(mensaje)
        if leidos[0] != "null": 
            for mensaje in leidos:
                self.leidos.enqueue(mensaje)
        if borradores[0] != "null": 
            for mensaje in borradores:
                self.borradores.push(mensaje)

    def getBandeja(self):
        return self.bandeja
    
    def getLeidos(self):
        return self.leidos

    def getBorradores(self):
        return self.borradores
    