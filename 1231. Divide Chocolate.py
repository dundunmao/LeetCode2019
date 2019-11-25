class Solution:
    def maximizeSweetness(self, sweetness, K: int) -> int:
        start = 0
        end = sum(sweetness)
        while start + 1 < end:
            mid = start + (end - start) // 2 # 保证每一piece都不低于mid
            cuts = self.cut(sweetness, mid)
            if cuts == K + 1:
                return mid
            elif cuts > K + 1:
                start = mid
            else:
                end = mid
        if start == K + 1:
            return start
        else:
            return end

    def cut(self, sweetness, sweet):
        total = 0
        cuts = 0
        for ele in sweetness:
            total += ele
            if total >= sweet:
                cuts += 1
                total = 0
        return cuts
s = Solution()
sweet = [1,2,3,4,5,6,7,8,9] # 6
K = 5
# print(s.cut(sweet, 1))
print(s.maximizeSweetness(sweet,K))

sweet = [5,6,7,8,9,1,2,3,4] # 1
# print(s.cut(sweet, 1))
K = 8
print(s.maximizeSweetness(sweet,K))
