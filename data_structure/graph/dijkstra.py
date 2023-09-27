# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File:dijkstra.py
# Time:2023/9/26 14:00
# Author:white_li@trendmicro.com
# version:py3
"""

Max = float('inf')

matrix = [
    [0, 10, Max, 4, Max, Max],
    [10, 0, 8, 2, 6, Max],
    [Max, 8, 0, 15, 1, 5],
    [4, 2, 15, 0, 6, Max],
    [Max, 6, 1, 6, 0, 12],
    [Max, Max, 5, Max, 12, 0]
]

# algorithm steps
# step1 init start node and distance table
# scan node with min distance, record index and update min_value
# update distance array, compare start node go through min index node with existed distance node from start node


def dijkstra(start, graph):
    size_nodes = len(matrix)
    visited_nodes = [False] * size_nodes
    distance = [Max] * size_nodes
    # init start node
    distance[start] = 0
    # visited all nodes
    while visited_nodes.count(False):
        min_value = Max
        min_value_index = -1

        # scanning minium distance node
        for i in range(size_nodes):
            if not visited_nodes[i] and distance[i] < min_value:
                min_value_index = i
                min_value = distance[i]

        visited_nodes[min_value_index] = True

        # update distance array
        # for example, i = B, min_index=D,
        # min(A->B, A->D->B) = min(A->B, A->D + matrix[D][B])
        # distance[B] = min(distance[B], distance[D]+ matrix[D][B])
        for i in range(size_nodes):
            distance[i] = min(distance[i], distance[min_value_index] + matrix[min_value_index][i])

    return distance


if __name__ == '__main__':
    start = int(input("please input start node id:"))
    print(dijkstra(start, matrix))
