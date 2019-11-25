# dag
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        res = [[None for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(s, 0, p, 0, res)

    def dfs(self, s, i, p, j, res):
        if res[i][j] is not None:
            return res[i][j]
        n = len(s)
        m = len(p)
        if i == n and j == m:
            res[i][j] = True
        elif i == n:
            if p[j] == '*':
                res[i][j] = self.dfs(s, i, p, j + 1, res)
            # res[i][j] = True
            # k = j
            # while k < m:
            #     if p[k] != '*':
            #         res[i][j] = False
            #         break
            #     k += 1
        elif j == m:
            res[i][j] = False
        else:
            if p[j] == s[i] or p[j] == '?':
                res[i][j] = self.dfs(s, i + 1, p, j + 1, res)
            else:
                if p[j] != '*':
                    res[i][j] = False
                else:
                    res[i][j] = self.dfs(s, i + 1, p, j, res) or self.dfs(s, i, p, j + 1, res)
        return res[i][j]

# dp

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        res = [[None for i in range(m + 1)] for j in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    res[i][j] = True
                elif j == m:
                    res[i][j] = False
                elif i == n:
                    if p[j] == '*':
                        res[i][j] = res[i][j + 1]
                    else:
                        res[i][j] = False
                else:
                    if p[j] == s[i] or p[j] == '?':
                        res[i][j] = res[i + 1][j + 1]
                    else:
                        if p[j] != '*':
                            res[i][j] = False
                        else:
                            res[i][j] = res[i + 1][j] or res[i][j + 1]
        return res[0][0]
x = Solution()
s = "aa"
p = "*"
print(x.isMatch(s, p))
s = ""
p = "*"
print(x.isMatch(s, p))
