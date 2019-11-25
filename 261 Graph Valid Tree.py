#BFS
import collections
from collections import deque
class Solution(object):
    #要证明这个无向图：1无环，2connect。这样才是树
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # 检查是不是有环
        if len(edges) != n - 1:
            return False
        #  减了hash,key是node,value是neighbor
        neighbors = collections.defaultdict(list)
        for u, v in edges: #因为是无向的，所有互为neighbor，所以加起点终点都加
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {} #检查visited
        queue = deque()
        # 先把0这个node放进去
        queue.append(0)
        visited[0] = True
        while len(queue) != 0:
            cur = queue.popleft()
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
        # 如果没遍历往所有node，说明有环，或不connect
        return len(visited) == n


class Solution1:
    def validTree(self, n: int, edges) -> bool:
        # 检查是不是有环
        if len(edges) != n - 1:
            return False
        #  减了hash,key是node,value是neighbor
        neighbors = collections.defaultdict(list)
        for u, v in edges: #因为是无向的，所有互为neighbor，所以加起点终点都加
            neighbors[u].append(v)
            neighbors[v].append(u)
        visited = set()
        path = set()
        if self.dfs(0, neighbors, visited, path) and len(visited) == n:
            return True
        return False
    def dfs(self, cur, neighbors, visited, path):
        path.add(cur)
        if cur in visited:
            return False
        visited.add(cur)
        for child in neighbors[cur]:
            if child not in path:
                if not self.dfs(child, neighbors, visited, path):
                    return False
        path.remove(cur)
        return True



#     lint

class union_find:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.root[root_a] = root_b

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if n - 1 != len(edges):
            return False
        uf = union_find(n)
        for i in range(len(edges)):
            root1 = uf.find(edges[i][0])
            root2 = uf.find(edges[i][1])
            if root1 == root2:
                return False
            else:
                uf.connect(edges[i][0],edges[i][1])
        return True
s = Solution1()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(s.validTree(n, edges))

edges = [[0, 1], [0, 2], [0, 3], [1, 4],[3,4]]
n = 5
print(s.validTree(n, edges))
