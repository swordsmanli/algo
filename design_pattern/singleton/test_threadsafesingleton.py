# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:test_threadsafesingleton.py
# Time:2023/9/15 14:42
# Author:white_li@trendmicro.com
# version:py3
"""
import threading
import unittest
from ThreadSafeSingleTon import ThreadSafeSingleTon


class TestThreadSafeSingleTon(unittest.TestCase):

    def test_singleton_instance(self):
        t1 = ThreadSafeSingleTon.instance()
        t2 = ThreadSafeSingleTon.instance()
        self.assertIs(t1, t2, "instance equals")

    def test_singleton_value(self):
        t1 = ThreadSafeSingleTon.instance()
        t2 = ThreadSafeSingleTon.instance()
        t1.set_value(100)
        self.assertEquals(t2.get_value(), 100, "should be equals")

    def test_multithreading_create_instance(self):
        instances = []
        threads = []

        def create_instance():
            instances.append(ThreadSafeSingleTon.instance())

        threads = [threading.Thread(target=create_instance) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        instance_0 = instances[0]
        for instance in instances:
            self.assertIs(instance, instance_0, "multi-thread creation instance should be equals")