from DSAA.data_structure.basic.node import Node


class LinkedList:
    def __init__(self, node=None):
        self.head_node = node
        self.last_node = node
        self.traveler = Traveller(self.head_node)

    def __iter__(self):
        return self.traveler

    def __next__(self):
        tmp = next(self.traveler)
        if tmp:
            return tmp
        raise StopIteration

    def __repr__(self):
        info = ""
        for node in self.travel():
            info += "{0} -> ".format(node)
        return info + "None"

    def is_empty(self):
        return not self.head_node

    def travel(self):
        res = []
        pointer = self.head_node
        while pointer:
            res.append(pointer)
            pointer = pointer.getNextNode()
        return res

    def length(self):
        return len(self.travel())

    def getIndex(self, node):
        nodes = self.travel()
        for i in range(0, len(nodes)):
            if node.getData() == nodes[i].getData():
                return i
        return -1

    def getNode(self, index):
        nodes = self.travel()
        if index < 0 or index > (len(nodes) - 1):
            raise IndexError("Index {0} out of bound".format(index))

        for i in range(0, len(nodes)):
            if i == index or i == self.length() - index:
                return nodes[i]

    def app_end(self, node):
        if not self.is_empty():
            self.last_node.modifyNextNode(node)
            self.last_node = node
        else:
            self.head_node = node
            self.last_node = self.head_node

    def app_start(self, node):
        if not self.is_empty():
            node.modifyNextNode(self.head_node)
            self.head_node = node
        else:
            self.head_node = node
            self.last_node = self.head_node

    def insert(self, index, node):
        if index < 0 or index > (self.length() - 1):
            return
        elif index == 0:
            self.app_start(node)
        else:
            node_pointer1 = self.getNode(index - 1)
            node_pointer2 = self.getNode(index)
            node.modifyNextNode(node_pointer2)
            node_pointer1.modifyNextNode(node)

    def pop(self, index):
        if self.is_empty():
            return
        if index < -1 or (-1 < index < 0) or index > (self.length() - 1):
            return
        elif index == 0:
            node_pointer = self.getNode(index + 1)
            node_pointer2 = self.getNode(index)
            self.head_node.modifyNextNode(None)
            self.head_node = node_pointer
            return node_pointer2
        elif index == -1:
            node_pointer1 = self.getNode(self.length() - 2)
            node_pointer2 = node_pointer1.getNextNode()
            node_pointer1.modifyNextNode(None)
            self.last_node = node_pointer1
            return node_pointer2
        else:
            node_pointer1 = self.getNode(index - 1)
            node_pointer2 = self.getNode(index)
            node_pointer3 = self.getNode(index + 1)
            node_pointer1.modifyNextNode(node_pointer3)
            node_pointer2.modifyNextNode(None)
            return node_pointer2

    def printAll(self):
        print("------------------------")
        print("whole linked list:", end=" ")
        print(self)
        print("node's number = {0}".format(self.length()))
        print("nodes:")
        print("# head")
        if not self.is_empty():
            node_pointer = self.head_node
            count = 1
            while node_pointer is not None:
                print("#{0} [{1}]: {2}".format(count, count - 1, node_pointer))
                node_pointer = node_pointer.getNextNode()
                count += 1
        print("# end")
        print("------------------------")


class Traveller:
    def __init__(self, node: Node or None):
        self.init = node
        self.cur = node

    def getCur(self):
        return self.cur

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.cur
        if tmp:
            self.cur = self.cur.getNextNode()
            return tmp
        self.cur = self.init
        raise StopIteration


if __name__ == "__main__":
    nodes1 = [10, 6, 9, 1, 3, 7]
    l1 = LinkedList()
    for num in nodes1:
        l1.app_end(Node(num))
    print(l1)
    print(l1.getNode(2))
    print(l1.getNode(3))
    print(l1.getIndex(Node(1)))
    for mem in l1:
        print(mem)
