
class MergeSort:
    """
    递推公式:
    - f(p, r) = f(p, q) + f(q+1, r)
    - 递归基：p >= r

    分析：
    - 时间复杂度：O(nlogn)
    - 空间复杂度：O(n)  # TODO: 需要知道计算方式
    - 稳定排序
    - 非原地排序算法
    """
    @classmethod
    def merge_sort(cls, nums: list):
        n = len(nums)
        cls.merge_sort_c(nums, 0, n-1)

    @classmethod
    def merge_sort_c(cls, nums: list, p: int, r: int):
        if p >= r:
            return
        q = (p + r) >> 1
        cls.merge_sort_c(nums, p, q)
        cls.merge_sort_c(nums, q + 1, r)
        cls.merge(nums, p, q, r)

    @classmethod
    def merge(cls, nums: list, p: int, q: int, r: int):
        tmp = []
        i, j = p, q + 1
        while i <= q and j <= r:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        start = i
        end = q
        if j <= r:
            start = j
            end = r
        while start <= end:
            tmp.append(nums[start])
            start += 1
        for i, elem in enumerate(tmp):
            nums[p+i] = elem


class QuickSort:
    """
    递推公式：
    - f(p, r) = f(p, q - 1) + f(q + 1, r)
    - 递归基：p >= r

    实现思想：
    1. 每次选择一个元素就位，并使其左侧元素全部小于该元素，其右侧元素全部大于等于该元素
    2. 基于该元素，分为左右两个子问题，分别进行排序
    3. 只有一个元素或者没有元素的时候停止继续

    分析：
    - 时间复杂度：最优 O(nlogn), 最差 O(n^2)
    - 空间复杂度：O(logn)
        - 设期望每次都可以均分，则递归的数据规模变化：
        - n, n/2, n/4, ..., 1
        - 设递归次数为 k，则数据规模可以表示为：n/2^k
        - n/2^0, n/2^1, n/2^2, ..., 1
        - 最后一次递归为 n/2^k = 1
        - 解得 k = logn
        - 进行了logn次递归，考虑递归栈用到的空间，则空间复杂度为 O(n)
    - 非稳定排序
    - 原地排序算法
    """
    @classmethod
    def quick_sort(cls, nums: list):
        n = len(nums)
        cls.quick_sort_c(nums, 0, n-1)

    @classmethod
    def quick_sort_c(cls, nums: list, p: int, r: int):
        if p >= r:
            return
        q = cls.partition(nums, p, r)
        print(f"{p=} {r=} {q=} {nums=}")
        cls.quick_sort_c(nums, p, q-1)
        cls.quick_sort_c(nums, q+1, r)

    @classmethod
    def partition(cls, nums: list, p: int, r: int):
        """
        主要思想：
        1. 通过数据交换实现原地算法
        2. 通过双指针，将小于povit的元素置换到i指针前面
        """
        pivot = nums[r]
        i = p
        for j in range(p, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

