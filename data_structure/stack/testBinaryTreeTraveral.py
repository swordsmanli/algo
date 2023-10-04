import unittest
from binaryTreeTraveral import Solution, TreeNode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.left = TreeNode(4)
        self.root.right = TreeNode(6)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(8)

    def test_preorder(self):
        self.assertEqual(Solution().preorder(self.root), [5,4,1,2,6,7,8])  # add assertion here

    def test_midorder(self):
        self.assertEqual(Solution().midorder(self.root), [1,4,2,5,7,6,8])  # add assertion here

    def test_postorder(self):
        self.assertEqual(Solution().postorder(self.root), [1,2,4,7,8,6,5])  # add assertion here



if __name__ == '__main__':
    unittest.main()
