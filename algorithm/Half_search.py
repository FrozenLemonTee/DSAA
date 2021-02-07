from DSAA.algorithm.Merge_sort import mergeSort
from DSAA.data_structure.basic.init_structure import initializeLinkedList
import time


# 要求传入的链表是有序的
def halfSearch(my_linked_list, number):
    node_pointer1 = my_linked_list.head_node
    node_pointer2 = my_linked_list.last_node
    if my_linked_list.is_empty():
        return -1
    else:
        if number < node_pointer1.getData() or number > node_pointer2.getData():
            return -1
        else:
            low = 0
            high = my_linked_list.length() - 1
            while low <= high:
                mid = (low + high) // 2
                node_pointer3 = my_linked_list.getNode(mid)
                if node_pointer3.getData() > number:
                    high = mid - 1
                elif node_pointer3.getData() < number:
                    low = mid + 1
                else:
                    return mid
            return -1


if __name__ == "__main__":
    start1 = time.perf_counter()
    linkedList = initializeLinkedList(400)
    linkedList = mergeSort(linkedList)
    linkedList.printAll()
    end1 = time.perf_counter()
    print("用时{0}秒".format(end1 - start1))
    num = input("请输入要查询的值：")
    start2 = time.perf_counter()
    index = halfSearch(linkedList, int(num))
    print("索引为：", index)
    print("该节点信息：", linkedList.getNode(index))
    end2 = time.perf_counter()
    print("用时{0}秒".format(end2 - start2))
    pass
