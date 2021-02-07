class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        if self.next_node:
            return "({0},#{1}, -> #{2})".format(self.data, id(self), id(self.next_node))
        else:
            return "({0},#{1}, -> None)".format(self.data, id(self))

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.next_node

    def modifyNextNode(self, node):
        self.next_node = node

    def modifyData(self, data):
        self.data = data
