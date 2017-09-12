import queue
from collections import namedtuple
import heapq
import math
import random


def gen_graph(n, low_lim, upp_lim):
    graph = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(random.randint(low_lim, upp_lim))
        graph.append(row)
    return graph


def print_graph(graph):
    for row in graph:
        print(row)
    print()
    return True


def main():
    graph = gen_graph(10, 100, 2500)
    print_graph(graph)
    print(graph[2][4])
    return True


main()
