from DSAA.data_structure.basic.node import Node
from DSAA.data_structure.basic.LinkedList import LinkedList
from DSAA.data_structure.basic.init_structure import initializeLinkedList


# 复制链表的切片，原链表没有被破坏
def getFragment(my_linked_list: LinkedList, index1: int, index2: int) -> LinkedList:
    if not my_linked_list.is_empty():
        if index1 == index2:
            return LinkedList(Node(my_linked_list.getNode(index1).getData()))
        if index2 < index1:
            index1, index2 = index2, index1
        node_pointer = my_linked_list.getNode(index1)
        fragment = LinkedList()
        while node_pointer is not my_linked_list.getNode(index2):
            fragment.app_end(Node(node_pointer.getData()))
            if node_pointer is my_linked_list.getNode(index2):
                break
            node_pointer = node_pointer.getNextNode()
        fragment.app_end(Node(node_pointer.getData()))
        return fragment
    else:
        return LinkedList()


# 将链表切为两个子链表(注意原链表在操作后已被破坏)，并且返回右侧链表，区间： 前[0,index]  后[index+1,length-1]
def cutList(my_linked_list: LinkedList, index: int) -> LinkedList:
    if index == -1:
        index = my_linked_list.length() - 1
    if index < -1 or index > my_linked_list.length() - 1:
        return LinkedList()
    if my_linked_list.is_empty():
        my_linked_list.head_node = None
        my_linked_list.last_node = my_linked_list.head_node
        return LinkedList()
    else:
        node_pointer1 = my_linked_list.getNode(index)
        the_list = getFragment(my_linked_list, index + 1, my_linked_list.length() - 1)
        my_linked_list.last_node = node_pointer1
        my_linked_list.last_node.modifyNextNode(None)
        return the_list


# 合并两个链表，将后者合并至前者
def combineList(mt_list1: LinkedList, my_list2: LinkedList):
    if mt_list1.is_empty() and my_list2.is_empty():
        my_list2.head_node = mt_list1.head_node
        my_list2.last_node = mt_list1.last_node
    elif mt_list1.is_empty() and not my_list2.is_empty():
        my_list = getFragment(my_list2, 0, my_list2.length() - 1)
        mt_list1.head_node = my_list.head_node
        mt_list1.last_node = my_list.last_node
        my_list2.head_node = mt_list1.head_node
        my_list2.last_node = mt_list1.last_node
    elif not mt_list1.is_empty() and my_list2.is_empty():
        my_list = getFragment(mt_list1, 0, mt_list1.length() - 1)
        mt_list1.head_node = my_list.head_node
        mt_list1.last_node = my_list.last_node
        my_list2.head_node = mt_list1.head_node
        my_list2.last_node = mt_list1.last_node
    else:
        mt_list1.last_node.modifyNextNode(my_list2.head_node)
        my_list2.head_node = mt_list1.head_node
        mt_list1.last_node = my_list2.last_node


# 覆盖链表的一部分，覆盖区间[index1,index2]
def coverFragment(covered_list: LinkedList, fragment: LinkedList, index1: int, index2: int):
    if index1 > index2:
        index1, index2 = index2, index1
    if index1 < 0 or index2 > covered_list.length() - 1:
        return
    length0 = covered_list.length()
    length = fragment.length()
    if length >= length0:
        covered_list.head_node = fragment.head_node
        covered_list.last_node = fragment.last_node
    else:
        if index1 == 0 and index2 != covered_list.length() - 1:
            cut1 = cutList(covered_list, index2)
            combineList(fragment, cut1)
            covered_list.head_node = fragment.head_node
            covered_list.last_node = fragment.last_node
        elif index1 != 0 and index2 == covered_list.length() - 1:
            cutList(covered_list, index1 - 1)
            combineList(covered_list, fragment)
        elif index1 == 0 and index2 == covered_list.length() - 1:
            covered_list.head_node = fragment.head_node
            covered_list.last_node = fragment.last_node
        else:
            cut1 = cutList(covered_list, index1 - 1)
            cut2 = cutList(cut1, index2 - covered_list.length())
            combineList(covered_list, fragment)
            combineList(covered_list, cut2)


# 全加器
def _fullAdder(node_pointer1: Node, node_pointer2: Node, carry: int, result_list: LinkedList) -> int:
    summary = 0
    if node_pointer1:
        summary += node_pointer1.getData()
    if node_pointer2:
        summary += node_pointer2.getData()
    summary += carry
    result_list.app_end(Node(summary % 10))
    if summary > 9:
        carry = 1
    else:
        carry = 0
    return carry


# 将两个链表相加(小端存储)
def plusLinkedList(my_list1: LinkedList, my_list2: LinkedList) -> LinkedList:
    if my_list1.is_empty():
        return getFragment(my_list2, 0, my_list2.length() - 1)
    if my_list2.is_empty():
        return getFragment(my_list1, 0, my_list1.length() - 1)
    list3 = LinkedList()
    node_pointer1 = my_list1.head_node
    node_pointer2 = my_list2.head_node
    carry = _fullAdder(node_pointer1, node_pointer2, 0, list3)
    node_pointer1 = node_pointer1.getNextNode()
    node_pointer2 = node_pointer2.getNextNode()
    while True:
        carry = _fullAdder(node_pointer1, node_pointer2, carry, list3)
        if node_pointer1:
            node_pointer1 = node_pointer1.getNextNode()
        if node_pointer2:
            node_pointer2 = node_pointer2.getNextNode()
        if not node_pointer1 and not node_pointer2:
            break
    return list3


# 将一个链表与一位数相乘，返回一个新链表
def _multiplyWithSingleDigit(the_list: LinkedList, num: int) -> LinkedList:
    if num == 0:
        return LinkedList(Node(0))
    else:
        result = LinkedList()
        node_pointer = the_list.head_node
        tmp = node_pointer.getData() * num
        result.app_end(Node(tmp % 10))
        if tmp > 9:
            carry = tmp // 10
        else:
            carry = 0
        node_pointer = node_pointer.getNextNode()
        while True:
            if not node_pointer:
                if carry > 0:
                    result.app_end(Node(carry))
                break
            else:
                tmp = node_pointer.getData() * num + carry
                result.app_end(Node(tmp % 10))
                if tmp > 9:
                    carry = tmp // 10
                else:
                    carry = 0
            if node_pointer:
                node_pointer = node_pointer.getNextNode()
    return result


# 将两个链表相乘，返回一个新链表
def multiplyLinkedList(the_list1: LinkedList, the_list2: LinkedList) -> LinkedList:
    if the_list1.length() < the_list2.length():
        my_list1 = the_list2
        my_list2 = getFragment(the_list1, 0, the_list1.length() - 1)
    else:
        my_list1 = the_list1
        my_list2 = getFragment(the_list2, 0, the_list2.length() - 1)
    node_pointer2 = my_list2.head_node
    result = _multiplyWithSingleDigit(my_list1, node_pointer2.getData())
    index = 0
    while node_pointer2.getNextNode():
        node_pointer2 = node_pointer2.getNextNode()
        index += 1
        temp = _multiplyWithSingleDigit(my_list1, node_pointer2.getData())
        for i in range(0, index):
            temp.app_start(Node(0))
        result = plusLinkedList(result, temp)
    return result


if __name__ == "__main__":
    list1 = initializeLinkedList(6)
    print(list1)
    print("*")
    list2 = initializeLinkedList(7)
    print(list2)
    print("=")
    print(multiplyLinkedList(list1, list2))
    pass
