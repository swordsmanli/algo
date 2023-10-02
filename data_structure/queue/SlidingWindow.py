# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:SlidingWindow.py
# Time:2023/10/2 11:35
# Author:white_li@trendmicro.com
# version:py3
"""

#leetcode 239
# 单调队列实现 滑动窗口最大值

from typing import List
from collections import deque


class MonoQueue:
    '''
    单调递减队列
    '''
    def __init__(self):
        self.q = deque()

    def push(self, value):
        # 保持队头元素最大
        # 对位加入元素大于对头元素，不断弹出队尾元素
        while self.q and value > self.q[-1]:
            self.q.pop()
        # 加入元素
        self.q.append(value)

    def pop(self, value):
        if self.q and value == self.q[0]:
            self.q.popleft()

    def front(self):
        # 返回队头元素
        return self.q[0]


def maxSlidingWindown(num: List[int], k: int) -> List[int]:
    mono_q = MonoQueue()
    result = []
    for i in range(k):
        mono_q.push(num[i])
    result.append(mono_q.front())
    for j in range(k, len(num)):
        # 滑动窗口
        mono_q.pop(num[j-k]) # 删除左窗口元素
        mono_q.push(num[j]) # 插入右窗口元素
        result.append(mono_q.front())  # 返回窗口最大值
    return result


if __name__ == '__main__':
    maxSlidingWindown([2,4,-2,-4,3,1,5],4)