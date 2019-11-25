import heapq
class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n
        # 因为存的是index，最后的index对应的值一定是最小的，用这个最小值跟当前i的值比
        unresolved_index_maxheap = []
        for i in range(n):
            while len(unresolved_index_maxheap) != 0 and T[-unresolved_index_maxheap[0]] < T[i]:
                unresolved_index = - heapq.heappop(unresolved_index_maxheap)
                res[unresolved_index] = i - unresolved_index
            heapq.heappush(unresolved_index_maxheap, -i)
        return res
x = Solution()
nums1 = [73,74,75,71,69,72,76,73]

print(x.dailyTemperatures(nums1))
