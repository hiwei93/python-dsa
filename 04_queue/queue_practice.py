from typing import List
import collections


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


class SlidingWindowMaximum():
    """
    https://leetcode.cn/problems/sliding-window-maximum
    """
    @staticmethod
    def solution(nums: List[int], k: int) -> List[int]:
        """
        使用双端队列实现单调队列结题
        - 时间复杂度：O(n)
        - 空间复杂度：O(k), 因为 q 最多存 K+1 个值，eg: `nums=[5,4,3,2,1]`,  `k=3`
        TODO：理解不够深入，需要重新实现
        总结：
        - 获取局部最值，会用到单调线性数据结构（单调栈、单调队列）
            - 单调栈相关题目：https://leetcode.cn/problems/next-greater-element-i
        """
        q = collections.deque()
        n = len(nums)
        # 初始化，找到第一个滑块的最大值
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:  # 因为有滑块和q中存储位置，所以必须为 >=，元素相等，需要更新位置信息
                q.pop()
            q.append(i)

        result = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:  # 因为有滑块和q中存储位置，所以必须为 >=，元素相等，需要更新位置信息
                q.pop()
            q.append(i)
            while q[0] <= i - k: # 保证q中存储的是滑块范围内的最大值
                q.popleft()
            result.append(nums[q[0]])
        return result


class MyCircularQueueByArray:
    """
    622. 设计循环队列 - 数组方式实现
    https://leetcode.cn/problems/design-circular-queue
    """
    def __init__(self, k: int):
        self.capacity = k
        self.items = [None] * k 
        self.head = self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        last = (self.tail - 1 + self.capacity) % self.capacity
        return self.items[last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyCircularQueueByLinkedList:
    """
    622. 设计循环队列 - 链表方式实现
    """
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = LinkedNode(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
