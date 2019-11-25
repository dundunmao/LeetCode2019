# dag
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        res = [[None for j in range(m + 1)] for i in range(n + 1)]
        i = 0
        j = 0
        return self.dfs(text1, text2, i, j, res)

    def dfs(self, text1, text2, i, j, res):
        if res[i][j] is not None:
            return res[i][j]
        # base case
        if i == len(text1) or j == len(text2):
            res[i][j] = 0
            return res[i][j]
        else:
            # general case
            if text1[i] == text2[j]:
                res[i][j] = 1 + self.dfs(text1, text2, i + 1, j + 1, res)
            else:
                res[i][j] = max(self.dfs(text1, text2, i, j + 1, res), self.dfs(text1, text2, i + 1, j, res))

        return res[i][j]





# dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        f = [[None for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    f[i][j] = 0
                elif text1[i] == text2[j]:
                    f[i][j] = 1 + f[i + 1][j + 1]
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j + 1])
        return f[0][0]

# dp 滚动数组，在f[i]的i上加%2
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        f = [[None for j in range(m + 1)] for i in range(2)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    f[i % 2][j] = 0
                elif text1[i] == text2[j]:
                    f[i % 2][j] = 1 + f[(i + 1) % 2][j + 1]
                else:
                    f[i % 2][j] = max(f[(i + 1) % 2][j], f[i % 2][j + 1])
        return f[0][0]

# 一维数组，用pre,cur,temp记录
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        pre = [None for i in range(m + 1)]
        cur = [None for i in range(m + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    cur[j] = 0
                elif text1[i] == text2[j]:
                    cur[j] = 1 + pre[j + 1]
                else:
                    cur[j] = max(pre[j], cur[j + 1])
            cur, pre = pre, cur

        return pre[0]

# n < m
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        pre = [None for i in range(n + 1)]
        cur = [None for i in range(n + 1)]

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m or j == n:
                    cur[j] = 0
                elif text2[i] == text1[j]:
                    cur[j] = 1 + pre[j + 1]
                else:
                    cur[j] = max(pre[j], cur[j + 1])
            cur, pre = pre, cur

        return pre[0]






