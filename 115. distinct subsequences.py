# dag
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        res = [[float('-inf') for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(s, 0, t, 0, res)

    def dfs(self, s, i, t, j, res):
        n = len(s)
        m = len(t)
        if res[i][j] != float('-inf'):
            return res[i][j]
        if i == n and j == m:
            res[i][j] = 1
        elif i == n:
            res[i][j] = 0
        elif j == m:
            res[i][j] = self.dfs(s, i + 1, t, j, res)
        else:
            if s[i] == t[j]:
                res[i][j] = self.dfs(s, i + 1, t, j + 1, res) + self.dfs(s, i + 1, t, j, res)
            else:
                res[i][j] = self.dfs(s, i + 1, t, j, res)
        return res[i][j]


# dp
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        res = [[float('-inf') for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    res[i][j] = 1
                elif i == n:
                    res[i][j] = 0
                elif j == m:
                    res[i][j] = res[i + 1][j]
                else:
                    if s[i] == t[j]:
                        res[i][j] = res[i + 1][j + 1] + res[i + 1][j]
                    else:
                        res[i][j] = res[i + 1][j]
        return res[0][0]

# 滚动数组

class Solution3:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        res = [[float('-inf') for i in range(m + 1)] for j in range(2)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    res[i % 2][j] = 1
                elif i == n:
                    res[i % 2][j] = 0
                elif j == m:
                    res[i % 2][j] = res[(i + 1) % 2][j]
                else:
                    if s[i] == t[j]:
                        res[i % 2][j] = res[(i + 1) % 2][j + 1] + res[(i + 1) % 2][j]
                    else:
                        res[i % 2][j] = res[(i + 1) % 2][j]
        return res[0][0]
# 一个一维数组
class Solution4:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        res = [float('-inf') for i in range(m + 1)]
        for i in range(n, -1, -1):
            for j in range(m + 1):
                if i == n and j == m:
                    res[j] = 1
                elif i == n:
                    res[j] = 0
                elif j == m:
                    res[j] = res[j]
                else:
                    if s[i] == t[j]:
                        res[j] = res[j + 1] + res[j]
                    else:
                        res[j] = res[j]
        return res[0]

x = Solution4()
s = "rabbbit"
t = "rabbit"
print(x.numDistinct(s, t))
s = "babgbag"
t = "bag"
print(x.numDistinct(s, t))

