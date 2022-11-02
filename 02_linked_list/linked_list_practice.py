"""
链表练习题
1. 删除链表的倒数第 N 个结点
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        p = self
        while p:
            yield p.val
            p = p.next

    def __repr__(self):
        items = (str(i) for i in self)
        return ' -> '.join(items)


def init_list(elems):
    head = ListNode(None, None)
    p = head
    for elem in elems:
        p.next = ListNode(elem)
        p = p.next
    return head.next


class RemoveNthFromEnd(object):
    """
    https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
    """
    @staticmethod
    def solution(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        head = ListNode(None, head)
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head.next


class ReverseLinkedList(object):
    """
    https://leetcode.cn/problems/reverse-linked-list/
    """
    @staticmethod
    def iteration_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        pre = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_
        return pre

    @classmethod
    def recursion_solution(cls, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if head is None or head.next is None:
            return head
        new_node = cls.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_node


class HasCycle(object):
    """
    https://leetcode.cn/problems/linked-list-cycle/submissions/
    """
    @staticmethod
    def solution(head: Optional[ListNode]) -> bool:
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not head or not head.next:
            return False
        slow, fast = head, head.next.next
        while fast is not slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class MergeTwoSortedLists(object):
    """
    https://leetcode.cn/problems/merge-two-sorted-lists/
    """
    @staticmethod
    def solution(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度：O(m+n)
        空间复杂度：O(1)
        """
        new_list = ListNode(None, None)
        p = new_list
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return new_list.next


class MiddleNodes(object):
    """
    https://leetcode.cn/problems/middle-of-the-linked-list/submissions/
    """
    @staticmethod
    def solution(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class MergedKSortedLists(object):
    """
    https://leetcode.cn/problems/merge-k-sorted-lists/
    """
    @classmethod
    def recursion_solution(cls, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        设：有K个链表，每个链表长度最长为n
        时间复杂度：O(n*K^2)
        空间复杂度：O(k)
        """
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        p = lists[0]
        q = cls.recursion_solution(lists[1:])
        return cls.merge_two_list(p, q)

    @classmethod
    def iteration_solution(cls, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        设：有K个链表，每个链表长度最长为n
        时间复杂度：O(n*K^2)
        空间复杂度：O(1)
        """
        merged_list = None
        for list_i in lists:
            merged_list = cls.merge_two_list(merged_list, list_i)
        return merged_list

    @classmethod
    def divide_and_conquer_solution(cls, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        分治思想的解法
        TODO: 完成归并排序、快速排序后，回来重做，重新分析
        """
        return cls.divide_merge(lists, 0, len(lists) - 1)

    @classmethod
    def divide_merge(cls, lists: List[Optional[ListNode]], l: int, r: int):
        """
        @param: l - 左指针
        @param: r - 右指针
        """
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return cls.merge_two_list(
            cls.divide_merge(lists, l, mid),
            cls.divide_merge(lists, mid+1, r))

    @classmethod
    def merge_two_list(cls, list1, list2):
        merged_list = ListNode()
        p = merged_list
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return merged_list.next


if __name__ == '__main__':
    lists = [init_list(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    print(MergedKSortedLists().mer)