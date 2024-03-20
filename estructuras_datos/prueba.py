from . import *

class Prueba:
    def lista():
        lista = List()
        for i in range(5):
            lista.addFirst(i)
        lista.show()

        print("cabeza",lista.first().getData())
        print("cola",lista.last().getData())
        lista.removeLast()
        lista.show()

        print("cabeza",lista.first().getData())
        print("cola",lista.last().getData())
        lista.removeFirst()
        lista.addFirst("5")
        lista.removeLast()
        lista.removeLast()
        lista.removeLast()

        lista.show()

    def listaDoble():
        lista_doble = DoubleList()
        for i in range(5):
            lista_doble.addLast(i)
        lista_doble.show()

        print("cabeza",lista_doble.first().getData())
        print("cola",lista_doble.last().getData())
        lista_doble.removeLast()
        lista_doble.show()

        print("cabeza",lista_doble.first().getData())
        print("cola",lista_doble.last().getData())
        lista_doble.removeFirst()
        lista_doble.addFirst("5")
        lista_doble.show()

        lista_doble.addBefore(lista_doble.last(),6)
        lista_doble.addAfter(lista_doble.first(),7)
        lista_doble.show()

        lista_doble.remove(lista_doble.first().getNext())
        lista_doble.remove(lista_doble.first().getNext().getNext())
        lista_doble.show()
        lista_doble.removeFirst()
        lista_doble.removeFirst()
        lista_doble.removeFirst()
        lista_doble.show()
        lista_doble.removeLast()
        lista_doble.show()

    def stack():
        pila = Stack()
        for i in range(5):
            pila.push(i)
        pila.show()
        pila.pop()
        pila.pop()
        pila.show()
        print(pila.top().getData())

    def queue():
        cola = Queue()
        for i in range(5):
            cola.enqueue(i)
        cola.show()
        cola.dequeue()
        cola.dequeue()
        cola.show()
        print(cola.first().getData())