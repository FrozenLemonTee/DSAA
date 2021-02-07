# 交换链表中任意两个节点，注意分类讨论，前后两个index是/不是头（尾）节点指针，共有2*2=4种情况
def changeNode(my_linked_list, index1, index2):
    if index1 == index2:
        return
    if index2 < index1:
        index1, index2 = index2, index1
    if index2 - index1 == 1:
        exchangeNode(my_linked_list, index1)
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
        pointer1_next = my_linked_list.getNode(index1 + 1)  # pointer1_nextnode
        pointer2_next = my_linked_list.getNode(index2 + 1)  # pointer2_nextnode
        node_pointer2.modifyNextNode(pointer1_next)
        node_pointer1.modifyNextNode(pointer2_next)
        pre_pointer2.modifyNextNode(node_pointer1)
        my_linked_list.head_node = node_pointer2

        # 修改前：
        # pre_pointer2 = my_linked_list.findNode(index2 - 1)
        # pro_pointer1 = my_linked_list.findNode(index1 + 1)
        # node_pointer1.modifyNextNode(node_pointer2.getNextNode())
        # pre_pointer2.modifyNextNode(node_pointer1)
        # node_pointer2.modifyNextNode(pro_pointer1)
        # my_linked_list.head_node = node_pointer1
    else:
        pre_pointer1 = my_linked_list.getNode(index1 - 1)
        pre_pointer2 = my_linked_list.getNode(index2 - 1)
        pointer1_next = my_linked_list.getNode(index1 + 1)
        pointer2_next = my_linked_list.getNode(index2 + 1)
        node_pointer2.modifyNextNode(pointer1_next)
        node_pointer1.modifyNextNode(pointer2_next)
        pre_pointer1.modifyNextNode(node_pointer2)
        pre_pointer2.modifyNextNode(node_pointer1)


# 交换相邻两个节点
def exchangeNode(my_linked_list, index):
    node_pointer1 = my_linked_list.getNode(index)
    node_pointer2 = node_pointer1.getNextNode()
    if node_pointer1 is my_linked_list.head_node:
        node_pointer1.modifyNextNode(node_pointer2.getNextNode())
        node_pointer2.modifyNextNode(node_pointer1)
        my_linked_list.head_node = node_pointer2
    elif node_pointer2 is my_linked_list.last_node:
        node_pointer1.modifyNextNode(None)
        pre_pointer = my_linked_list.getNode(index - 1)
        node_pointer2.modifyNextNode(node_pointer1)
        pre_pointer.modifyNextNode(node_pointer2)
        my_linked_list.last_node = node_pointer1
    else:
        pre_pointer = my_linked_list.getNode(index - 1)
        node_pointer1.modifyNextNode(node_pointer2.getNextNode())
        node_pointer2.modifyNextNode(node_pointer1)
        pre_pointer.modifyNextNode(node_pointer2)
