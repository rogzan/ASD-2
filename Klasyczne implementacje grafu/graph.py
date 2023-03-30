#!/usr/bin/python
# -*- coding: utf-8 -*-

import polska


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

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        self.m.remove(vertex)
        self.d.pop(vertex)
        for index, k in enumerate(self.d):
            if index >= idx:
                self.d[k] -= 1

        new_g = [[0 for i in range(self.order())] for j in range(self.order())]
        new_i = 0
        new_j = 0
        for i in range(len(self.g)):
            if i == idx:
                continue
            for j in range(len(self.g)):
                if j == idx:
                    continue
                new_g[new_i][new_j] = self.g[i][j]
                new_j += 1
            new_i += 1
            new_j = 0
        self.g = new_g

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if self.g[idx1][idx2] != 0:
            self.g[idx1][idx2] = 0
            self.g[idx2][idx1] = 0

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
        self.g[idx1].append(vertex2)

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        self.m.remove(vertex)
        self.d.pop(vertex)
        for index, k in enumerate(self.d):
            if index >= idx:
                self.d[k] -= 1

        self.g.pop(idx)
        for i in range(len(self.g)):
            if vertex in self.g[i]:
                self.g[i].remove(vertex)

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if vertex2 in self.g[idx1]:
            self.g[idx1].remove(vertex2)
        if vertex1 in self.g[idx2]:
            self.g[idx2].remove(vertex1)

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


edg = polska.graf

Graph1 = AdjMatrix()
for i in edg:
    Graph1.insertVertex(i[0])
    Graph1.insertVertex(i[1])
    Graph1.insertEdge(i[0], i[1], i)

Graph1.deleteVertex('K')
Graph1.deleteEdge('W', 'E')
edges1 = Graph1.edges()
polska.draw_map(edges1)

Graph2 = AdjList()
for i in edg:
    Graph2.insertVertex(i[0])
    Graph2.insertVertex(i[1])
    Graph2.insertEdge(i[0], i[1], i)

Graph2.deleteVertex('K')
Graph2.deleteEdge('W', 'E')
edges2 = Graph2.edges()
print(Graph2.d.keys())
polska.draw_map(edges2)
