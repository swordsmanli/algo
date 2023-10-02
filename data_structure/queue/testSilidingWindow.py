import unittest
from SlidingWindow import maxSlidingWindown


class MyTestCase(unittest.TestCase):
    def test_maxSlidingWindow(self):
        nums = [2, 4, -2, -4, 3, 1, 5]
        k = 4
        self.assertEqual(maxSlidingWindown(nums, k), [4, 4, 3, 5])  # add assertion here


if __name__ == '__main__':
    unittest.main()
