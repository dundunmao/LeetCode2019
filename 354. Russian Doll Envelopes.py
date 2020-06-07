from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0 for i in range(n)] # i这么多个信封时最大宽度是多少
        res = 0
        for envelope in envelopes:
            i = self.binary_search(dp, 0, res, envelope[1]) #在0到res这区间的信封里，在第几个信封那可以把当前宽度加上
            dp[i] = envelope[1]
            if i == res:
                res += 1
        return res

    def binary_search(self, dp, start, end, target):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if dp[mid] == target:
                return mid
            elif dp[mid] < target:
                start = mid
            else:
                end = mid
        if dp[start] >= target:
            return start
        return end
s = Solution()
a = [[5,4],[6,4],[6,7],[2,3]]
print(s.maxEnvelopes(a))
