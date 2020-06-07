from typing import List

from collections import defaultdict

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            visited = set()
            if self.dfs(u, v, graph, visited):
                return edge
            graph[u].append(v)
            graph[v].append(u)
        return []

    def dfs(self, curr, goal, graph, visited):
        if curr == goal:
            return True
        visited.add(curr)
        if curr not in graph or goal not in graph:
            return False
        for child in graph[curr]:
            if child in visited:
                continue
            if self.dfs(child, goal, graph, visited):
                return True
        return False


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_find = UnionFind(n)
        for edge in edges:
            if not union_find.union(edge[0], edge[1]):
                return edge
        return []

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.size[root_u] < self.size[root_v]:
            self.root[root_u] = root_v
            self.size[root_u] += self.size[root_v]
        else:
            self.root[root_v] = root_u
            self.size[v] += self.size[u]
        return True

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
            return self.root[u]
        return u
