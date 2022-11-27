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
        pivot = nums[r]
        i = j = p
        while j < r:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
