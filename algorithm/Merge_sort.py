from DSAA.data_structure.basic.init_structure import initializeLinkedList
from DSAA.data_structure.basic.LinkedList import LinkedList
from DSAA.algorithm.Operations_between_lists import getFragment, combineList


# 归并排序： 递归 + 选择排序
def mergeSort(my_linked_list):
    length = my_linked_list.length()
    if length <= 1:
        return my_linked_list
    mid = length // 2
    cut1 = mergeSort(getFragment(my_linked_list, 0, mid - 1))
    cut2 = mergeSort(getFragment(my_linked_list, mid, my_linked_list.length() - 1))
    node_pointer1 = cut1.head_node
    node_pointer2 = cut2.head_node
    cut3 = LinkedList()
    while node_pointer1 is not None and node_pointer2 is not None:
        data1 = node_pointer1.getData()
        data2 = node_pointer2.getData()
        if data1 < data2:
            cut3.app_end(cut1.pop(cut1.getIndex(node_pointer1)))
            node_pointer1 = cut1.head_node
        else:
            cut3.app_end(cut2.pop(cut2.getIndex(node_pointer2)))
            node_pointer2 = cut2.head_node
    combineList(cut3, cut1)
    combineList(cut3, cut2)
    return cut3


if __name__ == "__main__":
    linklist = initializeLinkedList(50)
    linklist = mergeSort(linklist)
    print("排序后：")
    print(linklist)
    linklist.printAll()
    pass
