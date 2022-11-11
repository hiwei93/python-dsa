class CircularDequeArray:
    """
    实现双端循环队列 (数组方式)
    https://leetcode.cn/problems/design-circular-deque
    """
    def __init__(self, k: int):
        self.k = k
        self.items = [None] * k
        self.size = 0
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.k) % self.k
        self.items[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        last = (self.tail - 1 + self.k) % self.k
        return self.items[last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


class Node:
    def __init__(self, data: int, pre: 'Node' = None, next: 'Node' = None):
        self.data = data
        self.pre = pre
        self.next = next


class CircularDequeLinkedList():
    """
    实现双端循环队列 (双向链表)
    """
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        p = self.head
        while p:
            yield p.data
            if p == self.tail:
                break
            p = p.next

    def __str__(self):
        return str([i for i in self])

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.pre = new_node
        self.tail.next = new_node
        new_node.pre = self.tail
        self.head = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.pre = self.tail
        self.head.pre = new_node
        new_node.next = self.head
        self.tail = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 0:
            self.head = None
            self.tail = None
            return True
        self.head.pre.next = self.head.next
        self.head.next.pre = self.head.pre
        self.head = self.tail.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 0:
            self.head = None
            self.tail = None
            return True
        self.tail.pre.next = self.tail.next
        self.tail.next.pre = self.tail.pre
        self.tail = self.head.pre
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.data

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.data

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
