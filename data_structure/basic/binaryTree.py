from random import randint
from DSAA.data_structure.basic.TreeNode import TreeNode
import time


class BinaryTree:
    def __init__(self, node=None):
        self.root_node = node
        if node is None:
            self._count = 0
        else:
            self._count = 1

    # 遍历时调用辅助私有方法self._children_tree()递归，深度优先遍历（先序）
    def __repr__(self):
        info = ""
        node_pointer = self.root_node
        if node_pointer is not None:
            info += str(node_pointer)
            info += "\n"
            node_pointer = self.root_node.getLeftNode()
            info += self._children_tree(node_pointer)
            node_pointer = self.root_node.getRightNode()
            info += self._children_tree(node_pointer)
        else:
            info += "None"
        return info

    def is_empty(self):
        return self._count == 0

    def getNodesNumber(self):
        return self._count

    def _children_tree(self, root):
        info = ""
        node_pointer = root
        if node_pointer is not None:
            info += str(node_pointer)
            info += "\n"
            node_pointer = root.getLeftNode()
            info += self._children_tree(node_pointer)
            node_pointer = root.getRightNode()
            info += self._children_tree(node_pointer)
        return info

    def app(self, node):
        data = node.getData()
        node_pointer1 = self.root_node
        node_pointer2 = node_pointer1
        if self.is_empty():
            self.root_node = node
            self._count += 1
            return
        else:
            while node_pointer1 is not None:
                if data < node_pointer1.getData():
                    node_pointer2 = node_pointer1
                    node_pointer1 = node_pointer1.getLeftNode()
                else:
                    node_pointer2 = node_pointer1
                    node_pointer1 = node_pointer1.getRightNode()
        if node_pointer2.getLeftNode() is node_pointer1:
            node_pointer2.modifyLeftNode(node)
        else:
            node_pointer2.modifyRightNode(node)
        self._count += 1

    def findNode(self, data):
        if not self.is_empty():
            node_pointer1 = self.root_node
            while node_pointer1 is not None:
                if data < node_pointer1.getData():
                    node_pointer1 = node_pointer1.getLeftNode()
                elif data > node_pointer1.getData():
                    node_pointer1 = node_pointer1.getRightNode()
                else:
                    return node_pointer1
        print("There is no node whose data is {0}!".format(data))
        return

    def printAll(self):
        print("------------------------")
        print("node's number = {0}".format(self.getNodesNumber()))
        print("whole binary tree:")
        print()
        print(self)
        print("------------------------")


if __name__ == "__main__":
    start = time.perf_counter()
    tree = BinaryTree()
    for i in range(0, 10000):
        tree.app(TreeNode(randint(0, 1000)))
    tree.printAll()
    end = time.perf_counter()
    print("用时{0}秒".format(end - start))
