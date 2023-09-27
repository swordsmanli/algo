# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:ufs.py
# Time:2023/9/25 14:09
# Author:white_li@trendmicro.com
# version:py3
"""


class UfsArray:

    def __init__(self, n):
        self.idx = [i for i in range(n)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            for i in range(len(self.idx)):
                if self.idx[i] == x:
                    self.idx[i] = y
            return True

    def find(self, x):
        return self.idx[x]

    def is_connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

