from typing import List


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

    def pop(self):
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


class MinStackAssistStackSolution(object):
    """
    https://leetcode.cn/problems/min-stack
    - 辅助栈方法
    - 各个操作时间复杂度: O(1)
    - 空间复杂度：O(n)
    """
    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, val: int):
        self.items.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items.pop()
        self.min_stack.pop()
        return val

    def top(self) -> int:
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


class QueueByStack:
    """
    https://leetcode.cn/problems/implement-queue-using-stacks
    - push() 时间复杂度：O(n^2)
    """
    def __init__(self):
        self.stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        while self.stack:
            self.help_stack.append(self.stack.pop())
        self.stack.append(x)
        while self.help_stack:
            self.stack.append(self.help_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class QueueByStackOptmize:
    """
    https://leetcode.cn/problems/implement-queue-using-stacks
    - 优化栈元素迁移的次数
    - pop(), peek() 均摊时间复杂度：O(n)
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def __in2out(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            self.__in2out()
        return self.out_stack.pop()

    def peek(self) -> int:
        if len(self.out_stack) == 0:
            self.__in2out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


class EvaluateReversePolishNotation:
    """
    https://leetcode.cn/problems/evaluate-reverse-polish-notation
    逆波兰表达式求解
    - 时间复杂度: O(n)
    - 空间复杂度：O(n)
    """
    @classmethod
    def compute(cls, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        if op == "*":
            return num1 * num2
        if op == "/":
            return int(num1 / num2)  # 注意点二：除法获取整数部分

    @classmethod
    def evalRPN(cls, tokens: List[str]) -> int:
        num_stack = []

        for elem in tokens:
            if elem.isdigit() or len(elem) > 1:  # 注意点一：判断是否位数字
                num_stack.append(int(elem))
            else:
                after_num, num = num_stack.pop(), num_stack.pop()
                num_stack.append(cls.compute(num, after_num, elem))
        return num_stack[-1]


class LongestValidParentheses:
    @staticmethod
    def solution(s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, elem in enumerate(s):
            if elem == '(':
                stack.append(i)
            elif elem == ')':
                if len(stack) == 0:
                    stack.append(i)
                else:
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(i)
                    else:
                        max_len = max(max_len, i - stack[-1])
        return max_len


if __name__ == '__main__':
    print(LongestValidParentheses.solution(")()())"))
