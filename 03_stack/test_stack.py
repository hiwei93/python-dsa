import unittest

import sys

sys.path.append("stack")

from stack import ArrayStack, DynamicArrayStack, LinkedListStack


class TestArrayStack(unittest.TestCase):
    def test_push_item_over_capacity(self):
        stack = ArrayStack(3)
        for i in range(3):
            stack.push(i+1)
        print(stack)
        result = stack.push(4)
        self.assertEqual(result, False)

    def test_pop_item_from_empty_stack(self):
        stack = ArrayStack(5)
        item = stack.pop()
        self.assertEqual(item, None)


class TestDynmicArrayStatic(unittest.TestCase):
    def test_auto_increase_capacity(self):
        stack = DynamicArrayStack(3)
        for i in range(3):
            stack.push(i+1)
        print(stack)
        stack.push(4)
        print(stack)
        self.assertEqual(stack.capacity, 6)

    def test_auto_decrease_capacity(self):
        stack = DynamicArrayStack(3)
        for i in range(5):
            stack.push(i+1)
        stack.pop()
        stack.pop()
        print(stack)
        self.assertEqual(stack.capacity, 3)


class TestLinkedListStack(unittest.TestCase):
    def test_push_and_pop(self):
        stack = LinkedListStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(stack)
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.pop(), 3)
        print(stack)
        self.assertEqual(len(stack), 2)


if __name__ == '__main__':
    unittest.main()
