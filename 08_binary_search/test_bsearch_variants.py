import unittest

import sys

sys.path.extend('bsearch_variants')

from bsearch_variants import bsearch_first_match_v1, bsearch_first_match_v2, \
    bsearch_last_match_v1, bsearch_last_match_v2


class TestBsearchVariants(unittest.TestCase):
    def test_bsearch_first_match_v1(self):
        nums = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        v, expected = 8, 5
        self.assertEqual(bsearch_first_match_v1(nums, v), expected)
        v, expected = 7, -1
        self.assertEqual(bsearch_first_match_v1(nums, v), expected)

    def test_bsearch_first_match_v2(self):
        nums = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        v, expected = 8, 5
        self.assertEqual(bsearch_first_match_v2(nums, v), expected)
        v, expected = 7, -1
        self.assertEqual(bsearch_first_match_v2(nums, v), expected)

    def test_bsearch_last_match_v1(self):
        nums = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        v, expected = 8, 7
        self.assertEqual(bsearch_last_match_v1(nums, v), expected)
        v, expected = 9, -1
        self.assertEqual(bsearch_last_match_v1(nums, v), expected)

    def test_bsearch_last_match_v2(self):
        nums = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
        v, expected = 8, 7
        self.assertEqual(bsearch_last_match_v2(nums, v), expected)
        v, expected = 9, -1
        self.assertEqual(bsearch_last_match_v2(nums, v), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
