#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def nil():
    return Node()


def cons(el, lst):
    if is_empty(lst):
        new = nil()
        new.data = el
        return new
    new = nil()
    new.data = el
    new.next = lst
    return new


def first(lst):
    if is_empty(lst):
        return None
    res = lst.data
    return res


def rest(lst):
    if lst.next is None:
        return None
    temp = lst.next
    return temp


def is_empty(lst):
    if lst is None or lst.data is None or lst == "":
        return True
    return False


def create():
    return nil()


def add(el, lst):  # dodanie elementu na początek listy
    return cons(el, lst)


def add_end(el, lst):
    if is_empty(lst):
        return cons(el, lst)  # dojście do końca i wstawienie tam elementu
    else:
        first_el = first(lst)  # podział listy na: pierwszy element
        rest_lst = rest(lst)  # i całą resztę
        recreated_lst = add_end(el,
                                rest_lst)  # 'zejście 'w dół' rekurencji z przekazaniem dodawanego elementu, przy powrocie 'w górę' zwracana jest odtworzona lista
        return cons(first_el, recreated_lst)  # cons dołącza pierwszy element do 'odtwarzanej' przez rekurencję listy
        # zmienne first-el, rest_lst i recreated_lst są wprowadzone pomocniczo, dla wyjaśnienia działania funkcji


def remove_end(lst):
    if length(lst) == 2 or is_empty(lst):
        return cons(first(lst), None)
    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        recreated_lst = remove_end(rest_lst)
        return cons(first_el, recreated_lst)


def remove(lst):  # usunięcie elementu z początku  listy
    return rest(lst)


def length(lst):
    if is_empty(lst):
        return 0
    else:
        return 1 + length(rest(lst))


def get(lst):
    if is_empty(lst):
        return None
    else:
        return first(lst)


def print_list(lst):
    s = "[" + print_list_p(lst, "") + "]"
    print(s)


def print_list_p(lst, s):
    if length(lst) == 1:
        s = str(first(lst))
        return s
    elif is_empty(lst):
        s = ""
    else:
        s += str(first(lst)) + ", " + print_list_p(rest(lst), s)
    return s


def take(lst, n):
    if n >= length(lst):
        return lst
    elif n == 0:
        return nil()
    elif n == 1:
        return cons(first(lst), None)
    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        recreated_lst = take(rest_lst, n-1)
        return cons(first_el, recreated_lst)

def drop(lst, n):
    if n >= length(lst):
        return nil()
    elif n == 0:
        return lst
    elif n == 1:
        return rest(lst)
    else:
        rest_lst = rest(lst)
        return drop(rest_lst, n-1)


if __name__ == "__main__":
    el1 = ('AGH', 'Kraków', 1919)
    el2 = ('UJ', 'Kraków', 1364)
    el3 = ('PW', 'Warszawa', 1915)
    el4 = ('UW', 'Warszawa', 1915)
    el5 = ('UP', 'Poznań', 1919)
    el6 = ('PG', 'Gdańsk', 1945)
    el_temp1 = ('UJ', 'Kraków', 1364)
    el_temp2 = ('UP', 'Poznań', 1919)

    print("Tworzę pustą listę:")
    my_list = create()
    print_list(my_list)
    print("Dodaję 2 razy element na początek listy:")
    my_list = add(el1, my_list)
    my_list = add(el_temp1, my_list)
    print_list(my_list)
    print("Usuwam pierwszy element:")
    my_list = remove(my_list)
    print_list(my_list)
    print("Sprawdzam czy lista jest pusta:")
    print(is_empty(my_list))
    print("Dodaje reszte elementow:")
    my_list = add_end(el2, my_list)
    my_list = add_end(el3, my_list)
    my_list = add_end(el4, my_list)
    my_list = add_end(el5, my_list)
    my_list = add_end(el6, my_list)
    print_list(my_list)
    print("Sprawdzam dlugosc listy:")
    print(length(my_list))
    print("Sprawdzam pierwszy element z listy:")
    print(get(my_list))
    print("Dodaje dodatkowy element na koniec:")
    my_list = add_end(el_temp2, my_list)
    print_list(my_list)
    print("I usuwam go:")
    my_list = remove_end(my_list)
    print_list(my_list)
    print("Tworze nowa liste z 3 pierwszych elementow listy wejsciowej:")
    new_list1 = take(my_list, 3)
    print_list(new_list1)
    print("Tworze nowa liste z pominieciem 4 pierwszych elementow listy wejsciowej:")
    new_list2 = drop(my_list, 4)
    print_list(new_list2)
