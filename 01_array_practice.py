"""
数组练习
- 合并两个有序数组
- 求三数之和
- 求众数
- 求缺失的第一个正数
"""


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
    test_merge_ordered_list()