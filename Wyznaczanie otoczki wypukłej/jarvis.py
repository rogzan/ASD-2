#!/usr/bin/python
# -*- coding: utf-8 -*-


def left_idx(points):
    idx = 0
    for i in range(1, len(points)):
        if points[i][0] < points[idx][0]:
            idx = i
        elif points[i][0] == points[idx][0] and points[i][1] < points[idx][1]:
            idx = i
    return idx


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])

    if val > 0:
        return "p"  # prawoskretne
    elif val < 0:
        return "l"  # lewoskretne
    else:
        return "w"  # wspolliniowe


def jarvis_v1(points):
    n = len(points)
    res = []
    left = left_idx(points)

    p = left
    q = (p + 1) % n

    while True:
        res.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if orientation(points[p], points[r], points[q]) == "p":
                q = r
        p = q
        if p == left:
            break

    return res


def jarvis_v2(points):
    n = len(points)
    res = []
    left = left_idx(points)

    p = left
    q = (p + 1) % n

    while True:
        res.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if orientation(points[p], points[r], points[q]) == "p":
                q = r
        p = q
        if orientation(points[p], points[r], points[q]) == "w" and points[r][0] >= points[q][0] >= points[p][0]:
            q = r

        if p == left:
            break

    return res

# Pierwsza wersja
P1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
P2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
res1 = jarvis_v1(P1)
res2 = jarvis_v1(P2)

print(res1)
print(res2)

# Druga wersja
res1 = jarvis_v2(P1)
res2 = jarvis_v2(P2)

print(res1)
print(res2)

P3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
res3_1 = jarvis_v1(P3)
res3_2 = jarvis_v2(P3)
print(res3_1)
print(res3_2)
