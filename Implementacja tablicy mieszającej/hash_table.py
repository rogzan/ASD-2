#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def hash_function(self, key):
        if not isinstance(key, int):
            new_key = 0
            for i in key:
                new_key += ord(i)
            key = new_key
        idx = key % (len(self.tab))
        return int(idx)

    def coll_resolution(self, key):
        idx = self.hash_function(key)
        for i in range(len(self.tab)):
            new_idx = (idx + self.c1 * i + self.c2 * (i ** 2)) % (len(self.tab))
            if self.tab[new_idx] is None:
                return new_idx
        return None

    def search(self, key):  # zwraca wartość i indeks w tablicy
        idx = self.hash_function(key)
        if self.tab[idx] and self.tab[idx].key is key:
            return self.tab[idx].value, idx
        else:
            for i in range(len(self.tab)):
                new_idx = (idx + self.c1 * i + self.c2 * (i ** 2)) % (len(self.tab))
                if self.tab[new_idx] and self.tab[new_idx].key is key:
                    return self.tab[new_idx].value, new_idx
            return None


    def insert(self, el):
        key = el.key
        idx = self.hash_function(key)
        value = el.value
        if self.tab[idx] is not None:
            new_idx = self.coll_resolution(key)
            idx = new_idx
        if idx is not None and self.tab[idx] is None:
            self.tab[idx] = el
            return
        if self.search(key) is not None:
            self.tab[self.search(key)[1]].value = value
            return
        else:
            print("Brak miejsca")
            return

    def remove(self, key):
        idx = self.search(key)[1]
        if idx is None:
            print("Brak danej")
            return
        else:
            self.tab[idx] = None

    def __str__(self):
        s = "{"
        for i in range(len(self.tab)):
            if self.tab[i] is None:
                s += "None, "
            elif i == len(self.tab)-1:
                s += str(self.tab[i].key) + ":" + str(self.tab[i].value)
            else:
                s += str(self.tab[i].key) + ":" + str(self.tab[i].value)
                s += ", "
        s += "}"
        return s


if __name__ == "__main__":

    def test1(size, c1, c2):
        table = HashTable(size)
        j = 65
        for i in range(1, 16):
            if i == 6:
                el = Node(18, chr(j))
            elif i == 7:
                el = Node(31, chr(j))
            else:
                el = Node(i, chr(j))
            j += 1
            table.insert(el)
        print(table)
        print(table.search(5))
        print(table.search(14))
        table.insert(Node(5, 'Z'))
        print(table.search(5))
        table.remove(5)
        print(table)
        print(table.search(31))

        table.insert(Node('test', 'W'))
        print(table)

    def test2(size, c1, c2):
        table = HashTable(size)
        j = 65
        for i in range(1, 16):
            el = Node(13 * i, chr(j))
            j += 1
            table.insert(el)
        print(table)

    test1(13, 1, 0)
    test2(13, 1, 0)
    test2(13, 0, 1)
    test1(13, 0, 1)
