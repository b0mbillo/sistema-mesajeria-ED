from .lista import List

class Queue(List):
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, datos):
        return self.addLast(datos)

    def dequeue(self):
        return self.removeFirst()

    def last(self):
        pass

    def removeLast(self):
        pass