import heapq
class Solution:
    def kClosest(self, points, K):
        distance_heap = []
        heapq.heapify(distance_heap)
        for ele in points:
            heapq.heappush(distance_heap, [abs(ele[0]) + abs(ele[1]), ele])
        res = []
        while K > 0:
            res.append(heapq.heappop(distance_heap)[1])
            K -= 1
        return res


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_heap = []

        for ele in points:
            if len(distance_heap) == K:
                heapq.heappush(distance_heap, [-ele[0] ** 2 - ele[1] ** 2, ele])
                heapq.heappop(distance_heap)
            else:
                heapq.heappush(distance_heap, [-ele[0] ** 2 - ele[1] ** 2, ele])
        return [ele[1] for ele in distance_heap]

import random
class Solution(object):
    def kClosest(self, points, K):

        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)


points = [[1,3],[-2,2]]
K = 1
x = Solution()
print(x.kClosest(points, K))
