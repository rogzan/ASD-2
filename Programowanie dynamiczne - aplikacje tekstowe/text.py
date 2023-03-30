#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def string_compare_rec(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    exch = string_compare_rec(P, T, i - 1, j - 1) + int(P[i] != T[j])
    inse = string_compare_rec(P, T, i, j - 1) + 1
    dele = string_compare_rec(P, T, i - 1, j) + 1

    min_cost = min(exch, inse, dele)
    return min_cost


def string_compare_pd(P, T):
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D[0])):
        D[0][i] = i
    for i in range(len(D)):
        D[i][0] = i

    R = [['X' for i in range(len(T))] for j in range(len(P))]
    for i in range(1, len(R[0])):
        R[0][i] = "I"
    for i in range(1, len(R)):
        R[i][0] = "D"

    for i in range(1, len(D)):
        for j in range(1, len(D[0])):
            exch = D[i - 1][j - 1] + int(P[i] != T[j])
            inse = D[i][j - 1] + 1
            dele = D[i - 1][j] + 1

            min_op = min(exch, inse, dele)
            D[i][j] = min_op

            if min_op == exch:
                if P[i] == T[j]:
                    R[i][j] = 'M'
                else:
                    R[i][j] = 'S'
            elif min_op == inse:
                R[i][j] = 'I'
            else:
                R[i][j] = 'D'

    return D[len(D) - 1][len(D[0]) - 1], R


def path(R):
    res = []
    i = len(R) - 1
    j = len(R[0]) - 1
    el = R[i][j]

    while el != "X":
        el = R[i][j]
        res.append(el)

        if el == "M" or el == "S":
            i -= 1
            j -= 1
        elif el == "I":
            j -= 1
        elif el == "D":
            i -= 1

    return res[::-1][1::]


def match(P, T):
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D)):
        D[i][0] = i


    for i in range(1, len(D)):
        for j in range(1, len(D[0])):
            exch = D[i - 1][j - 1] + int(P[i] != T[j])
            inse = D[i][j - 1] + 1
            dele = D[i - 1][j] + 1

            min_op = min(exch, inse, dele)
            D[i][j] = min_op

    # punt startowy:
    m = sys.maxsize
    min_idx = 0
    for i in range(len(D[0])):
        if D[len(D) - 1][i] < m:
            m= D[len(D) - 1][i]
            min_idx = i

    return min_idx - len(P) + 2


def l_c_sub(P, T):
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for i in range(len(D[0])):
        D[0][i] = i
    for i in range(len(D)):
        D[i][0] = i

    for i in range(1, len(D)):
        for j in range(1, len(D[0])):
            if P[i] == T[j]:
                exch = D[i - 1][j - 1]
            else:
                exch = D[i - 1][j - 1] + 100
            inse = D[i][j - 1] + 1
            dele = D[i - 1][j] + 1

            min_op = min(exch, inse, dele)
            D[i][j] = min_op

    i = len(D) - 1
    j = len(D[0]) - 1
    idx = D[i][j]
    lcs = [""] * (idx + 1)

    while i > 0 and j > 0:
        if P[i] == T[j]:
            lcs[idx - 1] = P[i]
            i -= 1
            j -= 1
            idx -= 1

        elif D[i - 1][j] > D[i][j - 1]:
            j -= 1
        else:
            i -= 1
    return "".join(lcs)


# a
P1 = ' kot'
T1 = ' pies'
print(string_compare_rec(P1, T1, len(P1) - 1, len(T1) - 1))

# b
P2 = ' biały autobus'
T2 = ' czarny autokar'
cost, _ = string_compare_pd(P2, T2)
print(cost)

# c
P3 = ' thou shalt not'
T3 = ' you should not'
cost, parent = string_compare_pd(P3, T3)
path = path(parent)
print(path)

# d
P4 = ' bin'
T4 = ' mokeyssbanana'
idx = match(P4, T4)
print(idx)

# e
P5 = ' democrat'
T5 = ' republican'
res = l_c_sub(P5, T5)
print(res)

# f
T6 = ' 243517698'
l = []
for el in range(1, len(T6)):
    l.append(el)
l = sorted(l)
P6 = " "
for el in l:
    P6 += str(el)
res = l_c_sub(P6, T6)
print(res)
