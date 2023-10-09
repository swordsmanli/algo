import unittest
from binaryBalanceTree import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.right = TreeNode(6)
        self.root.left = TreeNode(4)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)

    def test_balance(self):
        self.assertEqual(Solution().isBalance(self.root), True)

    def test_none_balance(self):
        self.root.left.right.left = TreeNode(9)
        self.root.left.right.right = TreeNode(8)
        self.assertEqual(Solution().isBalance(self.root), False)



if __name__ == '__main__':
    unittest.main()
