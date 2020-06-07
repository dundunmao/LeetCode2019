import bisect
import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        graph = []
        temp_routes = [set() for i in range(n)]
        for i in range(n):
            for ele in routes[i]:
                temp_routes[i].add(ele)
            graph.append([])
        seen = set()
        targets = set()
        queue = collections.deque()
        for i in range(n):
            for j in range(i + 1, n):
                if self.intersect(routes[i], routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        for i in range(n):
            if S in temp_routes[i]:
                seen.add(i)
                queue.append(Node(i, 0))
            if T in temp_routes[i]:
                targets.add(i)
        while len(queue) > 0:
            cur = queue.popleft()
            if cur.node in targets:
                return cur.depth + 1
            for child in graph[cur.node]:
                if child not in seen:
                    seen.add(child)
                    queue.append(Node(child, cur.depth + 1))
        return -1

    def intersect(self, A, B):
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                return True
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
        return False
class Node:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


class Solution1:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        n = len(routes)
        # 如果已经到终点
        if S == T:
            return 0
        # 存 {stop:[bus]}
        stop_to_bus_hash = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stop_to_bus_hash:
                    stop_to_bus_hash[stop] = [bus]
                else:
                    stop_to_bus_hash[stop].append(bus)
        queue = collections.deque()
        queue.append(S)
        visited = set()
        res = 0
        while queue:
            res += 1
            size = len(queue)
            for i in range(size):
                curStop = queue.popleft()
                for bus in stop_to_bus_hash[curStop]:
                    if bus in visited:
                        continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T:
                            return res
                        queue.append(stop)
        return -1


s = Solution1()
routes = [[1, 2, 7],[1, 3, 7], [3, 6, 7]]
S = 1
T = 6
print(s.numBusesToDestination(routes, S, T))

routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
print(s.numBusesToDestination(routes, S, T))
