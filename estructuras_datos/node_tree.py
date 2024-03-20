
class NodeTree:
    def __init__(self, data, right: "NodeTree" = None, left: "NodeTree" = None) -> None:
        self.data = data
        self.right = right
        self.left = left

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self, left: "NodeTree"):
        self.left = left

    def setRight(self, right: "NodeTree"):
        self.right = right

    def hasLeft(self):
        return self.getLeft() != None

    def hasRight(self):
        return self.getRight() != None
    
    def isInternal(self):
        return self.hasLeft() or self.hasRight()