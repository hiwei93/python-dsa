"""
链表实现
- LRU 缓存
"""


class Node():
    def __init__(self, data: int, next: 'Node' = None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: int):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node: 'Node'):
        self.__next = next_node


class LinkedList(object):
    """
    实现方法：
    1. 头部插入节点
    2. 末尾插入节点
    3. 某个节点后插入
    4. 某个节点前插入
    5. 删除某个节点
    6. 根据致值查找
    7. 寻秩查找
    """
    def __init__(self):
        self.__head = None

    def __iter__(self):
        node = self.__head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return " -> ".join((str(i) for i in self))

    def insert_value_to_head(self, value: int):
        node = Node(value)
        self.insert_node_to_head(node)

    def insert_node_to_head(self, node: Node):
        if self.__head is None:
            self.__head = node
            return
        node.next = self.__head
        self.__head = node

    def insert_value_to_tail(self, value: int):
        node = Node(value)
        self.insert_node_to_tail(node)

    def insert_node_to_tail(self, node: Node):
        if self.__head is None:
            self.__head = node
            return

        p = self.__head
        while p.next is not None:
            p = p.next
        p.next = node

    def insert_value_after(self, node: Node, value: int) -> bool:
        new_node = Node(value)
        return self.insert_node_after(node, new_node)

    def insert_node_after(self, node: Node, new_node: Node) -> bool:
        if not node or not new_node:
            return False
        if not self.find_node(node):
            return False
        new_node.next = node.next
        node.next = new_node
        return True

    def insert_value_before(self, node: Node, value: int) -> bool:
        new_node = Node(value)
        return self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node) -> bool:
        if not node or not new_node:
            return False
        if node == self.__head:
            self.insert_node_to_head(new_node)
            return True
        p = self.__head
        while p and p.next != node:
            p = p.next
        if not p:
            return False
        new_node.next = p.next
        p.next = new_node
        return True

    def find_node(self, node: Node):
        p = self.__head
        while p:
            if p == node:
                return True
            p = p.next
        return False

    def delete_by_value(self, value: int) -> bool:
        if not self.__head:
            return False
        p, q = self.__head, None
        while p and p.data != value:
            q = p
            p = p.next
        if not p:
            return False
        q.next = q.next.next
        return True

    def delete_by_node(self, node: Node) -> bool:
        if not self.__head or not node:
            return False
        if node == self.__head:
            self.__head = node.next
            return True
        p = self.__head
        while p and p.next != node:
            p = p.next
        if not p:
            return False
        p.next = node.next
        return True

    def find_by_value(self, value: int) -> Node:
        p = self.__head
        while p and p.data != value:
            p = p.next
        return p

    def find_by_index(self, index: int) -> Node:
        p = self.__head
        position = 0
        while p and position != index:
            p = p.next
            position = position + 1
        return p

