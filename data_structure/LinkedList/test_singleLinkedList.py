# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:test_singleLinkedList.py
# Time:2023/9/18 15:41
# Author:white_li@trendmicro.com
# version:py3
"""
import unittest
from .SingleListedList import *


class TestSingleLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.list = LinkedNode()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())

    def test_append(self):
        self.list.append(3)
        self.list.append(4)
        self.list.append(5)
        self.assertEqual(self.list.len(), 3)

    def test_len(self):
        self.assertEqual(self.list.len(), 0)
        self.list.append(1)
        self.list.append(2)
        self.assertEqual(self.list.len(), 2)

    def test_remove(self):
        self.list.add(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.len(), 3)
        self.list.remove(2)
        self.assertEqual(self.list.len(), 2)

    def test_get_index(self):
        self.list.append(10)
        self.list.append(33)
        self.list.append(20)
        self.assertEqual(self.list.get_index(0), 10)
        self.assertEqual(self.list.get_index(1),33)
        self.assertEqual(self.list.get_index(2), 20)
        with self.assertRaises(IndexError):
            self.list.get_index(4)
