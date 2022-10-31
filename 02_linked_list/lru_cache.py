from typing import Tuple


class CacheNode:
    def __init__(self, key: int, data: int, next: 'CacheNode' = None):
        self.key = key
        self.data = data
        self.next = next


class LRUCache:
    """
    最近最少使用策略 LRU（Least Recently Used）
    - 单链表实现
    """
    def __init__(self, capacity: int):
        self.__capacity: int = capacity
        self.__head: CacheNode = None
        self.__length: int = 0

    def __iter__(self):
        p = self.__head
        while p:
            yield (p.key, p.data)
            p = p.next

    def __repr__(self):
        values = (str(item) for item in self)
        return " -> ".join(values)

    def __move_node_to_head(self, node: CacheNode, pre: CacheNode):
        if self.__length < 2:
            return
        pre.next = node.next
        node.next = self.__head
        self.__head = node

    def __find_node_by_key(self, key: int) -> Tuple[CacheNode, CacheNode]:
        """
        @return (target_node, pre_node)
        """
        if self.__head is None:
            return None
        p, q = self.__head, None
        while p and p.key != key:
            q = p
            p = p.next
        if not p:
            return None
        return p, q

    def get(self, key: int):
        """
        时间复杂度：O(n)
        """
        result = self.__find_node_by_key(key)
        if result is None:
            return None
        cur, pre = result
        data = cur.data
        if pre:  # pre 为空，则cur为根节点
            self.__move_node_to_head(cur, pre)
        return data

    def __delete_last_node(self):
        if self.__length == 1:
            self.__head = None
            self.__length = 0
            return
        p, q = self.__head, None
        while p.next is not None:
            q = p
            p = p.next
        q.next = None
        self.__length -= 1

    def put(self, key: int, value: int):
        """
        时间复杂度O(n)
        """
        result = self.__find_node_by_key(key)
        if result:  # 已经存在
            cur, pre = result
            cur.data = value
            self.__move_node_to_head(cur, pre)
            return
        # 不存在
        new_node = CacheNode(key, value)
        if self.__length == self.__capacity:  # 空间已满
            self.__delete_last_node()
        new_node.next = self.__head
        self.__head = new_node
        self.__length += 1
