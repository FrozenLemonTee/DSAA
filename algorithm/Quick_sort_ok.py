import time

from DSAA.data_structure.basic.init_structure import initializeLinkedList
from DSAA.data_structure.basic.node import Node
from DSAA.algorithm.Nodes_changing import changeNode


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
        if left == right:
            mid_node = node_pointer
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
    start = time.perf_counter()
    linked_list = initializeLinkedList(300)
    print("快速排序前：")
    linked_list.printAll()
    quickSort(linked_list, 0, linked_list.length() - 1)
    print("快速排序后：")
    linked_list.printAll()
    end = time.perf_counter()
    print("用时{0}秒.".format(end - start))
    pass
