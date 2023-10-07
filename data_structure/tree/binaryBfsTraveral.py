# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:binaryBfsTraveral.py
# Time:2023/10/7 22:27
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 102 二叉树层序遍历
# leetcode 226 反转二叉树


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def isSymmetric(root: TreeNode) -> bool:
        return Solution.bfsTraveral2(root) == Solution.inventTree(root)

    @staticmethod
    def inventTree(root: TreeNode):
        queue = []
        result = []
        if root is None:
            return []
        else:
            queue.append(root)
            while len(queue) > 0:
                size = len(queue)
                node: TreeNode = queue.pop(0)
                result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            return result

    @staticmethod
    def bfsTraveral2(root: TreeNode):
        queue = []
        if root is None:
            return []
        else:
            queue.append(root)
            result = []
            while len(queue) > 0:
                size = len(queue)
                for i in range(size):
                    node: TreeNode = queue.pop(0)
                    result.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return result

    @staticmethod
    def bfsTraveral(root: TreeNode):
        queue = []
        if root is None:
            return []
        else:
            queue.append(root)
            result = []
            while len(queue) > 0:
                level_node = []
                size = len(queue)
                for i in range(size):
                    node: TreeNode = queue.pop(0)
                    level_node.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(level_node)
            return result
