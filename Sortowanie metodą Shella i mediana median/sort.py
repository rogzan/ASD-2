# !/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time


# część I

def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


def shell_sort(tab):
    n = len(tab)
    h = n // 2
    while h > 0:  # gdy h=1 - koniec sortowania
        j = h
        while j < n:
            i = j - h
            while i >= 0:
                if tab[i + h] > tab[i]:
                    break
                else:
                    tab[i + h], tab[i] = tab[i], tab[i + h]
                i = i - h
            j += 1
        h = h // 2
    return tab


# część II

def quick_sort(tab, m_fives):
    if len(tab) == 0:
        return tab
    if m_fives:  # magiczne piątki
        div = pivot(tab)
    else:  # wersja klasyczna
        div = tab[0]
    lt = []  # elementy mniejsze od dzielącego
    eq = []  # elementy równe dzielącemu
    gt = []  # elementy większe od dzielącego
    while len(tab) > 0:
        y = tab.pop(0)
        if y < div:
            lt.append(y)
        elif y > div:
            gt.append(y)
        else:
            eq.append(y)
    return quick_sort(lt, m_fives) + eq + quick_sort(gt, m_fives)


def pivot(tab):
    t = tab
    while len(t) > 1:
        med_list = []
        sublists = [t[j:j + 5] for j in range(0, len(t), 5)]
        for list in sublists:
            if len(list) == 5:
                med = median_5(*list)
                med_list.append(med)
            if len(list) == 4:
                med = median_4(*list)
                med_list.append(med)
            if len(list) == 3:
                med = median_3(*list)
                med_list.append(med)
            if len(list) == 2:
                med = median_2(*list)
                med_list.append(med)
            if len(list) == 1:
                med_list.append(*list)
        t = med_list
    return t[0]


def median_2(a, b):
    return (a + b) / 2


def median_3(a, b, c):
    return max(min(a, b), min(c, max(a, b)))


def median_4(a, b, c, d):
    f = max(min(a, b), min(c, d))  # usuwa najmniejsza z 4
    g = min(max(a, b), max(c, d))  # usuwa największą z 4
    return median_2(f, g)


def median_5(a, b, c, d, e):
    f = max(min(a, b), min(c, d))  # usuwa najmniejsza z 4
    g = min(max(a, b), max(c, d))  # usuwa największą z 4
    return median_3(e, f, g)


# testy

tab1 = []
tab2 = []
tab3 = []
tab4 = []

for i in range(10000):
    x = int(random.random() * 100)
    tab1.append(x)
    tab2.append(x)
    tab3.append(x)
    tab4.append(x)

# część I

# shell sort
t_start = time.perf_counter()
shell_sort(tab1)
t_stop = time.perf_counter()
print("Czas obliczeń - shell sort:", "{:.7f}".format(t_stop - t_start))

# insertion sort
t_start = time.perf_counter()
insertion_sort(tab2)
t_stop = time.perf_counter()
print("Czas obliczeń - insertion sort:", "{:.7f}".format(t_stop - t_start))


# część II

# quick sort klasyczny
t_start = time.perf_counter()
quick_sort(tab3, False)
t_stop = time.perf_counter()
print("Czas obliczeń - quick sort klasyczny:", "{:.7f}".format(t_stop - t_start))

# quick sort magiczne piątki
t_start = time.perf_counter()
quick_sort(tab3, True)
t_stop = time.perf_counter()
print("Czas obliczeń - quick sort magiczne piątki:", "{:.7f}".format(t_stop - t_start))
