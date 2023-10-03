# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:topKFrequecyNunmber.py
# Time:2023/10/3 17:39
# Author:white_li@trendmicro.com
# version:py3
"""

from typing import List
import heapq


# leetcode 347 find top k frequency item
# minimum2 heap

class Solution:

    @staticmethod
    def topKLeastFrequncy(nums: List[int], k: int):
        map_counter = {}
        hpq = []
        for i in range(len(nums)):
            map_counter[nums[i]] = map_counter.get(nums[i], 0) - 1
        for key, freq in map_counter.items():
            heapq.heappush(hpq, (freq, key))
            if len(hpq) > k:
                heapq.heappop(hpq)
        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(hpq)[1]
        return res

    @staticmethod
    def topKFrequency(nums: List[int], k: int):
        map_counter = {}
        hpq = []
        for i in range(len(nums)):
            map_counter[nums[i]] = map_counter.get(nums[i], 0) + 1
        for n, c in map_counter.items():
            heapq.heappush(hpq, (c, n))
            if len(hpq) > k:
                heapq.heappop(hpq)
        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(hpq)[1]
        return res


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2, 3, 3, 3, 1]
    k = 2
    Solution.topKLeastFrequncy(nums, k)