import copy


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove(self):
        temp = self.head
        self.head = self.head.next
        temp = None

    def is_empty(self):
        if self.head is None:
            print("Lista jest pusta")
            return True
        print("Lista nie jest pusta")
        return False

    def length(self):
        if self.head is None:
            return 0
        else:
            len = 1
            temp = self.head
            while temp.next:
                len += 1
                temp = temp.next
            return len

    def get(self):
        return self.head.data

    def print_list(self):
        if self.head is None:
            print("[]")
        else:
            print("[", self.head.data, end=" ")
            temp = self.head
            while temp.next is not None:
                print(", ")
                print(temp.next.data, end=" ")
                temp = temp.next
            print("]")

    def add_end(self, node):
        if self.head is None:
            head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def remove_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            temp1 = self.head
            temp2 = None
            while temp1.next:
                temp2 = temp1
                temp1 = temp1.next
            temp2.next = None
            temp1 = None

    def take(self, n):
        new_list = LinkedList()
        m = self.length()
        i = 0
        if n >= 1:
            temp = self.head
            c = copy.deepcopy(temp)
            el = Node(c.data)
            new_list.add(el)
            i += 1
            while i < m and i < n:
                temp = temp.next
                c = copy.deepcopy(temp)
                el = Node(c.data)
                new_list.add_end(el)
                i += 1
        return new_list

    def drop(self, n):
        new_list = LinkedList()
        m = self.length()
        if n >= m or m < 1:
            return new_list
        i = 1
        temp = self.head
        while i < n and i < m:
            temp = temp.next
            i += 1
        c = copy.deepcopy(temp.next)
        el = Node(c.data)
        new_list.add(el)
        temp = temp.next
        while temp.next:
            c = copy.deepcopy(temp.next)
            el = Node(c.data)
            new_list.add_end(el)
            temp = temp.next
        return new_list



if __name__ == "__main__":

    el1 = Node(('AGH', 'Kraków', 1919))
    el2 = Node(('UJ', 'Kraków', 1364))
    el3 = Node(('PW', 'Warszawa', 1915))
    el4 = Node(('UW', 'Warszawa', 1915))
    el5 = Node(('UP', 'Poznań', 1919))
    el6 = Node(('PG', 'Gdańsk', 1945))
    el_temp1 = Node(('AGH', 'Kraków', 1919))
    el_temp2 = Node(('AGH', 'Kraków', 1919))

    #print(el1.data)

    my_list = LinkedList()
    my_list.add(el_temp1)
    my_list.add(el1)
    my_list.print_list()
    print("Usuwam pierwszy element:")
    my_list.remove()
    my_list.print_list()
    print("Sprawdzam czy lista jest pusta:")
    my_list.is_empty()
    print("Dodaje reszte elementow:")
    my_list.add_end(el2)
    my_list.add_end(el3)
    my_list.add_end(el4)
    my_list.add_end(el5)
    my_list.add_end(el6)
    my_list.print_list()
    print("Sprawdzam dlugosc listy:")
    print(my_list.length())
    print("Sprawdzam pierwszy element z listy:")
    print(my_list.get())
    print("Dodaje dodatkowy element na koniec:")
    my_list.add_end(el_temp2)
    my_list.print_list()
    print("I usuwam go:")
    my_list.remove_end()
    my_list.print_list()
    print("Tworze nowa liste z 3 pierwszych elementow listy wejsciowej:")
    new_list1 = my_list.take(3)
    new_list1.print_list()
    print("Tworze nowa liste z pominieciem 4 pierwszych elementow listy wejsciowej:")
    new_list1 = my_list.drop(4)
    new_list1.print_list()
