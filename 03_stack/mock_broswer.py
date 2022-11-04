"""
编程模拟实现一个浏览器的前进、后退功能
解题：
1. 基于链式栈实现
"""


class Node:
    def __init__(self, data: str = None, next: 'Node' = None):
        self.data = data
        self.next = next


class LinkedListStack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __iter__(self):
        p = self.__top
        while p:
            yield p.data
            p = p.next

    def __repr__(self):
        return " -> ".join(self)

    def push(self, item: str):
        new_node = Node(item, self.__top)
        self.__top = new_node
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return None
        item = self.__top.data
        self.__top = self.__top.next
        self.__size -= 1
        return item

    def clear(self):
        self.__top = None
        self.__size = 0


class Browser:
    def __init__(self):
        self.__current_page = None
        self.__forward_stack = LinkedListStack()   # 用于 -> 按钮
        self.__backward_stack = LinkedListStack()  # 用于 <- 按钮

    def open(self, url):
        if self.__current_page:
            self.__backward_stack.push(self.__current_page)
            self.__forward_stack.clear()
        self.__current_page = url
        print(f"open page: {url}")

    def can_go_back(self):
        return len(self.__backward_stack) > 0

    def go_back(self):
        """
        点击 <- 按钮
        """
        if self.can_go_back():
            self.__forward_stack.push(self.__current_page)
            url = self.__backward_stack.pop()
            self.__current_page = url
            print(f"back to page: {url}")
            return url
        print("!!!can not go back, there are no pages behind")
        return None

    def can_go_forward(self):
        return len(self.__forward_stack) > 0

    def go_forward(self):
        """
        点击 -> 按钮
        """
        if self.can_go_forward():
            self.__backward_stack.push(self.__current_page)
            url = self.__forward_stack.pop()
            self.__current_page = url
            print(f"forward to page: {url}")
            return url
        print("!!!can not go forward, there are no pages ahead")
        return None

