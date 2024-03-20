from .lista import List
from .double_node import DoubleNode

class DoubleList(List):
    def __init__(self) -> None:
        super().__init__()

    def addFirst(self, datos):
        nodo = DoubleNode(datos, self.head)
        if not self.isEmpty(): 
            self.head.setPrev(nodo)
        self.head = nodo
        if self.isEmpty():
            self.tail = nodo
        self.size += 1
        return True

    def addLast(self, datos):
        if self.isEmpty():
            return self.addFirst(datos)
        nodo = DoubleNode(datos, None, self.tail)
        self.tail.setNext(nodo)
        self.tail = nodo
        self.size += 1
        return True

    def removeFirst(self):
        if self.isEmpty():
            return
        elif self.head == self.tail:
            nodo = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return nodo.getData()
        nodo = self.head
        self.head = nodo.getNext()
        nodo.setNext()
        self.head.setPrev()
        self.size -= 1
        return nodo.getData()

    def removeLast(self):
        if self.isEmpty():
            return
        elif self.head == self.tail:
            nodo = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return nodo.getData()
        nodo = self.tail
        self.tail = nodo.getPrev()
        self.tail.setNext()
        nodo.setPrev()
        self.size -= 1
        return nodo.getData()

    def remove(self, nodo: DoubleNode):
        if self.isEmpty():
            return
        elif nodo == self.head:
            self.removeFirst()
        elif nodo == self.tail:
            self.removeLast()
        else:
            previo = nodo.getPrev()
            siguiente = nodo.getNext()
            siguiente.setPrev(previo)
            previo.setNext(siguiente)
            nodo.setNext()
            nodo.setPrev()
            self.size -= 1
            return nodo.getData()

    def addBefore(self, nodo: DoubleNode, datos):
        if nodo == self.head:
            self.addFirst(datos)
        else:
            previo = nodo.getPrev()
            nuevo = DoubleNode(datos,nodo,previo)
            previo.setNext(nuevo)
            nodo.setPrev(nuevo)
            self.size += 1
            return True

    def addAfter(self, nodo: DoubleNode, datos):
        if self.isEmpty():
            return
        if nodo == self.tail:
            return self.addLast(datos)
        siguiente = nodo.getNext()
        temp = DoubleNode(datos,siguiente,nodo)
        nodo.setNext(temp)
        siguiente.setPrev(temp)
        self.size += 1
        return True
