class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        res = [[0 for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(s1, 0, s2, 0, res)
    def dfs(self, s1, i, s2, j, res):
        if res[i][j] != 0:
            return res[i][j]
        n = len(s1)
        m = len(s2)
        if i == n and j == m:
            res[i][j] = 0
        elif i == n:
            res[i][j] = ord(s2[j]) + self.dfs(s1, i, s2, j + 1, res)
        elif j == m:
            res[i][j] = ord(s1[i]) + self.dfs(s1, i + 1, s2, j, res)
        else:
            if s1[i] == s2[j]:
                res[i][j] = self.dfs(s1, i + 1, s2, j + 1, res)
            else:
                res[i][j] = min(ord(s1[i]) + self.dfs(s1, i + 1, s2, j, res), ord(s2[j]) + self.dfs(s1, i, s2, j + 1, res))
        return res[i][j]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        res = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    res[i][j] = 0
                elif i == n:
                    res[i][j] = ord(s2[j]) + res[i][j + 1]
                elif j == m:
                    res[i][j] = ord(s1[i]) + res[i + 1][j]
                else:
                    if s1[i] == s2[j]:
                        res[i][j] = res[i + 1][j + 1]
                    else:
                        res[i][j] = min(ord(s1[i]) + res[i + 1][j], ord(s2[j]) + res[i][j + 1])
        return res[0][0]

x = Solution()
s = "sea"
p = "eat"
print(x.minimumDeleteSum(s, p))
s = "delete"
p = "leet"
print(x.minimumDeleteSum(s, p))
