class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        total = d * f + 1
        if target > d * f:
            return 0
        all_result = [[-1 for j in range(total)] for i in range(d + 1)]  # [level, sum]
        return self.dfs(d, target, all_result, f, target)

    def dfs(self, level, sum_up, all_result, f, target):
        if all_result[level][sum_up] != -1:
            return all_result[level][sum_up]
        if sum_up > target:
            return 0
        if level == 0:
            if sum_up == 0:
                return 1
            else:
                return 0

        res = 0
        for i in range(1, f + 1):
            res += self.dfs(level - 1, sum_up - i, all_result, f, target)
        all_result[level][sum_up] = res
        return res % (10 ** 9 + 7)


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        total = d * f + 1
        if target > total - 1:
            return 0
        dp = [[0 for j in range(total)] for i in range(d + 1)]  # [level, sum]
        for i in range(1, d + 1):

            for j in range(1, total):
                if i == 1 and 0 < j <= f:
                    dp[i][j] = 1
                else:
                    temp = 0
                    for k in range(1, f + 1):
                        if j - k >= 0:
                            temp += dp[i - 1][j - k]
                    dp[i][j] = temp
        return dp[d][target] % (10 ** 9 + 7)
