#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import graf_mst


class Vertex:
    def __init__(self, key=None):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class AdjList:
    def __init__(self):
        self.m = []
        self.d = {}
        self.g = []

    def insertVertex(self, vertex):
        idx = self.order()
        if vertex not in self.d.keys():
            self.d[vertex] = idx
            self.m.append(vertex)
            self.g.append([])

    def insertEdge(self, vertex1, vertex2, edge):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.g[idx1].append((vertex2, edge))

    def getVertexIdx(self, vertex):
        return self.d[vertex]

    def getVertex(self, vertex_idx):
        return self.m[vertex_idx]

    def neighbours(self, vertex_idx):
        return self.g[vertex_idx]

    def order(self):
        return len(self.m)

    def size(self):
        return len(self.edges())

    def edges(self):
        edges = []
        for i in range(len(self.g)):
            v1 = self.getVertex(i)
            for v2, edge in self.g[i]:
                edges.append((v1, v2, edge.weight))
        return edges


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.size = 0


def find(v):
    if v != v.parent:
        v.parent = find(v.parent)
    return v.parent


def union_sets(s1, s2):
    x = find(s1)
    y = find(s2)
    if x.size > y.size:  # mniejsze drzewo podpinam pod większe
        y.parent = x
    else:
        x.parent = y
        if x.size == y.size:
            y.size += 1


def same_components(s1, s2):
    return find(s1) == find(s2)


def make_set(v):
    return Node(v)



def Kruskal(g):
    m = g.order()  # v to liczba wierzchołków
    n = g.size()  # n to liczba krawędzi
    edges = g.edges()  # lista krawędzi postaci listy tupli (v1, v2, waga)
    edges.sort(key=lambda y: y[2])  # sortowanie w porządku malejącym po wagach
    A = []  # rezultat  - poszukwiana lista krawędzi
    V = []  # zamiast struktury union tworzę listę elementy z  etykietami id

    for i in range(m):
        V.append(make_set(i))

    for i in range(n):
        u = g.getVertexIdx(edges[i][0])  # przekodowanie - zamiast kodu ASCII (ord())
        v = g.getVertexIdx(edges[i][1])  # używam numeru indeksu w liście struktury grafu

        if find(V[u]) != find(V[v]):
            A.append((edges[i][0].key, edges[i][1].key))
            union_sets(V[u], V[v])

    return A


graf = graf_mst.graf
G = AdjList()
for el in graf:
    v1 = Vertex(el[0])
    v2 = Vertex(el[1])
    edge1 = Edge(v1, v2, el[2])
    edge2 = Edge(v2, v1, el[2])
    G.insertVertex(v1)
    G.insertVertex(v2)
    G.insertEdge(v1, v2, edge1)
    G.insertEdge(v2, v1, edge2)

res = Kruskal(G)
print(res)
