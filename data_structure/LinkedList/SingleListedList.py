# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:SingleListedList.py
# Time:2023/9/18 14:42
# Author:white_li@trendmicro.com
# version:py3
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedNode:

    def __init__(self):
        self.head = None

    def append(self, item):
        node = Node(item)
        if not self.is_empty():
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        else:
            self.head = node

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def items(self):
        cur: Node = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def find_exist(self, data):
        return data in self.items()

    def get_index(self, index):
        if index<0 or index >= self.len():
            raise IndexError("index out of bound error")
        else:
            cur = self.head
            count = 0
            while count < index:
                cur = cur.next
                count += 1
            return cur.data

    def remove(self, item):
        cur = self.head
        pre_node: Node = None
        while cur is not None:
            if cur.data == item:
                if not pre_node:
                    # remove the first one node
                    self.head = cur.next
                else:
                    pre_node.next = cur.next
                return True
            else:
                pre_node = cur
                cur = cur.next
        print(f"not found item{item}, delete failed")
        return False

    def insert_into(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > (self.len()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            # find the node
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def is_empty(self):
        return self.head is None

    def len(self):
        count = 0
        cur: Node = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count
