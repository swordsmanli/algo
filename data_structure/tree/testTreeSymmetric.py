import unittest
from treeSymmetric import Solution, TreeNode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(2)
        self.root.left = TreeNode(3)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)

        self.root.right.left = TreeNode(5)
        self.root.right.right = TreeNode(4)

    def test_something(self):
        self.assertEqual(Solution.isSymmetric(self.root), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
