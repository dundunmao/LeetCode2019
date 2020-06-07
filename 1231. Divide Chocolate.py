from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        start = 0
        end = sum(sweetness)
        while start + 1 < end:
            mid = start + (end - start) // 2 # 保证每一piece都不低于mid
            cuts = self.cut(sweetness, mid)
            if cuts >= K:
                start = mid
            else:
                end = mid
        if self.cut(sweetness, end) == K:
            return end
        else:
            return start

    def cut(self, sweetness, sweet):
        total = 0
        cuts = 0
        for ele in sweetness:
            total += ele
            if total >= sweet:
                cuts += 1
                total = 0
        return cuts - 1


class Solution1:
    def __init__(self):
        self.res = 0

    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if K == 0:
            return min(sweetness)
        self.dfs(sweetness, 0, 0, K + 1, float('inf'))
        return self.res

    def dfs(self, sweetness, pos, sum_up, k, branch_mini):
        if pos == len(sweetness):
            if k == 0:
                self.res = max(self.res, branch_mini)
        elif k == 0:
            return
        else:
            self.dfs(sweetness, pos + 1, sum_up + sweetness[pos], k, branch_mini)
            self.dfs(sweetness, pos + 1, 0, k - 1, min(branch_mini, sum_up + sweetness[pos]))


s = Solution1()
sweet = [1,2,3,4,5,6,7,8,9]# 6
K = 5
print(s.maximizeSweetness(sweet,K))
s = Solution1()
sweet = [5,6,7,8,9,1,2,3,4] # 1
K = 8
print(s.maximizeSweetness(sweet,K))
s = Solution1()
sweet = [1,2,2,1,2,2,1,2,2] # 5
K = 2
print(s.maximizeSweetness(sweet,K))
s = Solution1()
sweet = [19679,20653,68010,3714,54485,548,41366,11201,47138,70768,1050,87246,17114,56157,13235,65363,30444,56929,21969,22308]
K = 0
print(s.maximizeSweetness(sweet,K)) # 548
