import unittest

import sys

sys.path.extend("binary_search")

from binary_search import BinarySearchIteration, BinarySearchRecursive


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_iteration(self):
        nums, v = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98], 23
        expected = 3
        self.assertEqual(BinarySearchIteration.search(nums, v), expected)

    def test_binary_search_recursive(self):
        nums, v = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98], 23
        expected = 3
        self.assertEqual(BinarySearchRecursive.search(nums, v), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
