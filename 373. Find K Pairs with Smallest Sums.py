# import heapq
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         if len(nums1) == 0 or len(nums2) == 0:
#             return []
#         len_1 = len(nums1)
#         len_2 = len(nums2)
#         k = min(k, len_1*len_2)
#         res = []
#         visited = set()
#         pair_sum_min_heap = []
#         heapq.heappush(pair_sum_min_heap, [nums1[0] + nums2[0], (0, 0)])
#         while len(pair_sum_min_heap) > 0 and len(res) < k:
#             cur_sum, cur_pos = heapq.heappop(pair_sum_min_heap)
#             if cur_pos in visited:
#                 continue
#             visited.add(cur_pos)
#             res.append([nums1[cur_pos[0]], nums2[cur_pos[1]]])
#
#             if cur_pos[0] + 1 < len_1:
#                 heapq.heappush(pair_sum_min_heap, [nums1[cur_pos[0] + 1] + nums2[cur_pos[1]], (cur_pos[0] + 1, cur_pos[1])])
#
#             if cur_pos[1] + 1 < len_2:
#                 heapq.heappush(pair_sum_min_heap, [nums1[cur_pos[0]] + nums2[cur_pos[1] + 1], (cur_pos[0], cur_pos[1] + 1)])
#         return res

import heapq
class Pos:
    def __init__(self, first, second, sum):
        self.sum = sum
        self.first = first
        self.second = second
    def __lt__(a, b):
        return a.sum < b.sum
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        len_1 = len(nums1)
        len_2 = len(nums2)
        k = min(k, len_1*len_2)
        res = []
        visited = set()
        pair_sum_min_heap = []
        sum_first = nums1[0] + nums2[0]
        pos = Pos(0, 0, sum_first)
        heapq.heappush(pair_sum_min_heap, pos)
        while len(pair_sum_min_heap) > 0 and len(res) < k:
            cur_pos = heapq.heappop(pair_sum_min_heap)
            if (cur_pos.first, cur_pos.second) in visited:
                continue
            visited.add((cur_pos.first, cur_pos.second))
            res.append([nums1[cur_pos.first], nums2[cur_pos.second]])

            if cur_pos.first + 1 < len_1:
                pos = Pos(cur_pos.first + 1, cur_pos.second, nums1[cur_pos.first + 1] + nums2[cur_pos.second])
                heapq.heappush(pair_sum_min_heap, pos)

            if cur_pos.second + 1 < len_2:
                pos = Pos(cur_pos.first, cur_pos.second + 1, nums1[cur_pos.first] + nums2[cur_pos.second + 1])
                heapq.heappush(pair_sum_min_heap, pos)

        return res

x = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(x.kSmallestPairs(nums1, nums2, k))

