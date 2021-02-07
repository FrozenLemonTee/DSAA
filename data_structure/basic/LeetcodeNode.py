from typing import List


class ListNode:
    def __init__(self, val=0, the_next=None):
        self.next = None
        self.val = val

        self.next = the_next

    def __repr__(self):
        if not self:
            return "None"
        else:
            info = ""
            node_pointer = self
            while node_pointer:
                info += "({0}, #{1}) -> ".format(node_pointer.val, id(node_pointer))
                if not node_pointer.next:
                    info += "None"
                node_pointer = node_pointer.next
        return info


class RNode:
    def __init__(self, x: int, the_next=None, random=None):
        self.val = int(x)
        self.next = the_next
        self.random = random

    def __repr__(self):
        if not self:
            return "None"
        else:
            info = ""
            node_pointer = self
            while node_pointer:
                info += "({0}, -> #{1}, #{2}) -> ".format(node_pointer.val, id(node_pointer.random) if node_pointer.random else "None", id(node_pointer))
                if not node_pointer.next:
                    info += "None"
                node_pointer = node_pointer.next
        return info


class DoubleListNode(ListNode):
    def __init__(self, val, prev_node=None, next_node=None, child=None):
        super().__init__(val)
        self.val = val
        self.prev = prev_node
        self.next = next_node
        self.child = child

    def __repr__(self):
        if not self:
            return "None"
        else:
            info = ""
            node_pointer = self
            while node_pointer:
                info += "({0}, id=#{1}, child={2}) <-> ".format(node_pointer.val, id(node_pointer),
                                                                bool(node_pointer.child))
                if not node_pointer.next:
                    info += "None"
                node_pointer = node_pointer.next
        return info


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "(#{0}, val={1}, left={2}, right={3})".format(id(self), self.val, self.left.val if self.left else "None",
                                                             self.right.val if self.right else "None")


class KTreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        children = []
        if self.children:
            for child in self.children:
                children.append(child.val)
        return "(#{0}, val={1}, children={2})".format(id(self), self.val, children)


class PTreeNode:
    def __init__(self, val=0, left=None, right=None, next_node=None):
        self.val = val
        self.left = left
        self.right = right
        self.next_node = next_node

    def __repr__(self):
        return "(#{0}, val={1}, left={2}, right={3}, next={4})".format(id(self), self.val,
                                                                       self.left.val if self.left else "None",
                                                                       self.right.val if self.right else "None",
                                                                       self.next_node.val if self.next_node else "None")


"""静态方法"""


def turnIntoList(nums: List[int] or None) -> ListNode or None:
    dummy = ListNode(-1)
    pointer = dummy
    if nums:
        for num in nums:
            pointer.next = ListNode(num)
            pointer = pointer.next
    return dummy.next


def initRList(nums: List[int] or None) -> RNode or None:
    dummy = RNode(-1)
    pointer = dummy
    nodes = []
    if nums:
        for num in nums:
            q = RNode(num)
            pointer.next = q
            nodes.append(q)
            pointer = pointer.next
        for i in range(0, len(nodes)):
            nodes[i].random = nodes[(i + len(nodes) // 2) % len(nodes)]
        return nodes[0]
