# Dij
import heapq
class Solution:
    def networkDelayTime(self, times, N, K) -> int:
        graph = {}
        for edge in times:
            if not edge[0] in graph:
                graph[edge[0]] = []
            graph[edge[0]].append((edge[1], edge[2]))

        heap = [] # 存(node, distanc),按distance排序，min heap
        heapq.heappush(heap, DistHeap(K, 0))
        dist_to_k_hash = {} # distance from every node to k
        while heap:
            info = heapq.heappop(heap)
            dist = info.dist
            node = info.node
            if node in dist_to_k_hash:
                continue
            dist_to_k_hash[node] = dist
            if node in graph:
                for edge in graph[node]:
                    end = edge[0]
                    dist_to_start = edge[1]
                    if end not in dist_to_k_hash:
                        heapq.heappush(heap, DistHeap(end, dist + dist_to_start))

        if len(dist_to_k_hash) != N:
            return -1
        ans = 1
        for candidate in dist_to_k_hash.values():
            ans = max(ans, candidate)
        return ans


class DistHeap:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist

    def __lt__(a, b):
        return a.dist < b.dist

# Bellman
import heapq
class Solution3:
    def networkDelayTime(self, times, N, K):
        dist = [float('inf')] * (N + 1)
        dist[K] = 0
        for i in range(1, N):
            for edge in times:
                start = edge[0]
                end = edge[1]
                distance = edge[2]
                dist[end] = min(dist[end], dist[start] + distance)
        max_dist = 0
        for val in dist[1:]:
            if val == float('inf'):
                return -1
            max_dist = max(max_dist, val)
        return max_dist


# 弗洛伊德Floyd
class Solution2:
    def networkDelayTime(self, times, N, K):
        f = [[-1 for j in range(N)] for i in range(N)]
        for time in times:
            f[time[0] - 1][time[1] - 1] = time[2]
        for i in range(N):
            f[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if f[i][k] >= 0 and f[k][j] >= 0:
                        if f[i][j] < 0 or f[i][j] > f[i][k] + f[k][j]:
                            f[i][j] = f[i][k] + f[k][j]
        ans = float('-inf')
        for i in range(N):
            if f[K - 1][i] < 0:
                return -1
            ans = max(ans, f[K - 1][i])
        return ans







# dfs,超时
class Solution:
    def networkDelayTime(self, times, N, K) -> int:
        graph = {}
        for time in times:
            if time[0] in graph:
                graph[time[0]][time[1]] = time[2]
            else:
                graph[time[0]] = {}
                graph[time[0]][time[1]] = time[2]
        result = Result()
        visited = set()
        count = {}
        visited.add(K)
        self.dfs(K, visited, result, graph, count)
        if len(count) < N:
            return -1
        return max(count.values())

    def dfs(self, start, visited, result, graph, count):
        if start in count:
            if count[start] > result.cur:
                count[start] = result.cur
        else:
            count[start] = result.cur
        if start in graph:
            for child, val in graph[start].items():
                if child not in visited:
                    visited.add(child)
                    result.cur += val
                    self.dfs(child, visited, result, graph, count)
                    result.cur -= val
                    visited.remove(child)


class Result:
    def __init__(self):
        self.cur = 0

s = Solution2()
t = [[2,1,1],[2,3,1],[3,4,1]]
K = 2
N = 4

print(s.networkDelayTime(t, N, K))
t = [[1,2,1]]
K = 2
N = 2

print(s.networkDelayTime(t, N, K))
