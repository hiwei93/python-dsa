from typing import Optional


class ArrayStack(object):
    """
    顺序栈
    """
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__count = 0
        self.__items = [None] * capacity  # 模拟空间申请

    def __repr__(self):
        return str(self.__items)

    def push(self, item: int) -> bool:
        """
        时间复杂度: O(1)
        """
        if self.__capacity == self.__count:
            return False
        self.__items[self.__count] = item
        self.__count += 1
        return True

    def pop(self):
        """
        时间复杂度: O(1)
        """
        if self.__count == 0:
            return None
        item = self.__items[self.__count - 1]
        self.__count -= 1
        return item


class DynamicArrayStack(object):
    """
    动态扩、缩容的顺序栈
    """
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__count = 0
        self.__items = [None] * capacity  # 模拟空间申请
        self.__factor = 2

    def __repr__(self):
        return str(self.__items)

    def __len__(self):
        return self.__count

    @property
    def capacity(self):
        return self.__capacity

    def __extend(self):
        """
        扩容
        """
        capacity = self.__capacity * self.__factor
        new_items = [None] * capacity
        for i in range(self.__count):
            new_items[i] = self.__items[i]
        self.__items = new_items
        self.__capacity = capacity

    def push(self, item: int):
        if self.__capacity == self.__count:
            self.__extend()
        self.__items[self.__count] = item
        self.__count += 1
        return True

    def __reduce(self):
        """
        缩容
        """
        capacity = self.__count
        new_items = [None] * capacity
        for i in range(self.__count):
            new_items[i] = self.__items[i]
        self.__items = new_items
        self.__capacity = capacity

    def pop(self):
        if self.__count == 0:
            return None
        item = self.__items[self.__count - 1]
        self.__count -= 1
        if self.__capacity / self.__count == self.__factor:
            self.__reduce()
        return item


class Node(object):
    def __init__(self, data: Optional[int] = None, next: Optional['Node'] = None):
        self.data = data
        self.next = next


class LinkedListStack(object):
    """
    链式栈的实现
    """
    def __init__(self):
        self.__top = None
        self.__size = 0

    def __iter__(self):
        p = self.__top
        while p:
            yield p.data
            p = p.next

    def __repr__(self):
        return " -> ".join((str(i) for i in self))

    def __len__(self):
        return self.__size

    def push(self, item: int):
        new_node = Node(item, self.__top)
        self.__top = new_node
        self.__size += 1

    def pop(self):
        if not self.__top:
            return None
        item = self.__top.data
        self.__top = self.__top.next
        self.__size -= 1
        return item
