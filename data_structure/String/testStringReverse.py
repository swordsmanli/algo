# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:testStringReverse.py
# Time:2023/9/29 07:51
# Author:white_li@trendmicro.com
# version:py3
"""
import unittest
from reverse import Solution
from wordsStringReverse import Solution as Solution2


class TestStringReverse(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_odd_string_reverse(self):
        original_string = "abcde"
        two_reverse = Solution(Solution(original_string).reversed()).reversed()
        self.assertEquals(original_string, two_reverse)

    def test_even_string_reverse(self):
        original_string = "abcdef"
        two_reverse = Solution(Solution(original_string).reversed()).reversed()
        self.assertEquals(original_string, two_reverse)

    def test_reverse_k1(self):
        original_string = "abcdefg"
        k = 2
        self.assertEquals(Solution(original_string).reverseK(k), "bacdfeg")

    def test_reverse_k2(self):
        original_string = "abcd"
        k = 2
        self.assertEquals(Solution(original_string).reverseK(k), "bacd")

    def test_words_reverse(self):
        original_string = "i am a programmer"
        self.assertEquals(Solution2.reverse(original_string), ' '.join(original_string.split(' ')[::-1]))