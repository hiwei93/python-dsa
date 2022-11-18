
def findKthLargestNum(nums: list, k: int):
    """
    求解第K大元素
    https://time.geekbang.org/column/article/41913
    课程练习题
    - 课程解法：不考虑有重复值的情况

    时间复杂度：O(n)
    空间复杂度：O(logn)
    """
    n = len(nums)
    if k > n:
        raise ValueError(f"{k=} is bigger than length of nums")

    def partition(p: int, r: int):
        povit = nums[r]
        i = j = p
        while j < r - 1:
            if nums[j] < povit:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def findKthLargestNum_c(p: int, r: int):
        q = partition(p, r)
        if q + 1 == k:
            return nums[q]
        if q + 1 > k:
            return findKthLargestNum_c(p, q - 1)
        # q + 1 < k
        return findKthLargestNum_c(q + 1, r)

    return findKthLargestNum_c(0, n-1)


class FindKthLargestElem:
    """
    https://leetcode.cn/problems/kth-largest-element-in-an-array
    - 时间复杂度：O(n)
    - 空间复杂度：O(logn)
    """
    @classmethod
    def solution(cls, nums: list, k: int) -> int:
        n = len(nums)
        return cls.quick_selection(nums, n-k, 0, n-1)

    @classmethod
    def quick_selection(cls, nums, index, p, r):
        q = cls.partition(nums, p, r)
        if q == index:
            return nums[q]
        if q > index:
            return cls.quick_selection(nums, index, p, q - 1)
        # q < index
        return cls.quick_selection(nums, index, q + 1, r)

    @classmethod
    def partition(cls, nums, p, r):
        """
        TODO: 待优化，最差情况可能严重不均分
        """
        povit = nums[r]
        i = j = p
        while j < r - 1:
            if nums[i] < povit:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
        return i
