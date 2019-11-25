import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        n = len(quality)
        quality_wage_ratio = []
        for i in range(n):
            ratio = wage[i] / quality[i]
            quality_wage_ratio.append((ratio, quality[i]))
        quality_wage_ratio.sort()
        print(quality_wage_ratio)
        pq = []
        total_quality = 0
        min_wage = float('inf')
        for i in range(n):
            total_quality += quality_wage_ratio[i][1]
            heapq.heappush(pq, -quality_wage_ratio[i][1])
            if len(pq) > K:
                total_quality += heapq.heappop(pq)
            if len(pq) == K:
                min_wage = min(min_wage, quality_wage_ratio[i][0] * total_quality)

        return min_wage
s = Solution()
# a = [3,1,10,10,1]
# b = [4,8,2,2,7]
# c = 3
# print(s.mincostToHireWorkers(a, b, c))

# a = [10,20,5]
# b = [70,50,30]
# c = 2
# print(s.mincostToHireWorkers(a, b, c))


a = [1,1,1,5]
b = [1,1,1,10]
c = 3
print(s.mincostToHireWorkers(a, b, c))
