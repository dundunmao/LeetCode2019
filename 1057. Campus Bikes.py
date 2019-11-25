import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        heap = []
        res = [-1] * n
        bike_set = set()
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                node = Node(i, j, dist)
                heapq.heappush(heap, node)
        while heap:
            node = heapq.heappop(heap)
            worker = node.worker
            bike = node.bike
            if res[worker] == -1 and bike not in bike_set:
                res[worker] = node.bike
                bike_set.add(bike)
        return res

class Node:
    def __init__(self, worker, bike, dist):
        self.worker = worker
        self.bike = bike
        self.dist = dist
    def __lt__(a, b):
        if a.dist == b.dist and a.worker == b.worker:
            return a.bike < b.bike
        if a.dist == b.dist:
            return a.worker < b.worker
        return a.dist < b.dist


# 用Node超时和heap，直接用tuple + array.sort
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        worker_array = []
        res = [-1] * n
        bike_set = set()
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                worker_array.append((dist, i, j))
        worker_array.sort()
        for node in worker_array:
            worker = node[1]
            bike = node[2]
            if res[worker] == -1 and bike not in bike_set:
                res[worker] = bike
                bike_set.add(bike)
        return res
s = Solution()

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
print(s.assignBikes(workers, bikes))
