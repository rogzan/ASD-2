#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import graf_mst

class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.color = None

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, v1, v2, weight = 0):
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
        self.g[idx1].append((idx2, edge))

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        self.m.remove(vertex)
        self.d.pop(vertex)
        for index, k in enumerate(self.d):
            if index >= idx:
                self.d[k] -= 1

        self.g.pop(idx)
        for i in range(len(self.g)):
            for el in self.g[i]:
                if el[0] == idx:
                    self.g[i].remove(el)

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        for el in self.g[idx1]:
            if el[0] == idx2:
                self.g[idx1].remove(el)
        for el in self.g[idx2]:
            if el[0] == idx1:
                self.g[idx2].remove(el)

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
            for v2 in self.g[i]:
                edges.append((v1, v2))
        return edges

    def prim(self):
        n = len(self.g)
        intree = [0] * n  # lista informujaca czy dany wierzcholek jest w drzewie
        parent = [None] * n  # lista przyporzadkowujaca kazdemu wierzcholkowi poprzednika w MST
        distance = [sys.maxsize] * n  # lista odleglosci od wierzcholka startowego
        distance[0] = 0
        v = 0
        min_idx = None
        while intree[v] == 0:
            intree[v] = 1
            for i in range(len(self.g[v])):
                idx = self.g[v][i][0]
                if distance[idx] > self.g[v][i][1].weight and intree[idx] == 0:
                    distance[idx] = self.g[v][i][1].weight
                    parent[idx] = v

            min_dist = sys.maxsize
            for ver in range(len(self.g)):
                idx = ver
                if intree[idx] == 0 and min_dist > distance[idx]:
                    min_dist = distance[idx]
                    min_idx = idx
            v = min_idx

        mst = AdjList()
        parent = parent[1::]
        distance = distance[1::]
        cost = 0

        for i in range(len(self.g)):
            v = self.getVertex(i)
            mst.insertVertex(v)

        for i in range(len(parent)):
            v2 = self.getVertex(i + 1)
            v1 = self.getVertex(parent[i])
            edge1 = Edge(v1, v2, distance[i])
            edge2 = Edge(v2, v1, distance[i])
            mst.insertEdge(v1, v2, edge1)
            mst.insertEdge(v2, v1, edge2)
            cost += distance[i]

        return mst

def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i).key
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w.weight, end=";")
        print()
    print("-------------------")


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

mst = G.prim()
printGraph(mst)
