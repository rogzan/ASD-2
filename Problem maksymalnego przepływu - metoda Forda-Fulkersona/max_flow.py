#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.color = None

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, v1, v2, capacity=0):
        self.v1 = v1
        self.v2 = v2
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity
        self.isResidual = False

    def __repr__(self):
        return f'({self.capacity} {self.flow} {self.residual} {self.isResidual})'


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

    def search_key(self, key):
        for v, idx in self.d.items():
            if v.key == key:
                return idx

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
            for v2, edge in self.g[i]:
                edges.append(edge)
        return edges

    def bfs(self, s, t):
        n = self.order()
        parent = [None] * n
        visited = [False] * n
        queue = [s]  # dodanie wierzcholka poczatkowego
        visited[s] = True

        while queue:
            v = queue.pop(0)
            nbrs = self.neighbours(v)
            for i in range(len(nbrs)):
                idx = self.g[v][i][0]
                if not visited[idx] and self.g[v][i][1].residual > 0:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = v
        return parent

    def path_analysis(self, s, t, parent):
        curr = t
        min_cap = sys.maxsize

        if parent[t] is None:
            return 0
        while curr != s:
            p = parent[curr]
            nbrs = self.neighbours(p)
            for idx, e in nbrs:
                if idx == curr and not e.isResidual and e.residual < min_cap:
                    edge = e
                    min_cap = edge.residual
                    break
            curr = p
        return min_cap

    def path_aug(self, s, t, parent, min_cap):
        curr = t

        while curr != s:
            p = parent[curr]
            nbrs_p = self.neighbours(p)
            nbrs_curr = self.neighbours(curr)
            edge_res = None
            edge = None
            for idx, e in nbrs_p:
                if idx == curr and not e.isResidual:
                    edge = e
                    break
            for idx, e in nbrs_curr:
                if idx == p and e.isResidual:
                    edge_res = e
                    break
            curr = p
            edge.flow += min_cap
            edge.residual -= min_cap
            edge_res.residual += min_cap

    def max_flow(self, s, t):
        parent = self.bfs(s, t)
        min_flow = self.path_analysis(s, t, parent)

        while min_flow > 0:
            self.path_aug(s, t, parent, min_flow)
            parent = self.bfs(s, t)
            min_flow = self.path_analysis(s, t, parent)

        max_flow = 0
        edges = self.edges()
        for edge in edges:
            if edge.v2 == self.getVertex(t) and not edge.isResidual:
                max_flow += edge.flow
        return max_flow


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i).key
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w, end=";")
        print()
    print("-------------------")


def test(graf):
    G = AdjList()
    for el in graf:
        v1 = Vertex(el[0])
        v2 = Vertex(el[1])
        edge1 = Edge(v1, v2, el[2])
        edge2 = Edge(v2, v1, el[2])
        edge2.residual = 0
        edge2.isResidual = True
        G.insertVertex(v1)
        G.insertVertex(v2)
        G.insertEdge(v1, v2, edge1)
        G.insertEdge(v2, v1, edge2)

    s = G.search_key("s")
    t = G.search_key("t")
    print(G.max_flow(s, t))
    printGraph(G)


graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20),
          ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
          ('d', 'c', 4)]

test(graf_0)
test(graf_1)
test(graf_2)
test(graf_3)
