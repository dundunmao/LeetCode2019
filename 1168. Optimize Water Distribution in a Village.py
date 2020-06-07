import heapq
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        dus = DSU(n)
        heap = []
        for i in range(len(wells)): #把井到房子的通路加入heap
            heapq.heappush(heap, Node(0, i + 1, wells[i]))
        for p in pipes: #把房子间的通路加入heap
            heapq.heappush(heap, Node(p[0], p[1], p[2]))
        res = 0
        while len(heap) > 0: #根据Kruskal算法每次去最小路径，进行连通，直到都连上
            cur = heapq.heappop(heap)
            if dus.union(cur.start, cur.end): # 如果两个人没连通
                res += cur.val
        return res

class Node:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
    def __lt__(a, b):
        return a.val < b.val
class DSU:
    def __init__(self, n):
        self.size = [1 for i in range(n + 1)]
        self.root = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            self.root[i] = i

    def find(self, x):
        if self.root[x] != x: #如果自己不是自己的根
            self.root[x] = self.find(self.root[x]) #就去找根
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: #如果已经连通就returnFalse
            return False
        if self.size[root_x] < self.size[root_y]: # 如果x树比y树小，x归入y
            self.root[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.root[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

s = Solution()
# a = [[1,3],[3,4],[2,3], [2,5],[3,6],[4,6],[4,7],[5,6],[6,7]]
# d = DSU(7)
# d.union(1,7)
n = 3
wells = [1,2,2]
pipes = [[1,2,1],[2,3,1]]
print(s.minCostToSupplyWater(n,wells,pipes))
