class Solution:
    def knightDialer(self, N: int) -> int:
        m = 10 ** 9 + 7
        direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        dp = [[1 for j in range(3)] for i in range(4)]
        dp[3][0] = 0
        dp[3][2] = 0
        for k in range(1, N):
            temp = [[0 for j in range(3)] for i in range(4)]
            for i in range(4):
                for j in range(3):
                    if i == 3 and j != 1:
                        continue
                    for d in direction:
                        tx = i + d[0]
                        ty = j + d[1]
                        if tx < 0 or ty < 0 or tx >= 4 or ty >= 3:
                            continue
                        temp[i][j] = (temp[i][j] + dp[tx][ty]) % m
            dp = temp
        ans = 0
        for i in range(4):
            for j in range(3):
                ans = (ans + dp[i][j]) % m
        return ans


class Solution:
    def knightDialer(self, N: int) -> int:
        m = 10 ** 9 + 7
        dp = [1 for i in range(10)]

        for k in range(1, N):
            temp = [0] * 10
            temp[0] = dp[4] + dp[6]
            temp[1] = dp[6] + dp[8]
            temp[2] = dp[7] + dp[9]
            temp[3] = dp[4] + dp[8]
            temp[4] = dp[3] + dp[9] + dp[0]
            temp[5] = 0
            temp[6] = dp[1] + dp[7] + dp[0]
            temp[7] = dp[2] + dp[6]
            temp[8] = dp[1] + dp[3]
            temp[9] = dp[4] + dp[2]
            dp = temp
        ans = 0
        for i in range(10):
            ans += dp[i]
            ans %= m
        return ans

s = Solution()
n = 2
print(s.knightDialer(n))
