import unittest

import sys

sys.path.append("queue_")

from queue_ import ArrayQueue, DynamicArrayQueue, LinkedListQueue, \
    CircularQueue, CircularQueueV2


class TestQueue(unittest.TestCase):
    def test_add_item_to_full_queue(self):
        queue = ArrayQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        self.assertEqual(queue.enqueue(6), False)

    def test_fake_full(self):
        """
        测试假满的情况
        """
        queue = ArrayQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        queue.dequeue()
        queue.dequeue()
        print(queue)
        self.assertEqual(queue.enqueue(6), True)

    def test_head_tail_all_in_the_final_position(self):
        """
        测试head和tail都在最末尾的情况
        """
        queue = ArrayQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        for _ in range(5):
            queue.dequeue()
        self.assertEqual(queue.enqueue(6), True)

    def test_get_value_from_empty_queue(self):
        queue = ArrayQueue(5)
        self.assertEqual(queue.dequeue(), None)


class TestDynamicArrayQueue(unittest.TestCase):
    def test_add_value_to_full_queue(self):
        queue = DynamicArrayQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        self.assertEqual(queue.enqueue(6), True)
        print(queue)


class TestLinkedListQueue(unittest.TestCase):
    def test_get_elem_from_empty_queue(self):
        queue = LinkedListQueue()
        self.assertEqual(queue.dequeue(), None)

    def test_enqueue_and_dequeue(self):
        queue = LinkedListQueue()
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        for i in range(5):
            self.assertEqual(queue.dequeue(), i + 1)


class TestCircularQueue(unittest.TestCase):
    def test_add_value_to_full_queue(self):
        queue = CircularQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        self.assertEqual(queue.enqueue(6), False)

    def test_get_elem_from_empty_queue(self):
        queue = CircularQueue(5)
        self.assertEqual(queue.dequeue(), None)
        for i in range(5):
            queue.enqueue(i+1)
        for _ in range(5):
            queue.dequeue()
        self.assertEqual(queue.dequeue(), None)

    def test_enqueue_and_dequeue(self):
        queue = CircularQueue(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        for i in range(3):
            self.assertEqual(queue.dequeue(), i + 1)
        for i in range(3):
            queue.enqueue(i+6)
        print(queue)


class TestCircularQueueV2(unittest.TestCase):
    def test_add_value_to_full_queue(self):
        queue = CircularQueueV2(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        self.assertEqual(queue.enqueue(6), False)

    def test_get_elem_from_empty_queue(self):
        queue = CircularQueueV2(5)
        self.assertEqual(queue.dequeue(), None)
        for i in range(5):
            queue.enqueue(i+1)
        for _ in range(5):
            queue.dequeue()
        self.assertEqual(queue.dequeue(), None)

    def test_enqueue_and_dequeue(self):
        queue = CircularQueueV2(5)
        for i in range(5):
            queue.enqueue(i+1)
        print(queue)
        for i in range(3):
            self.assertEqual(queue.dequeue(), i + 1)
        for i in range(3):
            queue.enqueue(i+6)
        print(queue)


if __name__ == '__main__':
    unittest.main(verbosity=2)
