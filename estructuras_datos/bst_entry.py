class BSTEntry:
    def __init__(self, data, key: int) -> None:
        self.data = data
        self.key = key

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def getKey(self):
        return self.key