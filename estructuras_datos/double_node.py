from .node import Node

class DoubleNode(Node):
    def __init__(self, datos, siguiente: "DoubleNode" = None, previo: "DoubleNode" = None) -> None:
        self.prev = previo
        self.data = datos
        self.next = siguiente

    def setPrev(self, previo: "DoubleNode" = None):
        self.prev = previo

    def getPrev(self):
        return self.prev