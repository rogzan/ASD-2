#!/usr/bin/python
# -*- coding: utf-8 -*-

def realloc_and_shift(tab, size, head):
    new = [None for i in range(size)]
    index = 0
    for i in range(head, size // 2):
        if tab[i] is not None:
            new[index] = tab[i]
            index += 1
    for i in range(0, head):
        if tab[i] is not None:
            new[index] = tab[i]
            index += 1
    return new, index


class QueueCircular:
    def __init__(self):
        self.queue = [None for i in range(5)]
        self.size = 5
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return True if self.head == self.tail else False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.head]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.size
            return temp

    def enqueue(self, data):
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        if self.head == self.tail:
            self.queue, self.tail = realloc_and_shift(self.queue, self.size * 2, self.head)
            self.size *= 2
            self.head = 0

    def print_array(self):
        if self.is_empty():
            print("[]")
        else:
            print(my_queue.queue)

    def print_queue(self):
        if self.is_empty():
            print("[]")
        else:
            print("[", end="")
            if self.tail >= self.head:
                print(self.queue[self.head], end="")
                for i in range(self.head + 1, self.tail):
                    if self.queue[i] is not None:
                        print(",", end="")
                        print(self.queue[i], end="")
            else:
                print(self.queue[self.head], end="")
                for i in range(self.head + 1, self.size):
                    if self.queue[i] is not None:
                        print(",", end="")
                        print(self.queue[i], end="")
                for i in range(0, self.head):
                    if self.queue[i] is not None:
                        print(",", end="")
                        print(self.queue[i], end="")
            print("]")

my_queue = QueueCircular()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue.dequeue())
print(my_queue.peek())
my_queue.print_queue()
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.print_array()
while not my_queue.is_empty():
    print(my_queue.dequeue())
my_queue.print_queue()
