# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:binaryBalanceTree.py
# Time:2023/10/9 22:17
# Author:white_li@trendmicro.com
# version:py3
"""
#leetcode 110
# height 平均 O(logn), 最坏O(n), balance O(n)
# 时间 最坏 O(n^2)， 平均 O(nlogn)， 空间O(n)


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:

    def height(self, root: TreeNode):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1

    def isBalance(self, root: TreeNode) -> bool:
        if root is None:
            return True
        diff_height = abs(self.height(root.left) - self.height(root.right))
        if diff_height > 1:
            return False
        else:
            return (diff_height <= 1
                    and self.isBalance(root.right)
                    and self.isBalance(root.left))
