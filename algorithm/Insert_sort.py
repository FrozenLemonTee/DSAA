import time

from DSAA.data_structure.basic.init_structure import initializeLinkedList
from DSAA.algorithm.Nodes_changing import exchangeNode


def _insertSort(my_linked_list, index, gap):
    """ gap的值不定，切割为子链表分别排序，index为子链表第二处索引 """
    if my_linked_list.length() == 0 or my_linked_list.length() == 1:
        pass
    elif my_linked_list.length() == 2:
        if my_linked_list.head_node.getData() > my_linked_list.last_node.getData():
            exchangeNode(my_linked_list, 0)
    else:
        for i in range(index, my_linked_list.length(), gap):
            j = i
            while j >= index:
                node_pointer1 = my_linked_list.getNode(j)
                node_pointer2 = my_linked_list.getNode(j - gap)
                if node_pointer1.getData() < node_pointer2.getData():
                    exchangeNode(my_linked_list, j - gap)
                    j -= gap
                else:
                    break


def insertSort1(my_linked_list):
    """ 链表视为一个整体，gap = 1 """
    if my_linked_list.length() == 0 or my_linked_list.length() == 1:
        pass
    elif my_linked_list.length() == 2:
        if my_linked_list.head_node.getData() > my_linked_list.last_node.getData():
            exchangeNode(my_linked_list, 0)
    else:
        for i in range(1, my_linked_list.length()):
            j = i
            while j >= 1:
                node_pointer1 = my_linked_list.getNode(j)
                node_pointer2 = my_linked_list.getNode(j - 1)
                if node_pointer1.getData() < node_pointer2.getData():
                    exchangeNode(my_linked_list, j - 1)
                    j -= 1
                else:
                    break


def insertSort(my_linked_list):
    """方法入口"""
    _insertSort(my_linked_list, 1, 1)


if __name__ == "__main__":
    start = time.perf_counter()
    linked_list = initializeLinkedList(1000)
    print("插入排序前：")
    linked_list.printAll()
    insertSort(linked_list)
    print("插入排序后：")
    linked_list.printAll()
    end = time.perf_counter()
    print("用时{0}秒.".format(end - start))
    pass
