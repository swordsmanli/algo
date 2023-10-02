# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:symbolMatch.py
# Time:2023/10/2 10:43
# Author:white_li@trendmicro.com
# version:py3
"""

#leetcode 20, valid parentheses


class Solution:

    @staticmethod
    def is_match_symbol(s: str):
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(len(s)):
            if stack and s[i] in dic:
                if stack[-1] == dic[s[i]]:
                    stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0
