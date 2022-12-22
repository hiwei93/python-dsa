class BinarySearchIteration(object):
    """
    二分查找，迭代实现
    - 时间复杂度：O(logn)
    - 空间复杂度：O(1)
    """
    @classmethod
    def search(cls, nums, value: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == value:
                return mid
            if nums[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1


class BinarySearchRecursive(object):
    """
    二分查找，递归实现
    - 时间复杂度：O(logn)
    - 空间复杂度：O(logn)
    """
    @classmethod
    def search(cls, nums, value: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        return cls.bsearch(nums, low, high, value)

    @classmethod
    def bsearch(cls, nums, low, high, value):
        if low > high:
            return -1

        mid = low + ((high - low) >> 1)
        if nums[mid] == value:
            return mid
        if nums[mid] < value:
            return cls.bsearch(nums, mid + 1, high, value)
        return cls.bsearch(nums, low, mid - 1, value)
