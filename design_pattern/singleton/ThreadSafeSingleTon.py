# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:ThreadSafeSingleTon.py
# Time:2023/9/15 14:35
# Author:white_li@trendmicro.com
# version:py3
"""
import threading


class ThreadSafeSingleTon:

    _lock = threading.Lock()
    _instance = None

    def __int__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    @classmethod
    def instance(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = cls()
        return cls._instance

