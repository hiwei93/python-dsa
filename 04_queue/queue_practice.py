class CircularDequeArray:
    """
    实现双端队列 (数组方式)
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