# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:treeSymmetric.py
# Time:2023/10/8 22:25
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 101 递归实现二叉树是否对称， 只需要递归比较做子树和右子树是否对称
# 进一步比较左右子树外侧节点和内侧节点是否分表别相等


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:

    @staticmethod
    def compare(left: TreeNode, right: TreeNode) -> bool:
        if left is None and right:
            return False
        elif right is None and left:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False
        else:
            bool1 = Solution.compare(left.left, right.right)
            bool2 = Solution.compare(left.right, right.left)
            if bool2 and bool1:
                return True
            else:
                return False

    @staticmethod
    def isSymmetric(root: TreeNode):
        return Solution.compare(root.left, root.right)
