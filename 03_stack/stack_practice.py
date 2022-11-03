class ValidParentheses(object):
    """
    https://leetcode.cn/problems/valid-parentheses
    """
    @staticmethod
    def solution(s: str) -> bool:
        """
        设括号数量为 m
        时间复杂度: O(n)
        空间复杂度：O(n + m)
        """
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for elem in s:
            if elem in pairs:
                stack.append(elem)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != elem:
                    return False
        if len(stack) > 0:
            return False
        return True


class MinStackRoughSolution(object):
    """
    https://leetcode.cn/problems/min-stack
    - 粗暴解法：使用一个变量存储最小值
    - 问题：牺牲了出栈方法的性能，出栈的时候需要找到最小值，从O(1)变为了O(n)
    """
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, val: int) -> None:
        """O(1)"""
        if self.min is None or val < self.min:
            self.min = val
        self.items.append(val)

    def __find_min(self):
        min_ = None
        for i in self.items:
            if min_ is None or i < min_:
                min_ = i
        return min_

    def pop(self) -> None:
        """O(n)"""
        if len(self.items) == 0:
            return None
        val = self.items.pop()
        if len(self.items) == 0:
            self.min = None
        if val == self.min:
            self.min = self.__find_min()
        return val

    def top(self) -> int:
        """O(1)"""
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def getMin(self) -> int:
        """O(1)"""
        return self.min