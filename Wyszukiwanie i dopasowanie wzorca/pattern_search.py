#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


def naive_search(W, S):  # W - wzorzec, S - tekst
    N = len(W)
    M = len(S)
    num_comp = 0
    res = []

    for m in range(M - N + 1):
        i = 0
        while i < N:
            num_comp += 1
            if S[m + i] != W[i]:
                break
            i += 1

        if i == N:
            res.append(m)

    return len(res), num_comp


def hash(word):
    hw = 0
    N = len(word)
    d = 256
    q = 101  # liczba pierwsza
    for i in range(N):  # N - to długość wzorca
        hw = (hw * d + ord(word[
                               i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń

    return hw


def rabin_karp_search(W, S):
    N = len(W)
    M = len(S)
    hW = hash(W)
    num_comp = 0
    res = []

    for m in range(M - N + 1):
        num_comp += 1
        hS = hash(S[m:m + N])
        if hS == hW:
            if S[m:m + N] == W:
                res.append(m)

    return len(res), num_comp


def rabin_karp_search_2(W, S):
    N = len(W)
    M = len(S)
    hW = hash(W)
    num_comp = 0
    coll = 0
    res = []

    d = 256
    q = 101  # liczba pierwsza
    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    for m in range(M - N + 1):
        num_comp += 1
        if m == 0:
            hS = hash(S[m:m + N])
        else:
            hS = (d * (hS - ord(S[m - 1]) * h) + ord(S[m + N - 1])) % q
        if hS < 0:
            hS += q

        if hS == hW:
            coll += 1
            if S[m:m + N] == W:
                res.append(m)

    return len(res), num_comp, coll


def kmp_table(W, S):
    pos = 1
    cnd = 0
    T = [-1] * (len(W) + 1)
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


def kmp_search(W, S):
    T = kmp_table(W, S)
    N = len(W)
    M = len(S)
    num_comp = 0
    i = 0
    m = 0
    res = []

    while m < M:
        num_comp += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == N:
                res.append(m - i)
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return len(res), num_comp


with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()
W = "time."

# Metoda naiwna
t_start = time.perf_counter()
idx, comp = naive_search(W, S)
t_stop = time.perf_counter()
print("Czas obliczeń - m. naiwna:", "{:.7f}".format(t_stop - t_start))
print(f"{idx}; {comp}")

# Metoda Rabina-Karpa
t_start = time.perf_counter()
idx, comp = rabin_karp_search(W, S)
t_stop = time.perf_counter()
print("Czas obliczeń - m. Rabina-Karpa:", "{:.7f}".format(t_stop - t_start))
print(f"{idx}; {comp}")

# Metoda Rabina-Karpa 2
t_start = time.perf_counter()
idx, comp, coll = rabin_karp_search_2(W, S)
t_stop = time.perf_counter()
print("Czas obliczeń - m. Rabina-Karpa, rolling hash:", "{:.7f}".format(t_stop - t_start))
print(f"{idx}; {comp}; {coll}")

# Metoda Knutha-Morrisa-Pratta (KMP)
t_start = time.perf_counter()
idx, comp = kmp_search(W, S)
t_stop = time.perf_counter()
print("Czas obliczeń - m. Knutha-Morrisa-Pratta:", "{:.7f}".format(t_stop - t_start))
print(f"{idx}; {comp}")
