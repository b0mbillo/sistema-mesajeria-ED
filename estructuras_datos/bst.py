from .node_tree import NodeTree
from .queue import  Queue
from .bst_entry import BSTEntry
from .stack import Stack

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def addRoot(self, node: NodeTree):
        self.root = node
        self.size += 1

    def getRoot(self):
        return self.root

    def getMax(self):
        return self.maxNode(self.root).getData()

    def getMin(self):
        return self.minNode(self.root).getData()

    def isRoot(self, root: NodeTree):
        return self.root == root

    def insertLeft(self, nodo: NodeTree, left):
        if nodo == self.getMin():
            self.setMin(left)
        nodo.setLeft(NodeTree(left))
        self.size += 1

    def insertRight(self, nodo: NodeTree, right):
        if nodo == self.getMax():
            self.setMax(right)
        nodo.setRight(NodeTree(right))
        self.size += 1

    def remove(self, nodo: NodeTree):
        if nodo == self.root:
            self.root = None
            self.size = 0
            return

        p = self.parent(nodo)
        if nodo.hasLeft() or nodo.hasRight():
            if nodo.hasLeft():
                child = nodo.getLeft()
            else:
                child = nodo.getRight()
            if p.getLeft() == nodo:
                p.setLeft(child)
            else:
                p.setRight(child)
            nodo.setLeft(None)
            nodo.setRight(None)
        else:
            if p.getLeft() == nodo:
                p.setLeft(None)
            else:
                p.setRight(None)
        self.size -= 1

    def height(self, nodo: NodeTree):
        if not nodo.isInternal():
            return 0
        h = max(self.height(nodo.getLeft()), self.height(nodo.getRight()))
        return 1 + h

    def depth(self, nodo: NodeTree):
        if self.isRoot(nodo):
            return 0
        return 1 + self.depth(self.parent(nodo))

    def find(self, key: int):
        return self.searchTree(key, self.root)

    def searchTree(self, key: int, nodo: NodeTree):
        entry = nodo.getData()
        if key == entry.getKey():
            return nodo
        elif key < entry.getKey() and nodo.hasLeft():
            return self.searchTree(key, nodo.getLeft())
        elif key > entry.getKey() and nodo.hasRight():
            return self.searchTree(key, nodo.getRight())
        else:
            return None

    def insert(self, datos, key: int): 
        entry = BSTEntry(datos, key)
        nodo = NodeTree(entry)
        if self.size == 0:
            self.addRoot(nodo)
        else:
            self.addEntry(self.root, entry)
            self.size += 1


    def parent(self, nodo: NodeTree, actual=None, parent=None):
        if actual is None:
            actual = self.root

        if actual == nodo:
            return parent

        if nodo.getData().getKey() < actual.getData().getKey() and actual.hasLeft():
            return self.parent(nodo, actual.getLeft(), actual)
        elif nodo.getData().getKey() > actual.getData().getKey() and actual.hasRight():
            return self.parent(nodo, actual.getRight(), actual)
        else:
            return None

    def removeKey(self, key: int):
        nodo = self.find(key)
        if not nodo:
            return None

        if nodo == self.root:
            self.root = None
            self.size = 0
            return nodo

        padre = self.parent(nodo)
        if nodo.hasLeft() and nodo.hasRight():
            
            predecesor = self.predecesor(nodo)
            padre_predecesor = self.parent(predecesor)

            # Eliminar el predecesor de su posición actual
            if padre_predecesor is not None:
                if predecesor == padre_predecesor.getLeft():
                    padre_predecesor.setLeft(predecesor.getRight())
                else:
                    padre_predecesor.setRight(predecesor.getRight())
            else:
                # Si el predecesor no tiene padre, es el hijo izquierdo del nodo a eliminar
                nodo.setLeft(predecesor.getRight())

            predecesor.setLeft(nodo.getLeft())
            predecesor.setRight(nodo.getRight())
            if nodo == padre.getLeft():
                padre.setLeft(predecesor)
            else:
                padre.setRight(predecesor)
            self.size -= 1
        else:
            #un solo hijo o sin hijos
            hijo = nodo.getLeft() if nodo.hasLeft() else nodo.getRight()
            if nodo == padre.getLeft():
                padre.setLeft(hijo)
            else:
                padre.setRight(hijo)
            self.size -= 1
        return nodo


    def inorder(self, nodo: NodeTree):
        if nodo.hasLeft():
            self.inorder(nodo.getLeft())
        print(nodo.getData().getKey())
        if nodo.hasRight():
            self.inorder(nodo.getRight())

    def mostrarArbol(self, nodo: NodeTree):
        self.mostrar(nodo)
        print(self.size)

    def mostrar(self, nodo: NodeTree, nivel = 0, prefijo = "Raiz: "):
        if nodo:
            print(" " * (nivel*4) + prefijo + str(nodo.getData().getKey()) + "-" + nodo.getData().getData())
            if nodo.isInternal():
                self.mostrar(nodo.getRight(), nivel + 1, "Der: ")
                self.mostrar(nodo.getLeft(), nivel + 1, "Izq: ")

    def addEntry(self, nodo: NodeTree, entry: BSTEntry):
        temp = nodo.getData()
        new_nodo = NodeTree(entry)

        if entry.getKey() <= temp.getKey():
            if nodo.hasLeft():
                self.addEntry(nodo.getLeft(), entry)
            else:
                nodo.setLeft(new_nodo)
        else:
            if nodo.hasRight():
                self.addEntry(nodo.getRight(), entry)
            else:
                nodo.setRight(new_nodo)

    def maxNode(self, nodo: NodeTree):
        if nodo.hasRight():
            return self.maxNode(nodo.getRight())
        return nodo 
    
    def minNode(self, nodo: NodeTree):
        if nodo.hasLeft():
            return self.minNode(nodo.getLeft())
        return nodo

    def predecesor(self, nodo: NodeTree):
        temp = nodo.getLeft()
        return self.maxNode(temp)