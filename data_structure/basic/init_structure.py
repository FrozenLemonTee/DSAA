import random
from typing import List

from DSAA.data_structure.basic.node import Node
from DSAA.data_structure.basic.LinkedList import LinkedList
from DSAA.data_structure.basic.TreeNode import TreeNode
from DSAA.data_structure.basic.binaryTree import BinaryTree


def initializeLinkedList(num=0):
    linked_list = LinkedList()
    for i in range(0, num):
        linked_list.app_end(Node(random.randint(0, num)))
    return linked_list


def initList(nodes: List[int] or None):
    linked_list = LinkedList()
    for node in nodes:
        linked_list.app_end(Node(node))
    return linked_list


def initializeBinaryTree(num=0):
    tree = BinaryTree()
    for i in range(0, num):
        tree.app(TreeNode(random.randint(0, num)))
    return tree
