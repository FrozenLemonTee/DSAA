class TreeNode:
    def __init__(self, data, node1=None, node2=None):
        self.data = data
        self.left_node = node1
        self.right_node = node2

    def __repr__(self):
        result = "({0}, #{1})\n".format(self.data, id(self))
        if self.left_node is None:
            result += "left: -> None\n"
        else:
            result += "left: -> #{0}\n".format(id(self.left_node))
        if self.right_node is None:
            result += "right: -> None\n"
        else:
            result += "right: -> #{0}\n".format(id(self.right_node))
        return result

    def getData(self):
        return self.data

    def getLeftNode(self):
        return self.left_node

    def getRightNode(self):
        return self.right_node

    def modifyLeftNode(self, node):
        self.left_node = node

    def modifyRightNode(self, node):
        self.right_node = node


if __name__ == "__main__":
    t_node1 = TreeNode(20)
    t_node2 = TreeNode(35, t_node1)
    print(t_node1)
    print(t_node2)
