"""
线性复杂度排序方法
- 桶排序、计数排序、基数排序
"""
from pprint import pprint


class BucketSort(object):
    """
    - 时间复杂度：最好O(n), 最坏O(nlogn), 平均O(n)
        - 设有n个值，分为m个桶，则每个桶平均分配 k = n / m
        - 每个桶使用快排，则每个桶排序时间复杂度O(klogk)，所有桶排序共耗时 O(m*klogk)
        - 带入得 O(nlog(n/m))，当m趋于n，则log(n/m)趋于常数，最后为：O(n)
    - 空间复杂度：O(n + m)
    - 稳定性：与选择的排序算法有关，此处使用的是快排，非稳定排序算法
    - 非原地算法
    """
    @staticmethod
    def sort(nums: list, bucket_num: int):
        min_v = max_v = nums[0]
        for elem in nums:
            if elem < min_v:
                min_v = elem
            elif elem > max_v:
                max_v = elem

        bucket_size = (max_v - min_v) // bucket_num + 1

        buckets = [[] for _ in range(bucket_num)]
        for num in nums:
            i = (num - min_v) // bucket_size
            buckets[i].append(num)

        pprint(buckets)

        k = 0
        for bucket in buckets:
            QuickSort.sort(bucket)
            for elem in bucket:
                nums[k] = elem
                k += 1


class QuickSort(object):
    @classmethod
    def sort(cls, nums):
        n = len(nums)
        cls.quick_sort_c(nums, 0, n-1)

    @classmethod
    def quick_sort_c(cls, nums, p, r):
        if p >= r:
            return
        q = cls.partition(nums, p, r)
        cls.quick_sort_c(nums, p, q-1)
        cls.quick_sort_c(nums, q+1, r)

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


class CountingSort(object):
    """
    计数排序：
    - 时间复杂度：O(n)
    - 空间复杂度：O(n)
    """
    @classmethod
    def sort(cls, nums):
        n = len(nums)
        if n <= 1:
            return

        min_v = max_v = nums[0]
        for num in nums:
            if num < min_v:
                min_v = num
            elif num > max_v:
                max_v = num

        bucket_size = max_v - min_v + 1
        buckets = [0] * bucket_size
        # 分桶统计相同元素个数
        for num in nums:
            buckets[num-min_v] += 1
        # 元素个数从前向后累加
        for i in range(1, bucket_size):
            buckets[i] += buckets[i-1]
        # 计数排序
        _sorted = [None] * n
        for i in range(n-1, -1, -1):
            num = nums[i]
            _sorted[buckets[num-min_v]-1] = num
            buckets[num-min_v] -= 1
        # 排序结果拷贝回原始数组
        for i in range(n):
            nums[i] = _sorted[i]
