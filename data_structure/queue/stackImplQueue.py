# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:stackImplQueue.py
# Time:2023/9/30 17:14
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 232 implement queue using stack


class MyStackQueue:

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def pop(self):
        if not self.out_stack:
            if self.in_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
        if not self.empty():
            return self.out_stack.pop()
        else:
            print("empty queue")
            return None

    def push(self, x):
        self.in_stack.append(x)

    def peek(self):
        res = self.pop()
        self.push(res)
        return res

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
