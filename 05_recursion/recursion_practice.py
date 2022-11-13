class ClimbingStairs:
    """
    https://leetcode.cn/problems/climbing-stairs/
    TODO：在排序和树那两节课会讲两种递归代码的时间复杂度分析方法，完成后回来更新复杂度分析
    """
    cache = {}

    @classmethod
    def basic_solution(cls, n: int) -> int:
        """
        递归解法，会超时
        - 时间复杂度：O(n^2)
        - 空间复杂度：O(n^2)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return cls.climbStairs(n - 1) + cls.climbStairs(n - 2)

    @classmethod
    def cache_solution(cls, n: int) -> int:
        """
        递归 + 缓存优化
        - 时间复杂度：O(n)
        - 空间复杂度：(n)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in cls.cache:
            return cls.cache[n]
        result = cls.climbStairs(n - 1) + cls.climbStairs(n - 2)
        cls.cache[n] = result
        return result

    @staticmethod
    def iteration_solution(n: int) -> int:
        """
        迭代解法
        - 时间复杂度: O(n)
        - 空间复杂度: O(1)
        可优化：
        1. 优化 n=1, n=2 两个特殊情况，减少逻辑判断
        2. 优化prepre, pre, result变量赋值方式，减少变量
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        prepre, pre, result = 1, 2, 0
        for i in range(3, n + 1):
            result = pre + prepre
            prepre = pre
            pre = result
        return result

    @staticmethod
    def iteration_solutionv2(n: int) -> int:
        """
        迭代解法，优化
        """
        prepre, pre = 1, 1
        for i in range(2, n + 1):
            prepre, pre = pre, pre + prepre
        return pre
