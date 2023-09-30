# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:wordsStringReverse.py
# Time:2023/9/29 16:37
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 151, double index, left and right to define a word, O(n)


class Solution:

    @staticmethod
    def reverse(s: str) -> str:
        sr = list(' ' + s)
        i = j = len(sr)-1
        res = []
        while i >= 0:
            # find word tail
            while sr[i] == ' ' and i >= 0:
                i -= 1
            j = i
            # find work head
            while sr[i] != ' ' and i >= 0:
                i -= 1
            if j > i:
                # py slice [left index, right index+1)
                res.append(''.join(sr[i+1:j+1]))
        return ' '.join(res)


if __name__ == '__main__':
    print(Solution.reverse("i am a programmer"))