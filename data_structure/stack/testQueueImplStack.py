import unittest
from queueImplStack import *


class TestQueueImplStackCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = MyQueueStack()

    def test_pop(self):
        self.stack.push(2)
        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)  # add assertion here

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)

    def test_empty(self):
        self.stack.push(1)
        self.assertEqual(self.stack.empty(), False)
        self.stack.pop()
        self.assertEqual(self.stack.empty(), True)


class TestDoubleQueueImplStackCase(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = MyDoubleQueueStack()

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)  # add assertion here

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)

    def test_empty(self):
        self.stack.push(1)
        self.assertEqual(self.stack.empty(), False)
        self.stack.pop()
        self.assertEqual(self.stack.empty(), True)


if __name__ == '__main__':
    unittest.main()
