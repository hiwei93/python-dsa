
class MergeSort:
    """
    递推公式:
    - f(p, r) = f(p, q) + f(q+1, r)
    - 递归基：p >= r

    分析：
    - 时间复杂度：O(nlogn)
    - 空间复杂度：O(n)  # TODO: 知道计算方式
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
