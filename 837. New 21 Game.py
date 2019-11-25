

class Solution1:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (N + W + 1)
        for i in range(K, N + 1):
            dp[i] = 1.0
        S = min(N - K + 1, W)
        for i in range(K - 1, -1, -1):
            dp[i] = S / W
            S += dp[i] - dp[i + W]
        return dp[0]



# DFS 超时
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 表示，从 sum = 0 一直走到sum >= K，得到 sum <= N 的概率是多少
        return self.dfs(0, N, K ,W)

    def dfs(self, cur, N, K, W):
        if cur >= K:
            if cur <= N:
                return 1
            else:
                return 0
        sum = 0.0
        # 每次分w个岔
        for i in range(1, W + 1):
            sum += 1.0 / W * self.dfs(cur + i, N, K, W)
        return sum
# dp 超时，o（N*K）
class Solution2:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            for j in range(i - W, i):
                if j < 0:
                    continue
                if j >= K:
                    continue
                dp[i] += dp[j] * (1 / W)

        res = 0
        for i in range(K, N + 1):
            res += dp[i]
        return res

# dp + windows o(N)
class Solution3:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (N + 1)
        dp[0] = 1
        sum = 0
        for i in range(1, N + 1):
            if i - 1 < K:
                sum += dp[i - 1]
            if i - W - 1 >= 0:
                sum -= dp[i - W - 1]
            dp[i] = sum * (1 / W)
        res = 0
        for i in range(K, N + 1):
            res += dp[i]
        return res
