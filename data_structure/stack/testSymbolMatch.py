import unittest
from symbolMatch import *
from rpnCalc import Solution as RPN


class MyTestCase(unittest.TestCase):

    def test_match_symbol1(self):
        self.assertEqual(Solution.is_match_symbol("()[]{}"), True)  # add assertion here

    def test_match_symbol2(self):
        self.assertEqual(Solution.is_match_symbol("()"), True)

    def test_match_symbol3(self):
        self.assertEqual(Solution.is_match_symbol("(]"), False)

    def test_rpn(self):
        self.assertEqual(RPN.calcRpn(["5", "2", "-", "4", "*"]), 12)


if __name__ == '__main__':
    unittest.main()
