# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:kruskal.py
# Time:2023/9/25 16:51
# Author:white_li@trendmicro.com
# version:py3
"""


class Edge:

    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __str__(self):
        return f"node({self.s}) --{self.w}-- node({self.e})"


class UfsFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, x, y):
        # find common ancestor
        x_i, y_i = self.find(x), self.find(y)
        if x_i != y_i:
            # set new parent
            self.parent[x] = y

    def find(self, x):
        if self.parent[x] != x:
            # compress find path, store path result, recursive find
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


def kruskal(edges, n):
    if n > 1:
        edge_list = list()
        for e in edges:
            u, v, w = e
            edge_list.append(Edge(u, v, w))
        edge_list.sort()
        ufs = UfsFind(len(edge_list))
        min_spin_tree = list()
        for e in edge_list:
            if not ufs.is_connected(e.s, e.e):
                ufs.union(e.s, e.e)
                min_spin_tree.append(e)
                if len(min_spin_tree) == n-1:
                    break
        for i in min_spin_tree:
            print(i)
    else:
        print("n must bigger than 1")

if __name__ == '__main__':
    edges_list = [(1, 2, 1.3), (1, 3, 2.1), (1, 4, 0.9), (1, 5, 0.7), (1, 6, 1.8), (1, 7, 2.0), (1, 8, 1.5),
                  (2, 3, 0.9), (2, 4, 1.8), (2, 5, 1.2), (2, 6, 2.6), (2, 7, 2.3), (2, 8, 1.1),
                  (3, 4, 2.6), (3, 5, 1.7), (3, 6, 2.5), (3, 7, 1.9), (3, 8, 1.0),
                  (4, 5, 0.7), (4, 6, 1.6), (4, 7, 1.5), (4, 8, 0.9),
                  (5, 6, 0.9), (5, 7, 1.1), (5, 8, 0.8),
                  (6, 7, 0.6), (6, 8, 1.0),
                  (7, 8, 0.5)]
    kruskal(edges_list, 1)
