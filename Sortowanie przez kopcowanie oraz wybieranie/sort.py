# !/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time


# 1 część

class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority

    def __lt__(self, other):  # <
        return other.priority >= self.priority

    def __gt__(self, other):  # >
        return other.priority < self.priority

    def __repr__(self):
        return f'{self.priority}:{self.data}'


class Heap:
    def __init__(self, tab):
        self.q = tab
        self.size = len(self.q)
        # self.heapify()

    def is_empty(self):
        if len(self.q) == 0:
            return True
        return False

    def peek(self):
        return self.q[0]

    def left(self, idx):
        return idx * 2 + 1

    def right(self, idx):
        return idx * 2 + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def heap_sort(self):
        n = self.size
        for i in range(n // 2, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.q[i], self.q[0] = self.q[0], self.q[i]
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < n and self.q[i] < self.q[l]:  largest = l
        if r < n and self.q[largest] < self.q[r]:  largest = r
        if largest != i:
            self.q[i], self.q[largest] = self.q[largest], self.q[i]
            self.heapify(n, largest)

    def select_sort_swap(self):
        for i in range(len(self.q)):
            min_idx = i
            for j in range(i + 1, len(self.q)):
                if self.q[min_idx] > self.q[j]:
                    min_idx = j
            self.q[i], self.q[min_idx] = self.q[min_idx], self.q[i]

    def select_sort_switch(self):
        for i in range(len(self.q)):
            min_idx = i
            for j in range(i + 1, len(self.q)):
                if self.q[min_idx] > self.q[j]:
                    min_idx = j
            key = self.q[min_idx]
            while min_idx > i:
                self.q[min_idx] = self.q[min_idx - 1]
                min_idx -= 1
            self.q[i] = key

    def print_tab(self):
        if self.is_empty():
            print("{}")
            return
        size = len(self.q)
        print('{', end=' ')
        for i in range(size - 1):
            print(self.q[i], end=', ')
        if self.q[size - 1]: print(self.q[size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        size = len(self.q)
        if idx < size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.q[idx] if self.q[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


data = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

tab1 = []
for i in data:
    tab1.append(Node(i[1], i[0]))
heap1 = Heap(tab1)

heap1.print_tab()
heap1.print_tree(0, 0)
heap1.heap_sort()
heap1.print_tab()
heap1.print_tree(0, 0)

tab2 = []
for i in range(10000):
    x = int(random.random() * 100)
    tab2.append(Node(x, x))

heap2 = Heap(tab2)
t_start = time.perf_counter()
heap2.heap_sort()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# 2 część

tab3 = []
for i in data:
    tab3.append(Node(i[1], i[0]))
heap3 = Heap(tab3)

heap3.print_tab()
heap3.select_sort_swap()
heap3.print_tab()
heap3.print_tree(0, 0)
# selection sort z zamianą miejsc nie jest stabilny

tab4 = []
for i in data:
    tab4.append(Node(i[1], i[0]))
heap4 = Heap(tab4)

heap4.print_tab()
heap4.select_sort_switch()
heap4.print_tab()
heap4.print_tree(0, 0)
# selection sort w wersji z przesunięciem elementów jest stabilny

tab5 = []
for i in range(10000):
    x = int(random.random() * 1000)
    tab5.append(Node(x, x))

heap5 = Heap(tab5)
t_start = time.perf_counter()
heap5.select_sort_swap()
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
# Czas obliczeń obu algorytmów sortowania przez wybieranie jest znacznie dłuższy 
# od czasu wykonania algorytmu sortowania przez kopcowanie
