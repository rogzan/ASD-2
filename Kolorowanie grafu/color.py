# !/usr/bin/python
# -*- coding: utf-8 -*-

import polska


class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.color = None

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
                    v1 = self.getVertex(i).key
                    v2 = self.getVertex(j).key
                    edges.append((v1, v2))
        return edges

    def first_available(self, color_list):
        color_set = set(color_list)
        count = 0
        while True:
            if count not in color_set:
                color_list.append(count)
                return count
            count += 1

    def bfs(self):
        s = 0
        n = self.order()
        visited = [False] * n
        colors_used = []
        c = self.first_available(colors_used)
        self.getVertex(s).color = c
        queue = [s]  # dodanie wierzcholka poczatkowego
        visited[s] = True

        while queue:
            v = queue.pop(0)
            nbrs = self.neighbours(v)
            for idx in nbrs:
                if not visited[idx]:
                    nbrs_idx = self.neighbours(idx)
                    nbrs_colors = [self.getVertex(nbr).color for nbr in nbrs_idx if
                                   self.getVertex(nbr).color is not None]
                    self.getVertex(idx).color = self.first_available(nbrs_colors)
                    queue.append(idx)
                    visited[idx] = True

    def dfs(self):
        s = 0
        n = self.order()
        visited = [False] * n
        colors_used = []
        c = self.first_available(colors_used)
        self.getVertex(s).color = c
        stack = [s]

        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
            nbrs = self.neighbours(v)
            for idx in nbrs:
                if not visited[idx]:
                    nbrs_idx = self.neighbours(idx)
                    nbrs_colors = [self.getVertex(nbr).color for nbr in nbrs_idx if
                                   self.getVertex(nbr).color is not None]
                    self.getVertex(idx).color = self.first_available(nbrs_colors)
                    stack.append(idx)

    def coloring(self, type=True):
        res = []
        if type:
            self.bfs()
        else:
            self.dfs()
        res = []
        for v in self.m:
            res.append((v.key, v.color))
        return res


edg = polska.graf

Graph1 = AdjMatrix()
for i in edg:
    v1 = Vertex(i[0])
    v2 = Vertex(i[1])
    Graph1.insertVertex(v1)
    Graph1.insertVertex(v2)
    Graph1.insertEdge(v1, v2, i)
    Graph1.insertEdge(v2, v1, i)

colors1 = Graph1.coloring(True)  # True - bfs, False - dfs
edges1 = Graph1.edges()

polska.draw_map(edges1, colors1)
