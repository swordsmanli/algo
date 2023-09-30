# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:queueImplStack.py
# Time:2023/9/30 17:49
# Author:white_li@trendmicro.com
# version:py3
"""
#leetcode 225 implement stack using queue
'''
swap q1 with q2 on every push
|__2__|      q1_|5|4|____     q1 _|5|4|2|______
|__4__|      
|__5__|      q2_2________     q2 ______________

if only one q, append(q-1) element to q1 using pop(0)
'''


class MyQueueStack:

    def __init__(self):
        # q1 used to pop element
        # q2 used to push element
        self.q1 = []

    def pop(self):
        if self.empty():
            print("empty stack")
            return None
        else:
            return self.q1.pop(0)

    def push(self, x):
        self.q1.append(x)
        size = len(self.q1) - 1
        while size:
            size -= 1
            self.q1.append(self.q1.pop(0))

    def top(self):
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


class MyDoubleQueueStack:

    def __init__(self):
        # q1 used to pop element
        # q2 used to push element
        self.q1, self.q2 = [], []

    def pop(self):
        if self.empty():
            print("empty stack")
            return None
        else:
            return self.q1.pop(0)

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
