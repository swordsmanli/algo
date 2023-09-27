# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:singleTon.py
# Time:2023/9/15 13:59
# Author:white_li@trendmicro.com
# version:py3
"""


def singleton(cls):
    instance = {}

    def get_singletone(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_singletone


@singleton
class MyClass:

    def __init__(self, value=0):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val
