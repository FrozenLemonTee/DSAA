from DSAA.data_structure.basic.LinkedList import LinkedList
from DSAA.data_structure.basic.node import Node


# 交换链表中任意两个节点，注意分类讨论，前后两个index是/不是头（尾）节点指针，共有2*2=4种情况
def changeNode(my_linked_list, index1, index2):
    if index1 == index2:
        return
    node_pointer1 = my_linked_list.getNode(index1)
    node_pointer2 = my_linked_list.getNode(index2)
    if node_pointer1 is my_linked_list.head_node and node_pointer2 is my_linked_list.last_node:
        pre_pointer2 = my_linked_list.getNode(index2 - 1)
        node_pointer2.modifyNextNode(node_pointer1.getNextNode())
        node_pointer1.modifyNextNode(None)
        pre_pointer2.modifyNextNode(node_pointer1)
        my_linked_list.head_node = node_pointer2
        my_linked_list.last_node = node_pointer1
    elif node_pointer1 is not my_linked_list.head_node and node_pointer2 is my_linked_list.last_node:
        pre_pointer1 = my_linked_list.getNode(index1 - 1)
        pre_pointer2 = my_linked_list.getNode(index2 - 1)
        node_pointer2.modifyNextNode(node_pointer1.getNextNode())
        pre_pointer1.modifyNextNode(node_pointer2)
        pre_pointer2.modifyNextNode(node_pointer1)
        node_pointer1.modifyNextNode(None)
        my_linked_list.last_node = node_pointer1
    elif node_pointer1 is my_linked_list.head_node and node_pointer2 is not my_linked_list.last_node:
        pre_pointer2 = my_linked_list.getNode(index2 - 1)
        pro_pointer1 = my_linked_list.getNode(index1 + 1)
        node_pointer1.modifyNextNode(node_pointer2.getNextNode())
        pre_pointer2.modifyNextNode(node_pointer1)
        node_pointer2.modifyNextNode(pro_pointer1)
        my_linked_list.head_node = node_pointer1
    else:
        pre_pointer1 = my_linked_list.getNode(index1 - 1)
        pre_pointer2 = my_linked_list.getNode(index2 - 1)
        pro_pointer2 = my_linked_list.getNode(index2 + 1)
        node_pointer2.modifyNextNode(node_pointer1.getNextNode())
        node_pointer1.modifyNextNode(pro_pointer2)
        pre_pointer1.modifyNextNode(node_pointer2)
        pre_pointer2.modifyNextNode(node_pointer1)


def quickSort(my_linked_list, index_left, index_right):
    if index_left >= index_right:
        return
    node_pointer = my_linked_list.getNode(index_left)
    mid_node = Node(node_pointer.getData())
    left = index_left
    right = index_right
    while left < right:
        while my_linked_list.getNode(right).getData() >= mid_node.getData() and left < right:
            right -= 1
        if left < right:
            changeNode(my_linked_list, left, right)
        else:
            break
        while my_linked_list.getNode(left).getData() < mid_node.getData() and left < right:
            left += 1
        if left < right:
            changeNode(my_linked_list, left, right)
        else:
            break
    if my_linked_list.getNode(left) is my_linked_list.head_node:
        my_linked_list.pop(0)
        my_linked_list.app_start(mid_node)
        my_linked_list.head_node = mid_node
    elif my_linked_list.getNode(left) is my_linked_list.last_node:
        my_linked_list.pop(-1)
        my_linked_list.app_end(mid_node)
        my_linked_list.last_node = mid_node
    else:
        my_linked_list.pop(left)
        my_linked_list.insert(left, mid_node)
    if index_left < index_right:
        quickSort(my_linked_list, index_left, left - 1)
        quickSort(my_linked_list, left + 1, index_right)


if __name__ == "__main__":
    # node1 = Node(125)
    # node2 = Node(70)
    # node3 = Node(52)
    # node4 = Node(30)
    # node5 = Node(88)
    # node6 = Node(94)
    # node7 = Node(70)
    # linked_list = LinkedList(node=node1)
    # linked_list.app_end(node2)
    # linked_list.app_end(node3)
    # linked_list.app_end(node4)
    # linked_list.app_end(node5)
    # linked_list.app_end(node6)
    # linked_list.app_end(node7)
    # print("快速排序前：")
    # linked_list.printAll()
    # quickSort(linked_list, 0, linked_list.length() - 1)
    # print("快速排序后：")
    # linked_list.printAll()
    pass
