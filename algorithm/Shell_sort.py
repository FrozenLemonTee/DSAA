import time

from DSAA.algorithm.Nodes_changing import changeNode
from DSAA.algorithm.Insert_sort import _insertSort
from DSAA.data_structure.basic.init_structure import initializeLinkedList


# 希尔排序： 加强型插入排序
def shellSort(my_linked_list):
    if my_linked_list.length() == 0 or my_linked_list.length() == 1:
        pass
    elif my_linked_list.length() == 2:
        if my_linked_list.head_node.getData() > my_linked_list.last_node.getData():
            changeNode(my_linked_list, 0, 1)
    else:
        gap = my_linked_list.length() // 2
        while gap >= 1:
            for i in range(gap, my_linked_list.length()):
                _insertSort(my_linked_list, i, gap)
            gap = gap // 2


if __name__ == "__main__":
    start = time.perf_counter()
    linkedList = initializeLinkedList(400)
    print("希尔排序前：")
    linkedList.printAll()
    shellSort(linkedList)
    print("希尔排序后：")
    linkedList.printAll()
    end = time.perf_counter()
    print("用时{0}秒.".format(end - start))
    pass
