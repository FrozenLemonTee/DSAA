from DSAA.data_structure.basic.init_structure import initializeLinkedList
from DSAA.algorithm.Nodes_changing import exchangeNode
import time


def bubbleSort(my_linked_list):
    if my_linked_list.length() == 0 or my_linked_list.length() == 1:
        pass
    elif my_linked_list.length() == 2:
        if my_linked_list.head_node.getData() > my_linked_list.last_node.getData():
            exchangeNode(my_linked_list, 0)
    else:
        for i in range(0, my_linked_list.length()):
            for j in range(0, my_linked_list.length() - 1 - i):
                if my_linked_list.getNode(j).getData() > my_linked_list.getNode(j + 1).getData():
                    exchangeNode(my_linked_list, j)


if __name__ == "__main__":
    start = time.perf_counter()
    linked_list = initializeLinkedList(1000)
    print("冒泡排序前：")
    linked_list.printAll()
    bubbleSort(linked_list)
    print("冒泡排序后：")
    linked_list.printAll()
    end = time.perf_counter()
    print("用时{0}秒.".format(end - start))
    pass
