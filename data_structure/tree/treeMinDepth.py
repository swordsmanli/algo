# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:treeMinDepth.py
# Time:2023/10/8 23:13
# Author:white_li@trendmicro.com
# version:py3
"""
# leetcode 111 二叉树最小深度
# 二叉树最小深度定义是root 节点到叶子节点最小路径上的节点数


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def getMinDepth(self, root: TreeNode):
        if root is None:
            return 0
        else:
            left_depth = self.getMinDepth(root.left)
            right_depth = self.getMinDepth(root.right)
            if root.left and root.right is None:
                return left_depth + 1
            if root.right and root.left is None:
                return right_depth + 1
            return 1 + min(left_depth, right_depth)

    def minDepth(self, root: TreeNode):
        return self.getMinDepth(root)


class Solution2:

    def getMinDepth(self, root: TreeNode):
        if root is None:
            return 0
        else:
            stack = []
            stack.append(root)
            depth = 0
            while len(stack) > 0:
                stack_size = len(stack)
                depth += 1
                for i in range(stack_size):
                    node: TreeNode = stack.pop()
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                    if node.left is None and node.right is None:
                        return depth
