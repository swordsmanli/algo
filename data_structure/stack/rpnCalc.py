# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:rpnCalc.py
# Time:2023/10/2 11:17
# Author:white_li@trendmicro.com
# version:py3
"""

#leetcode 150, calculate rpn result

from typing import List


class Solution:

    @staticmethod
    def calcRpn(e: List[str]):
        stack = []
        for i in e:
            if i == "+":
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num2 + num1)
            elif i == "-":
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num2 - num1)
            elif i == '*':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num2 * num1)
            elif i == '/':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(num2 / num1)
            else:
                stack.append(int(i))
        return stack[-1]
