# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:treeMaxDepth.py
# Time:2023/10/8 22:48
# Author:white_li@trendmicro.com
# version:py3
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def getDepth(root: TreeNode):
        if root is None:
            return 0
        depth = max(Solution.getDepth(root.left), Solution.getDepth(root.right)) + 1
        return depth

    @staticmethod
    def maxDepth(root: TreeNode):
        return Solution.getDepth(root)


class Solution2:

    @staticmethod
    def getMaxDepth(root: TreeNode):
        stack = []
        if root is None:
            return 0
        else:
            stack.append(root)
            depth = 0
            while len(stack) > 0:
                stack_size = len(stack)
                depth += 1
                for i in range(stack_size):
                    node: TreeNode = stack.pop()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            return depth
