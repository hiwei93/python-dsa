"""
栈练习题：
- https://leetcode.cn/problem-list/cC9Vnw7N
"""

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


class BackspaceStringCompare:
    """
    https://leetcode.cn/problems/backspace-string-compare
    """
    @classmethod
    def convert_str2stack(cls, value: str):
        stack = []
        for elem in value:
            if elem == '#':
                if len(stack):
                    stack.pop()
            else:
                stack.append(elem)
        return stack

    @classmethod
    def solution(cls, s: str, t: str) -> bool:
        """
        时间复杂度：O(m + n)
        空间复杂度：O(m + n)
        """
        stack_s = cls.convert_str2stack(s)
        stack_t = cls.convert_str2stack(t)
        if len(stack_s) != len(stack_t):
            return False
        while stack_s or stack_t:
            value_s = stack_s.pop()
            value_t = stack_t.pop()
            if value_s != value_t:
                return False
        return True


class BasicCalculator:
    """
    https://leetcode.cn/problems/basic-calculator
    TODO：需要再次实现，确保已经理解
    """
    @staticmethod
    def solution(s: str) -> int:
        """
        括号展开方法
        """
        op_stack = [1]
        sign = 1
        result = 0
        i, n = 0, len(s)

        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = op_stack[-1]
                i += 1
            elif s[i] == '-':
                sign = -op_stack[-1]
                i += 1
            elif s[i] == '(':
                op_stack.append(sign)
                i += 1
            elif s[i] == ')':
                op_stack.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                result += num * sign
        return result


class BaseballGame:
    """
    https://leetcode.cn/problems/baseball-game
    """
    @staticmethod
    def solution(operations: List[str]) -> int:
        score_stack = []
        for op in operations:
            if op == '+':
                first = score_stack.pop()
                second = score_stack.pop()
                score_stack.append(second)
                score_stack.append(first)
                score_stack.append(first + second)
            elif op == 'C':
                score_stack.pop()
            elif op == 'D':
                score_stack.append(2 * score_stack[-1])
            else:
                score_stack.append(int(op))
        return sum(score_stack)


class NextGreaterElementI:
    """
    https://leetcode.cn/problems/next-greater-element-i
    """
    @staticmethod
    def solution(nums1: List[int], nums2: List[int]) -> List[int]:
        """
        暴力解法：
        时间复杂度：O(m * n)
        """
        result = []
        for elem1 in nums1:
            position, next_max = -1, -1
            for i, elem2 in enumerate(nums2):
                if elem1 == elem2:
                    position = i
                if position > -1 and elem2 > elem1:
                    next_max = elem2
                    break
            result.append(next_max)
        return result

    """
    问题
    1. 需要找到num1在num2中的位置
    2. 找到num2中元素后面的第一个最大值

    优化
    1. 先处理num2，把每个值后面的的第一个最大值先计算出来
    2. 使用哈希表存储元素值与其一个最大值的关系
    3. 使用单调栈计算第一个最大值
    """
    @staticmethod
    def solution_by_stack(nums1: List[int], nums2: List[int]) -> List[int]:
        """
        单调栈 + 哈希表
        时间复杂度：O(m+n)
        空间复杂度: O(n)
        """
        next_greater_map = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater_map[num] = stack[-1] if stack else -1
            stack.append(num)
        return [next_greater_map[n] for n in nums1]


if __name__ == '__main__':
    print(NextGreaterElementI.solution_by_stack([4, 1, 2], [1, 3, 4, 2]))
