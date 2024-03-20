from .lista import List

class Stack(List):
    def __init__(self) -> None:
        super().__init__()

    def push(self, datos):
        return self.addLast(datos)

    def pop(self):
        return self.removeLast()

    def top(self):
        return self.last()

    def first(self):
        pass