import unittest
from binaryBfsTraveral import TreeNode
from binaryBfsTraveral import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(5)
        self.root.left = TreeNode(4)
        self.root.right = TreeNode(6)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(2)

        self.root2 = TreeNode(4)
        self.root2.left = TreeNode(2)
        self.root2.right = TreeNode(7)
        self.root2.left.left = TreeNode(1)
        self.root2.left.right = TreeNode(3)
        self.root2.right.left = TreeNode(6)
        self.root2.right.right = TreeNode(9)

        self.root3 = TreeNode(1)
        self.root3.left = TreeNode(2)
        self.root3.right = TreeNode(2)
        self.root3.left.left = TreeNode(3)
        self.root3.left.right = TreeNode(4)
        self.root3.right.left = TreeNode(4)
        self.root3.right.right = TreeNode(3)

        self.root4 = TreeNode(1)
        self.root4.left = TreeNode(2)
        self.root4.right = TreeNode(2)
        self.root4.left.right = TreeNode(3)
        self.root4.left.left = TreeNode(None)
        self.root4.right.right = TreeNode(3)
        self.root4.right.left = TreeNode(None)

    def test_invertTree(self):
        self.assertEqual(Solution.inventTree(self.root2), [4,7,2,9,6,3,1])

    def test_bfsTraveral(self):
        self.assertEqual(Solution.bfsTraveral(self.root), [[5], [4, 6], [1, 2]])  # add assertion here

    def test_isSymmetric1(self):
        self.assertEqual(Solution.isSymmetric(self.root3), True)

    def test_isSymmetric2(self):
        # print(Solution.bfsTraveral2(self.root4))
        # print(Solution.inventTree(self.root4))
        self.assertEqual(Solution.isSymmetric(self.root4), False)


if __name__ == '__main__':
    unittest.main()
