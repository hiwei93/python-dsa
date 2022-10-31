import unittest

import sys
sys.path.append('linked_list')

from linked_list import LinkedList


def init_list(elems: list) -> LinkedList:
    l = LinkedList()
    for elem in elems:
        l.insert_value_to_tail(elem)
    return l


class TestLinkedList(unittest.TestCase):
    def test_find_by_index(self):
        elems = list(range(5))
        l = init_list(elems)
        node = l.find_by_index(1)
        self.assertEqual(node.data, elems[1])

    def test_find_by_value(self):
        elems = [1, 2, 3, 4, 5]
        l = init_list(elems)
        node = l.find_by_value(3)
        self.assertEqual(node.data, 3)

    def test_insert_value_after(self):
        elems = [1, 2, 3, 4, 5]
        l = init_list(elems)
        node = l.find_by_value(3)
        print(l)
        l.insert_value_after(node, -3)
        print(l)
        self.assertEqual(l.find_by_value(-3), l.find_by_index(3))

    def test_insert_value_before(self):
        elems = [1, 2, 3, 4, 5]
        l = init_list(elems)
        node = l.find_by_value(3)
        print(l)
        l.insert_value_before(node, -3)
        print(l)
        self.assertEqual(l.find_by_value(-3), l.find_by_index(2))

    def test_delete_by_value(self):
        elems = [1, 2, 3, 4, 5]
        l = init_list(elems)
        print(l)
        l.delete_by_value(3)
        print(l)
        self.assertEqual(l.find_by_value(3), None)

    def test_delete_by_node(self):
        elems = [1, 2, 3, 4, 5]
        l = init_list(elems)
        node = l.find_by_value(3)
        print(l)
        l.delete_by_node(node)
        print(l)
        self.assertEqual(l.find_by_value(3), None)


if __name__ == '__main__':
    unittest.main()
