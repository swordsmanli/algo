# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:binaryTree.py
# Time:2023/10/4 20:13
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 144/94/145
# 时间O(n)， 空间最坏O(n), 平均O(logn)

from typing import List


class TreeNode:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # @staticmethod
    # def preorderTraversal(root: TreeNode):
    #     res = []
    #     if not root:
    #         return []
    #     res.append(root.val)
    #     Solution.preorderTraversal(root.left)
    #     Solution.preorderTraversal(root.right)
    #     return res

    def preorderTraversal(self, root: TreeNode, res: List[int]) -> List[int]:
        # def preorder(root: TreeNode):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)

        if not root:
            return []
        res.append(root.val)
        self.preorderTraversal(root.left, res)
        self.preorderTraversal(root.right, res)
        return res

    def midorderTraveral(self, root: TreeNode, res: List[int]):
        if not root:
            return []
        self.midorderTraveral(root.left, res)
        res.append(root.val)
        self.midorderTraveral(root.right, res)
        return res

    def postorderTraveral(self, root: TreeNode, res: List[int]):
        if not root:
            return []
        self.postorderTraveral(root.left, res)
        self.postorderTraveral(root.right, res)
        res.append(root.val)
        return res
