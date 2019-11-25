import heapq


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        heap_max = []
        heap_min = []
        for i in range(len(arrays)):
            heapq.heappush(heap_max, [-arrays[i][-1], i])
            heapq.heappush(heap_min, [arrays[i][0], i])

        first_mini, first_min_index = heapq.heappop(heap_min)
        first_maxi, first_max_index = heapq.heappop(heap_max)
        if first_min_index == first_max_index:
            second_mini, second_min_index = heapq.heappop(heap_min)
            second_maxi, second_max_index = heapq.heappop(heap_max)
            return max(abs(-first_maxi - second_mini), abs(-second_maxi - first_mini))
        else:
            return abs(-first_maxi - first_mini)



class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        overall_max = arrays[0][-1]
        overall_min = arrays[0][0]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, abs(overall_max - arrays[i][0]), abs(overall_min - arrays[i][-1]))
            overall_max = max(overall_max, arrays[i][-1])
            overall_min = min(overall_min, arrays[i][0])
        return res


