def binary_search(nums, value: int) -> int:
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
