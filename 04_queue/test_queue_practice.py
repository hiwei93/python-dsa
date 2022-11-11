import unittest

import sys

sys.path.append("queue_practice")

from queue_practice import CircularDequeLinkedList


class TestCircularDequeLinkedList(unittest.TestCase):
    def test_insert_front_from_empty_queue(self):
        queue = CircularDequeLinkedList(3)
        queue.insertFront(1)
        print(queue)
        self.assertEqual(queue.getFront(), 1)

    def test_insert_last_from_empty_queue(self):
        queue = CircularDequeLinkedList(3)
        queue.insertLast(1)
        print(queue)
        self.assertEqual(queue.getRear(), 1)

    def test_insert_front_from_to_two_elems_queue(self):
        queue = CircularDequeLinkedList(3)
        queue.insertFront(1)
        queue.insertFront(2)
        queue.insertFront(3)
        print(queue)
        self.assertEqual(queue.getFront(), 3)
        self.assertEqual(queue.insertFront(4), False)

    def test_insert_last_from_to_two_elems_queue(self):
        queue = CircularDequeLinkedList(3)
        queue.insertLast(1)
        queue.insertLast(2)
        queue.insertLast(3)
        print(queue)
        self.assertEqual(queue.getRear(), 3)
        self.assertEqual(queue.insertLast(4), False)

    def test_insert_front_and_delete_front(self):
        queue = CircularDequeLinkedList(5)
        for i in range(5):
            queue.insertFront(i+1)
        print(queue)
        for i in range(5):
            print(queue)
            self.assertEqual(queue.getFront(), 5 - i)
            queue.deleteFront()
        self.assertEqual(queue.getFront(), -1)

    def test_insert_last_and_delete_last(self):
        queue = CircularDequeLinkedList(5)
        for i in range(5):
            queue.insertLast(i+1)
        for i in range(5):
            print(queue)
            self.assertEqual(queue.getRear(), 5 - i)
            queue.deleteLast()
        self.assertEqual(queue.deleteLast(), False)
        self.assertEqual(queue.getRear(), -1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
