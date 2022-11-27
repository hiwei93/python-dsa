import unittest

import sys

sys.path.extend("sort_practice")

from sort_practice import FindKthLargestElem


class TestFindKthLargestElem(unittest.TestCase):
    def test_solution(self):
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
        expected = 4
        self.assertEqual(FindKthLargestElem.solution(nums, k), expected)
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 1
        expected = 6
        self.assertEqual(FindKthLargestElem.solution(nums, k), expected)
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 9
        expected = 1
        self.assertEqual(FindKthLargestElem.solution(nums, k), expected)
        nums, k = [2, 1], 1
        expected = 2
        self.assertEqual(FindKthLargestElem.solution(nums, k), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
