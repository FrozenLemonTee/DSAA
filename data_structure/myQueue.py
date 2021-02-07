from DSAA.data_structure.basic.node import Node
from DSAA.data_structure.basic.LinkedList import LinkedList


class myQueue(LinkedList):
    def app(self, node):
        self.last_node.modifyNextNode(node)
        self.last_node = node

    def pop(self):
        if not self.is_empty():
            node_pointer = self.head_node.getNextNode()
            self.head_node.modifyNextNode(None)
            self.head_node = node_pointer
        return

    def printAll(self):
        print("------------------------")
        print("whole queue:", end=" ")
        print(self)
        print("node's number = {0}".format(self.length()))
        print("nodes:")
        print("# head")
        if self.is_empty():
            print("# end")
        else:
            node_pointer = self.head_node
            count = 1
            while node_pointer is not None:
                print("#{0}: {1}".format(count, node_pointer))
                node_pointer = node_pointer.getNextNode()
                count += 1
            print("# end")
        print("------------------------")


if __name__ == "__main__":
    node1 = Node(15)
    node2 = Node(7)
    node3 = Node(22)
    node4 = Node(30)
    node5 = Node(88)
    node6 = Node(94)
    queue = myQueue(node1)
    queue.app(node2)
    queue.app(node3)
    queue.app(node4)
    queue.app(node5)
    queue.app(node6)
    queue.printAll()
    print(queue.getNode(1), queue.getNode(3))
    queue.pop()
    queue.pop()
    queue.printAll()
