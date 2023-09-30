import unittest
from stackImplQueue import MyStackQueue


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = MyStackQueue()

    def test_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)

    def test_push(self):
        self.queue.push(1)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 1)

    def test_empty(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.pop()
        self.queue.pop()
        self.assertEqual(self.queue.empty(), True)
        self.queue.push(3)
        self.assertEqual(self.queue.empty(), False)


if __name__ == '__main__':
    unittest.main()
