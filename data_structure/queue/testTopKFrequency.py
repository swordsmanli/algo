import unittest
from topKFrequecyNunmber import Solution


class MyTestCase(unittest.TestCase):
    def test_topKFrequency(self):
        nums = [2, 2, 2, 2, 2, 3, 3, 3, 1]
        k = 2
        self.assertEqual(Solution.topKFrequency(nums, k), [2, 3])  # add assertion here

    def test_topKLeastFrequency(self):
        nums = [2, 2, 2, 2, 2, 3, 3, 3, 1]
        k = 2
        self.assertEqual(Solution.topKLeastFrequncy(nums, k), [1, 3])


if __name__ == '__main__':
    unittest.main()
