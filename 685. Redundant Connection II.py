from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [0 for i in range(n + 1)]
        ans1 = []
        ans2 = []
        # 找一个node有两个parent的边
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if parents[v] > 0: # 说明v已经有parent了
                ans1 = [parents[v], v]
                ans2 = [edge[0], edge[1]]
                # 删后来的边
                edge[0], edge[1] = -1, -1
            parents[v] = u
        # 找成环的最后一个边
        union_find = UnionFind(n)
        for edge in edges:
            if edge == [-1, -1]:
                continue
            u = edge[0]
            v = edge[1]
            if not union_find.union(u, v):
                return ans1 if ans1 else edge
        return [] if not ans2 else ans2

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
            return self.root[u]
        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        self.root[root_v] = root_u
        return True



class Solution1:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {}
        parents = [0 for i in range(n + 1)]
        ans1 = []
        ans2 = []
        # 找一个node有两个parent的边
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if parents[v] > 0:  # 说明v已经有parent了
                ans1 = [parents[v], v]
                ans2 = [edge[0], edge[1]]
                # 删后来的边
                # edge[0], edge[1] = -1, -1
            else:
                if u in graph:
                    graph[u].append(v)
                else:
                    graph[u] = [v]
            parents[v] = u
        visited = set()
        path = []
        for node in graph.keys():
            if node not in visited:
                if not self.dfs(node, graph, parents, visited, path):
                    return ans1 if ans1 else [parents[node], node]

        return [] if not ans2 else ans2

    def dfs(self, node, graph, parents, visited, path):
        if node in path:
            return False
        if node not in graph:
            return True
        else:
            visited.add(node)
            path.append(node)
            for child in graph[node]:
                if not self.dfs(child, graph, parents, visited, path):
                    return False
            path.pop()
        return True


s = Solution1()
a = [[1,2],[1,3],[2,3]]
print(s.findRedundantDirectedConnection(a)) #[2,3]
a = [[1,2], [2,3], [3,4], [4,1], [1,5]]
print(s.findRedundantDirectedConnection(a)) #[4,1]
a = [[2,1],[3,1],[4,2],[1,4]]
print(s.findRedundantDirectedConnection(a)) #[2,1]
