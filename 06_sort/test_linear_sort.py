import unittest

import sys

sys.path.extend('linear_sort')

from linear_sort import BucketSort, CountingSort


class TestLinearSort(unittest.TestCase):
    def test_bucket_sort(self):
        nums = [5, 4, 3, 2, 1]
        expected = sorted(nums)
        BucketSort.sort(nums, 3)
        self.assertEqual(nums, expected)

    def test_counting_sort(self):
        nums = [2, 5, 3, 1, 2, 3, 1, 3]
        expected = sorted(nums)
        CountingSort.sort(nums)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
