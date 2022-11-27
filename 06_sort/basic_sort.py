"""
冒牌排序、插入排序、选择排序
"""


def bubble_sort(nums: list):
    """
    冒泡排序：
    - 时间复杂度：最优 O(n)，最差 O(n^2)，平均 O(n^2)
    - 空间复杂度: O(1)
    - 原地排序算法
    - 稳定排序算法
    """
    n = len(nums)
    for i in range(n):
        ordered = True
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:  # 注意比较操作，要确保排序的稳定性
                nums[j+1], nums[j] = nums[j], nums[j+1]
                ordered = False
        if ordered:
            break


def insertion_sort(nums: list):
    """
    插入排序
    - 时间复杂度：最优 O(n), 最差 O(n^2), 平均 O(n)
    - 空间复杂度: O(1)
    - 原地排序算法
    - 稳定排序算法
    TODO: 不确认该实现方法是否正确，使用元素替换代替元素搬运
    """
    n = len(nums)
    for i in range(n):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:  # 注意比较操作，要确保排序的稳定性
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break


def insertion_sort_v2(nums: list):
    """
    插入排序, 官方实现版本
    """
    n = len(nums)
    if n <= 1:
        return

    for i in range(1, n):
        v = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > v:
            nums[j + 1] = nums[j]  # 当前元素向后移动
            j -= 1
        nums[j + 1] = v  # 遍历将 j 多减了一次


def selection_sort(nums: list):
    """
    选择排序
    - 时间复杂度：最优 O(n^2), 最差 O(n^2)，平均 O(n^2)
    - 空间复杂度: O(1)
    - 是原地排序算法
    - 不是稳定排序算法
    """
    n = len(nums)
    for i in range(n):
        min_, min_index = nums[i], i
        for j in range(i, n):
            if nums[j] < min_:
                min_ = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]