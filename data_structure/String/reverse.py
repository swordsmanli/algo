# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:reverse.py
# Time:2023/9/29 07:26
# Author:white_li@trendmicro.com
# version:py3
"""


from typing import List


class Solution:

    def __init__(self, s: str):
        self.s_array = list(s)

    # leetcode 344
    def reversed(self) -> str:
        s = self.s_array
        i = 0
        while (i < (len(s)-1)//2):
            j = len(s)-1 - i
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
        return ''.join(s)

    #leetcode 541
    def reverseK(self, k: int):
        if k <= 0:
            print("k parameter should be larger than 1 and must be integer")

        else:
            size = len(self.s_array)
            for i in range(0, size, 2*k):
                left, right = i, min(i+k-1, size-1)
                while left < right:
                    t = self.s_array[left]
                    self.s_array[left] = self.s_array[right]
                    self.s_array[right] = t
                    left += 1
                    right -= 1
        return ''.join(self.s_array)


if __name__ == "__main__":
    test_str = "abcd"
    teststr = list(test_str)
    print("raw string", test_str)
    print("reversed string:", Solution(teststr).reverseK(2))