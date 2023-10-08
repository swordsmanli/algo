import unittest
from treeMaxDepth import Solution, TreeNode, Solution2


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.left = TreeNode(4)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)
        self.root.right = TreeNode(6)

    def test_recursive(self):
        self.assertEqual(Solution.maxDepth(self.root), 3)  # add assertion here

    def test_iteration(self):
        self.assertEqual(Solution2.getMaxDepth(self.root), 3)


if __name__ == '__main__':
    unittest.main()
