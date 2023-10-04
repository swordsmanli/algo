import unittest
from binaryTreeRecursive import TreeNode
from binaryTreeRecursive import Solution


class TestBinaryRecursive(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.left = TreeNode(4)
        self.root.right = TreeNode(6)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(8)

    def test_recursive_preorder(self):
        self.assertEqual(Solution().preorderTraversal(self.root, []), [5,4,1,2,6,7,8])  # add assertion here

    def test_recursive_midorder(self):
        self.assertEqual(Solution().midorderTraveral(self.root, []), [1,4,2,5,7,6,8])

    def test_recursive_postorder(self):
        self.assertEqual(Solution().postorderTraveral(self.root, []), [1,2,4,7,8,6,5])


if __name__ == '__main__':
    unittest.main()
