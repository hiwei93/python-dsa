import unittest

import sys

sys.path.append("basic_sort")

from basic_sort import bubble_sort, insertion_sort, selection_sort,\
    insertion_sort_v2


class TestBasicSort(unittest.TestCase):
    def test_bubble_sort(self):
        nums = [5, 4, 3, 2, 1]
        bubble_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        nums = [4, 5, 6, 1, 1, 3, 2]
        insertion_sort(nums)
        self.assertEqual(nums, [1, 1, 2, 3, 4, 5, 6])

    def test_selection_sort_v2(self):
        nums = [4, 5, 6, 1, 1, 3, 2]
        insertion_sort_v2(nums)
        self.assertEqual(nums, [1, 1, 2, 3, 4, 5, 6])

    def test_selection_sort(self):
        nums = [5, 4, 3, 2, 1]
        selection_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main(verbosity=2)
