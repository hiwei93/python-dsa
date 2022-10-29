"""
数组练习
- 合并两个有序数组
- 求三数之和
- 求众数
- 求缺失的第一个正数
"""


from typing import List


def merge_ordered_list(l1: list, l2: list) -> list:
    """
    合并两个有序数组, 时间复杂度：O(max(m, n))，空间复杂度o(m + n)
    - 此处认为连个数组的顺序都为从小到大
    - l1 中元素优先级高于 l2
    （归并排序中会用到）
    """
    l1_len, l2_len = len(l1), len(l2)
    merged_l = [None] * (l1_len + l2_len)  # 此处不需要如此初始化， 只是模拟分配内存的步骤

    p1, p2 = 0, 0
    i = 0

    while p1 < l1_len and p2 < l2_len:
        if l1[p1] <= l2[p2]:
            merged_l[i] = l1[p1]
            p1 += 1
        else:
            merged_l[i] = l2[p2]
            p2 += 1
        i += 1

    for j in range(p1, l1_len, 1):
        merged_l[i] = l1[j]
        i += 1
    for j in range(p2, l2_len, 1):
        merged_l[i] = l2[j]
        i += 1
    return merged_l


class TowSum():
    """
    https://leetcode.cn/problems/two-sum/
    """
    @staticmethod
    def solution_1(nums: List[int], target: int) -> List[int]:
        """
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        length = len(nums)
        for i in range(0, length - 1, 1):
            for j in range(i + 1, length, 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def solution_2(nums: List[int], target: int) -> List[int]:
        """
        时间复杂度: O(n)
        空间复杂度：O(n)
        """
        value2index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in value2index:
                return [value2index[diff], i]
            value2index[num] = i
        return []


class ThreeSum():
    """
    https://leetcode.cn/problems/3sum/
    """
    @staticmethod
    def solution(nums: List[int]) -> List[List[int]]:
        """
        排序、去重、双指针
        - 时间复杂度 O(n^2)
            - 排序O(nlongn) https://www.cnblogs.com/clement-jiao/p/9243066.html
            - 两层遍历O(n^2)
        - 空间复杂度O(n) // 主要用在排序上面了
        """
        length = len(nums)
        results = []
        if length < 3:
            return results

        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:  # 优化一：从第二个元素开始去重
                continue
            lp, rp = i + 1, length - 1  # 优化二：左右指针，减少一层循环
            while lp < rp:
                sum_ = nums[i] + nums[lp] + nums[rp]
                if sum_ == 0:
                    results.append([nums[i], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:  # 优化一：去重
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:  # 优化一：去重
                        rp -= 1
                    lp += 1
                    rp -= 1
                elif sum < 0:
                    lp += 1
                elif sum > 0:
                    rp -= 1
        return results


class MajorityElement():
    """
    https://leetcode.cn/problems/majority-element/
    """
    @staticmethod
    def solution_by_hash(nums: List[int]) -> int:
        """
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        frequent = len(nums) / 2
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        for num, count in counter.items():
            if count > frequent:
                return num
        return None

    @staticmethod
    def solution_by_sort(nums: List[int]) -> int:
        """
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]

    @staticmethod
    def solution_by_boyer_Moore(nums: List[int]) -> int:
        """
        时间复杂度：O(n)
        空间发复杂度：O(1)
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


class FirstMissingPositive():
    """
    https://leetcode.cn/problems/first-missing-positive
    """
    @staticmethod
    def solution_by_hash(nums: List[int]) -> int:
        """
        模拟哈希表，更改原始数组，增加标记位
        - 时间复杂度O(n)
        - 空间复杂度O(1)
        """
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for i in range(length):
            num = abs(nums[i])
            if num <= length:
                nums[num - 1] = -1 * abs(nums[num - 1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

    @staticmethod
    def solution_by_exchange(nums: List[int]) -> int:
        """
        时间复杂度：O(n)
        空间复杂度：O(1)
        注意：注意替换顺序
        """
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1
        return length + 1


def test_merge_ordered_list():
    l1 = [1, 2, 3]
    l2 = [2, 2, 4, 5]
    merged_l = merge_ordered_list(l1, l2)
    assert merged_l == [1, 2, 2, 2, 3, 4, 5]

    l1 = [2]
    l2 = [1, 3]
    merged_l = merge_ordered_list(l1, l2)
    assert merged_l == [1, 2, 3]

    l1 = []
    l2 = []
    merged_l = merge_ordered_list(l1, l2)
    assert merged_l == []


if __name__ == '__main__':
    FirstMissingPositive.solution_by_exchange([3, 4, -1, 1])