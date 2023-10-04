# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:binaryTreeTraveral.py
# Time:2023/10/4 22:28
# Author:white_li@trendmicro.com
# version:py3
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # steps push root node, then loop push right node, left node
    def preorder(self, root: TreeNode):
        if root is None:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # 递归的调用过程是不断往左边走，当左边走不下去了，就打印节点，并转向右边，然后右边继续这个过程。
    def midorder(self, root: TreeNode):

        if root is None:
            return []
        stack = []
        result = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                # left 节点找不到child
                tmp = stack.pop()
                result.append(tmp.val) # 加入left node value
                root = tmp.right
        return result

    # left->right->root, traveral root->right->left, then reverse result
    # O(n), O(n) length of nodes
    def postorder(self, root: TreeNode):
        if root is None:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.insert(0, node.val)  # reverse result
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result
