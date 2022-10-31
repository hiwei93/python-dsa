import unittest

import sys

sys.path.append('lru_cache')

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_get_data_from_empty_cache(self):
        cache = LRUCache(5)
        print(cache)
        v = cache.get(1)
        self.assertEqual(v, None)

    def test_put_data_to_empty_cache(self):
        cache = LRUCache(5)
        print(cache)
        cache.put(1, -1)
        print(cache)
        self.assertEqual(cache.get(1), -1)

    def test_put_several_data_to_cache(self):
        cache = LRUCache(5)
        for i in range(1, 4, 1):
            cache.put(i, -i)
        values = list(cache)
        self.assertEqual(values[0], (3, -3))
        self.assertEqual(values[1], (2, -2))
        self.assertEqual(values[2], (1, -1))

    def test_put_data_to_full_cache(self):
        print("#"*20, "test_put_data_to_full_cache")
        cache = LRUCache(5)
        for i in range(1, 6, 1):
            cache.put(i, -i)
        print(cache)
        cache.put(6, -6)
        print(cache)
        values = list(cache)
        self.assertEqual(values[0], (6, -6))
        self.assertEqual(values[-1], (2, -2))

    def test_get_data_from_one_data_cahce(self):
        print("#"*20, "test_get_data_from_one_data_cahce")
        cache = LRUCache(5)
        cache.put(3, -3)
        print(cache)
        v = cache.get(3)
        print(cache)
        self.assertEqual(v, -3)

    def test_get_head_data(self):
        print("#"*20, "test_get_head_data")
        cache = LRUCache(5)
        for i in range(1, 4, 1):
            cache.put(i, -i)
        print(cache)
        cache.get(3)
        print(cache)
        values = list(cache)
        self.assertEqual(values[0], (3, -3))

    def test_get_non_existent_data(self):
        print("#"*20, "test_get_non_existent_data")
        cache = LRUCache(5)
        for i in range(1, 4, 1):
            cache.put(i, -i)
        print(cache)
        v = cache.get(6)
        print(cache)
        self.assertEqual(v, None)

    def test_get_data_from_full_cache(self):
        print("#"*20, "test_put_data_to_full_cache")
        cache = LRUCache(5)
        for i in range(1, 6, 1):
            cache.put(i, -i)
        print(cache)
        cache.get(5)  # 访问根节点
        print(cache)
        values = list(cache)
        self.assertEqual(values[0], (5, -5))

        cache.get(1)  # 访问尾结点
        print(cache)
        values = list(cache)
        self.assertEqual(values[0], (1, -1))

        cache.get(3)  # 访问其他节点
        print(cache)
        values = list(cache)
        self.assertEqual(values[0], (3, -3))


if __name__ == '__main__':
    unittest.main()