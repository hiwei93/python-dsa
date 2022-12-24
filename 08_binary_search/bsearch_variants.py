def bsearch_first_match_v1(nums: list, v: int) -> int:
    """
    查找第一个值等于给定值的元素
    """
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= v:  # 目的：形成 low < v <= high, low + 1 = high; 这样保证找到的是第一个满足条件的值
            high = mid - 1
        else:
            low = mid + 1

    if low < n and nums[low] == v:  # 处理边界条件
        return low
    return -1

def bsearch_first_match_v2(nums: list, v: int) -> int:
    """
    查找第一个值等于给定值的元素
    """
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > v:
            high = mid - 1
        elif nums[mid] < v:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] != v:  # 判断是否为第一个满足条件的
                return mid
            high = mid - 1
    return -1


def bsearch_last_match_v1(nums: list, v: int) -> int:
    """
    查找最后一个值等于给定值的元素
    """
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] <= v:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] == v:
        return high
    return -1


def bsearch_last_match_v2(nums: list, v: int) -> int:
    """
    查找最后一个值等于给定值的元素
    """
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > v:
            high = mid - 1
        elif nums[mid] < v:
            low = mid + 1
        else:
            if mid == n - 1 or nums[mid + 1] != v:
                return mid
            low = mid + 1
    return -1
