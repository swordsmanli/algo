# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:test_singletone.py
# Time:2023/9/15 14:05
# Author:white_li@trendmicro.com
# version:py3
"""

import unittest
from algo.design_pattern.singleton.singleTon import MyClass


class TestSingleTon(unittest.TestCase):

    def test_singletone_class(self):
        mc1 = MyClass(1)
        mc2 = MyClass(2)
        self.assertIs(mc1, mc2, "MyClass should be this same instance")

    def test_set_singleton_value(self):

        m1 = MyClass(1)
        m1.set_value(2)
        m2 = MyClass()
        self.assertEquals(
            m2.get_value(),
          2,
          "attribute in one instance should be equal to the other instance"
        )
        m2.set_value(10)
        self.assertEquals(m2.get_value(), 10, "attribute set in other instance should affect another instance value")
