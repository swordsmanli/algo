import unittest
from treeMinDepth import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.left = TreeNode(4)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)
        self.root.right = TreeNode(6)

    def test_recursive(self):
        self.assertEqual(Solution().minDepth(self.root), 2)  # add assertion here

    def test_iterator(self):
        self.assertEqual(Solution2().getMinDepth(self.root), 2)

if __name__ == '__main__':
    unittest.main()
