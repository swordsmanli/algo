# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:trapRainWater.py
# Time:2023/10/3 20:56
# Author:white_li@trendmicro.com
# version:py3
"""

# leetcode 42

from typing import List


class Solution:

    # O(n)
    @staticmethod
    def trapRainWaterDP(height: List[int]):
        if len(height) <= 2:
            return 0
        else:
            left_max_height = [0] * len(height)
            right_max_height = [0] * len(height)

            left_max_height[0] = height[0]
            right_max_height[len(height)-1] = height[len(height)-1]
            for i in range(1, len(height)):
                # find largest height at left at pos i
                left_max_height[i] = max(left_max_height[i-1], height[i])
            for i in range(len(height)-2, -1, -1):
                # find largest height at right at pos i
                right_max_height[i] = max(right_max_height[i+1], height[i])
            sum_ = 0
            for i in range(len(height)):
                h = min(left_max_height[i], right_max_height[i]) - height[i]
                if h > 0:
                    sum_ += h
            return sum_

    # O(n^2)
    @staticmethod
    def trapRainWater(height: List[int]):
        sum = 0
        for i in range(len(height)):
            if i == 0 or i == (len(height) - 1):
                continue
            else:
                left_index, right_index = height[i], height[i]
                for l in range(0, i):
                    if height[l] > left_index:
                        left_index = height[l]
                for r in range(i + 1, len(height)):
                    if height[r] > right_index:
                        right_index = height[r]
                h = min(right_index, left_index) - height[i]
                if h > 0:
                    sum += h
        return sum