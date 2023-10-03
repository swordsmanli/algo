import unittest
from trapRainWater import *


class MyTestCase(unittest.TestCase):
    def test_trapRainWater(self):
        height = [4,2,0,3,2,5]
        self.assertEqual(Solution.trapRainWater(height), 9)
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(Solution.trapRainWater(height), 6)

    def test_trapRainWaterDP(self):
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(Solution.trapRainWaterDP(height), 9)
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(Solution.trapRainWaterDP(height), 6)


if __name__ == '__main__':
    unittest.main()
