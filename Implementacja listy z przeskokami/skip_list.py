#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import random

class Node:
    def __init__(self, key=None, value=None, height=0):
        self.key = key
        self.value = value
        self.height = height
        self.next = [None] * height


class SkipList:
    def __init__(self, max_height):
        self.head = Node()
        self.max_lvl = max_height

    def randomLevel(self, p=0.5):
        lvl = 1
        while random() < p and lvl < self.max_lvl:
            lvl = lvl + 1
        return lvl

    def search(self, key, update=None):
        if update is None:
            update = self.updateList(key)
        if len(update) > 0:
            el = update[0].next[0]
            if el is not None and el.key == key:
                return el
        return None

    def updateList(self, key):
        x = self.head
        update = [None] * len(x.next)
        for i in reversed(range(len(x.next))):
            while x.next[i] is not None and x.next[i].key < key:
                x = x.next[i]
            update[i] = x
        return update

    def insert(self, key, val):
        node = Node(key, val, self.randomLevel())

        self.max_lvl = max(self.max_lvl, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(key)
        x = self.search(key, update)
        if x is None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
        else:
            x.value = val

    def delete(self, key):
        update = self.updateList(key)
        x = self.search(key, update)
        if x is not None:
            for i in range(len(x.next)):
                update[i].next[i] = x.next[i]

    def displayList_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []  # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.next[0]
        for lvl in range(self.max_lvl - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

    def __str__(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        res = "["
        while node is not None:
            res += str(node.key) + ":" + node.value
            node = node.next[0]
            if node:
                res += ", "
        res += "]"
        return res


slist = SkipList(3)  # 3 - maks wysokość
j = 65
for i in range(1, 16):
    slist.insert(i, chr(j))
    j += 1
slist.displayList_()
print(slist.search(2).value)
slist.insert(2, 'Z')
print(slist.search(2).value)
slist.delete(5)
slist.delete(6)
slist.delete(7)
print(slist)
slist.insert(6, 'W')
print(slist)
