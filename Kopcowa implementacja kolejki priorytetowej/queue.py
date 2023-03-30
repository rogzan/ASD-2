#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority

    def __lt__(self, other): #<
        return other.priority > self.priority

    def __gt__(self, other): #>
        return other.priority < self.priority

    def __str__(self):
        return f'{self.priority}:{self.data}'

class Queue:
    def __init__(self):
        self.q = []
        self.size = 0

    def is_empty(self):
        if len(self.q) == 0:
            return True
        return False

    def peek(self):
        return self.q[0]

    def dequeue(self):
        if self.is_empty():
            return None
        to_del = self.q[0]
        n = len(self.q) - 1  # indeks ostatniego elementu
        v = self.q[n]  # zapamietuje ostatni element
        i = 0
        j = self.left(i)  # przeszukiwania od lewego syna
        while j < n:
            if j + 1 < n and self.q[j + 1] > self.q[j]:  # szukam wiekszego syna
                j = j + 1
            if v > self.q[j] or v.priority == self.q[j].priority:
                break
            self.q[j], self.q[i] = self.q[i], self.q[j]  # zamiana elementow
            i = j  # przenosze sie na indeks wiekszego syna
            j = self.left(j)  # aktualizuje indeks parenta
        self.q[i] = v
        self.q.pop()
        self.size -= 1
        return to_del

    def enqueue(self, data, pr):
        new = Node(data, pr)
        self.q.append(new)
        i = len(self.q) - 1   # indeks nowego elementu
        j = self.parent(i)  # indeks rodzica nowego elementu
        while i > 0 and self.q[j] < new:
            self.q[j], self.q[i] = self.q[i], self.q[j]  # zamiana elementow
            i = j  # przenosze sie na indeks parenta
            j = self.parent(i)  # aktualizuje indeks parenta
        self.q[i] = new
        self.size += 1

    def left(self, idx):
        return idx * 2 + 1

    def right(self, idx):
        return idx * 2 + 2

    def parent(self, idx):
        return (idx - 1) // 2

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


queue = Queue()
data = "ALGORYTM"
priority_list = [4, 7, 6, 7, 5, 2, 2, 1]
for i in range(len(priority_list)):
    queue.enqueue(data[i], priority_list[i])
queue.print_tree(0,0)
queue.print_tab()
print(queue.dequeue())
print(queue.peek())
queue.print_tab()
while not queue.is_empty():
    print(queue.dequeue())
queue.print_tab()
