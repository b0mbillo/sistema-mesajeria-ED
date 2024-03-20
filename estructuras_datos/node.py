class Node:
    def __init__(self, datos, siguiente: "Node" = None) -> None:
        self.data = datos
        self.next = siguiente 

    def setData(self, datos_nuevos):
        self.data = datos_nuevos

    def setNext(self, siguiente: "Node" = None):
        self.next = siguiente

    def getData(self):
        return self.data

    def getNext(self):
        return self.next