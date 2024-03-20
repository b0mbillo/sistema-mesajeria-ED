from .node import Node

class List:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def addFirst(self, datos):
        nodo = Node(datos, self.head)
        self.head = nodo
        if self.isEmpty():
            self.tail = nodo
        self.size += 1
        return True

    def addLast(self, datos):
        if self.isEmpty():
            return self.addFirst(datos)
        nodo = Node(datos)
        self.tail.setNext(nodo)
        self.tail = nodo
        self.size += 1
        return True

    def removeFirst(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.getNext()
        temp.setNext()
        self.size -= 1 
        return temp.getData()

    def removeLast(self):
        if self.size == 1:
            self.removeFirst()
        else:
            temp = self.tail
            nodo = self.head
            while(nodo.getNext() != self.tail):
                nodo = nodo.getNext()
            nodo.setNext()
            self.tail = nodo
            self.size -= 1
            return temp.getData()

    def isEmpty(self):
        if self.size == 0:
            return True

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def getSize(self):
        return self.size

    def getData(self):
        nodo = self.head
        for _ in range(self.size):
            yield nodo.data
            nodo = nodo.getNext()

    def show(self):
        data = self.getData()
        print(*data)