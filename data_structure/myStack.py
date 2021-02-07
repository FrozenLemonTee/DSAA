from DSAA.data_structure.basic.node import Node
from DSAA.data_structure.basic.LinkedList import LinkedList
import random
from time import sleep


class myStack(LinkedList):
    def push(self, node):
        if not self.is_empty():
            self.last_node.modifyNextNode(node)
            self.last_node = node
        else:
            self.head_node = node
            self.last_node = self.head_node

    def pop(self):
        if not self.is_empty() and self.length() > 1:
            node_pointer1 = self.getNode(self.length() - 2)
            node_pointer2 = node_pointer1.getNextNode()
            node_pointer1.modifyNextNode(None)
            self.last_node = node_pointer1
            return node_pointer2
        elif self.length() == 1:
            node_pointer = self.head_node
            self.head_node = None
            self.last_node = self.head_node
            return node_pointer
        else:
            return

    def printAll(self):
        print("------------------------")
        print("whole stack:", end=" ")
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
    stack1 = myStack()
    stack2 = myStack()
    for i in range(0, 30):
        stack1.push(Node(random.randint(0, 50)))
        print(stack1)
        sleep(0.5)
    for j in range(0, 30):
        stack2.push(stack1.pop())
        print(stack1)
        sleep(0.5)
    stack2.printAll()
