#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import copy


class Vertex:
    def __init__(self, key=None):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, v1=0, v2=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = 0


class AdjMatrix:
    def __init__(self):
        self.m = []
        self.d = {}
        self.g = []

    def insertVertex(self, vertex):
        idx = self.order()
        if vertex not in self.d.keys():
            self.d[vertex] = idx
            self.m.append(vertex)
            self.g.append([0])
            for i in range(len(self.g)):
                l = len(self.g[i])
                while l < len(self.g):
                    self.g[i].append(0)
                    l += 1

    def insertEdge(self, vertex1, vertex2, edge):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if self.g[idx1][idx2] == 0:
            self.g[idx1][idx2] = edge

    def getVertexIdx(self, vertex):
        return self.d[vertex]

    def getVertex(self, vertex_idx):
        return self.m[vertex_idx]

    def neighbours(self, vertex_idx):
        n_list = []
        for i in range(len(self.g)):
            if self.g[vertex_idx][i] != 0:
                n_list.append(i)
        return n_list

    def order(self):
        return len(self.m)

    def size(self):
        return len(self.edges())

    def edges(self):
        edges = []
        for i in range(len(self.g)):
            for j in range(len(self.g)):
                if self.g[i][j] != 0:
                    v1 = self.getVertex(i)
                    v2 = self.getVertex(j)
                    edges.append((v1, v2))
        return edges


def nbrs(v, G):
    n_list = []
    for i in range(len(G[v])):
        if G[v][i] != 0:
            n_list.append(i)
    return n_list


def is_isomorphism(P, G, M):
    return (P == (np.matmul(M, (np.transpose(np.matmul(M, G)))))).all()


def ullman(used_columns, current_row, G, P, M, no_recursion, no_iso):
    no_recursion = no_recursion + 1
    if current_row == len(M):
        if is_isomorphism(P, G, M):
            no_iso += 1
            return no_recursion, no_iso
    M_copy = copy.copy(M)
    for c in range(len(M[0])):
        if used_columns[c] == 0:
            if current_row < len(M):
                M_copy[current_row][c] = 1
                for i in range(len(M[0])):
                    if i != c:
                        if M_copy[current_row][i] == 1 and used_columns[i] == 1 and i > c:
                            used_columns[i] = 0
                        M_copy[current_row][i] = 0
                used_columns[c] = 1
                no_recursion, no_iso = ullman(used_columns, current_row + 1, G, P, M_copy, no_recursion, no_iso)
                used_columns[c] = 0

    return no_recursion, no_iso


def M0(M, G, P):
    M_copy = copy.copy(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if len(nbrs(j, G)) < len(nbrs(i, P)):
                M_copy[i][j] = 0
            else:
                M_copy[i][j] = 1
    return M_copy


def ullman_2(used_columns, current_row, G, P, M, no_recursion, no_iso):
    no_recursion = no_recursion + 1
    if current_row == len(M):
        if is_isomorphism(P, G, M):
            no_iso += 1
            return no_recursion, no_iso
    M_copy = copy.copy(M)
    m0 = M0(M, G, P)

    for c in range(len(M[0])):
        if used_columns[c] == 0:
            if current_row < len(M) and m0[current_row][c] == 1:
                M_copy[current_row][c] = 1
                for i in range(len(M[0])):
                    if i != c:
                        if M_copy[current_row][i] == 1 and used_columns[i] == 1 and i > c:
                            used_columns[i] = 0
                        M_copy[current_row][i] = 0
                used_columns[c] = 1
                no_recursion, no_iso = ullman_2(used_columns, current_row + 1, G, P, M_copy, no_recursion, no_iso)
                used_columns[c] = 0
    return no_recursion, no_iso


def prune(M, G, P):
    util = True
    while util:
        util = False
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    for x in nbrs(i, P):
                        num = 0
                        for y in nbrs(j, G):
                            if M[x][y] == 1:
                                num += 1
                        if num == 0:
                            M[i][j] = 0
                            util = True


def ullman_3(used_columns, current_row, G, P, M, no_recursion, no_iso):
    no_recursion = no_recursion + 1
    if 1 not in M:
        M = np.ones((len(M), len(M[0])))

    if current_row == len(M):
        if is_isomorphism(P, G, M):
            no_iso += 1
            return no_recursion, no_iso
    M_copy = copy.copy(M)
    m0 = M0(M, G, P)
    prune(M_copy, G, P)
    if 1 not in M_copy:
        return no_recursion, no_iso

    for c in range(len(M[0])):
        if used_columns[c] == 0:
            if current_row < len(M) and m0[current_row][c] == 1:
                M_copy[current_row][c] = 1
                for i in range(len(M[0])):
                    if i != c:
                        if M_copy[current_row][i] == 1 and used_columns[i] == 1 and i > c:
                            used_columns[i] = 0
                        M_copy[current_row][i] = 0
                used_columns[c] = 1
                no_recursion, no_iso = ullman_3(used_columns, current_row + 1, G, P, M_copy, no_recursion, no_iso)
                used_columns[c] = 0
    return no_recursion, no_iso


graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

G = AdjMatrix()
for el in graph_G:
    v1 = Vertex(el[0])
    v2 = Vertex(el[1])
    G.insertVertex(v1)
    G.insertVertex(v2)
    G.insertEdge(v1, v2, el[2])
    G.insertEdge(v2, v1, el[2])

P = AdjMatrix()
for el in graph_P:
    v1 = Vertex(el[0])
    v2 = Vertex(el[1])
    P.insertVertex(v1)
    P.insertVertex(v2)
    P.insertEdge(v1, v2, el[2])
    P.insertEdge(v2, v1, el[2])

m_g = np.array(G.g)
m_p = np.array(P.g)

M = np.array([[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]])


used_col = [0] * len(M[0])
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == 1:
            used_col[j] = 1

no_rec1, no_iso1 = ullman(used_col, 0, m_g, m_p, M, 0, 0)
no_rec2, no_iso2 = ullman_2(used_col, 0, m_g, m_p, M, 0, 0)
no_rec3, no_iso3 = ullman_3(used_col, 0, m_g, m_p, M, 0, 0)

print(no_iso1, no_rec1)
print(no_iso2, no_rec2)
print(no_iso3, no_rec3)
