# dp o(n^2)
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x:x[0])
        # dp[i]代表: 算上intrvals[i]，最多能有多少non-overlap
        dp = [1] * len(intervals)
        for i in range(1, len(intervals)):
            maxi = 1
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    maxi = max(maxi, dp[j] + 1)
            dp[i] = maxi
        return len(intervals) - max(dp)
#     greedy o(nlgn)
class Solution1:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])
        # dp[i]代表: 算上intrvals[i]，最多能有多少non-overlap
        res = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                res += 1
                end = intervals[i][1]

        return len(intervals) - res
s = Solution1()
a = [[1,2]] #0
print(s.eraseOverlapIntervals(a))
a = [ [1,2], [2,3], [3,4], [1,3] ] # 1
print(s.eraseOverlapIntervals(a))
a = [ [1,2], [1,2], [1,2] ] #2
print(s.eraseOverlapIntervals(a))
a = [ [1,2], [2,3] ] #0
print(s.eraseOverlapIntervals(a))
