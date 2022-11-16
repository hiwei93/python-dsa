import unittest

import sys

sys.path.extend('advance_sort')

from advance_sort import MergeSort, QuickSort


class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        expected = [1, 2, 3, 4, 5]
        nums = [1, 2, 3, 4, 5]
        MergeSort.merge_sort(nums)
        self.assertEqual(nums, expected)
        nums = [5, 4, 3, 2, 1]
        MergeSort.merge_sort(nums)
        self.assertEqual(nums, expected)
        nums = [3, 4, 5, 1, 2]
        MergeSort.merge_sort(nums)
        self.assertEqual(nums, expected)
        expected = [1, 2, 3, 3, 4, 5]
        nums = [1, 2, 3, 4, 5, 3]
        MergeSort.merge_sort(nums)
        self.assertEqual(nums, expected)


class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        expected = [1, 2, 3, 4, 5, 6]
        nums = [1, 2, 3, 4, 5, 6]
        QuickSort.quick_sort(nums)
        self.assertEqual(nums, expected)
        nums = [6, 5, 4, 3, 2, 1]
        QuickSort.quick_sort(nums)
        self.assertEqual(nums, expected)
        nums = [3, 1, 4, 2, 6, 5]
        QuickSort.quick_sort(nums)
        self.assertEqual(nums, expected)
        expected = [1, 2, 2, 3, 4, 5]
        nums = [1, 2, 3, 4, 5, 2]
        QuickSort.quick_sort(nums)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
