class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_space = 0
        n = len(seats)
        ans = 0
        for i in range(n):
            if seats[i] == 1:
                max_space = 0
            else:
                max_space += 1
                ans = max(ans, (max_space + 1) // 2)
        for i in range(n):
            if seats[i] == 1:
                ans = max(ans, i)
                break
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                ans = max(ans, n - 1 - i)
                break
        return ans


s = Solution()
# a = [1,0,0,0,1,0,1] #2
# print((s.maxDistToClosest(a)))
a = [1,0,0,0] #3
print((s.maxDistToClosest(a)))

a = [0,1] #1
print((s.maxDistToClosest(a)))
