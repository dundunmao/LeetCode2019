### DAG
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        all_result = [[None for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(s, 0, p, 0, all_result)

    def dfs(self, s, i, p, j, all_result):
        if all_result[i][j] is not None:
            return all_result[i][j]
        n = len(s)
        m = len(p)

        if i == n and j == m:
            all_result[i][j] = True
        elif j == m:
            all_result[i][j] = False
        elif i == n:
            if j + 1 < m and p[j + 1] == '*':
                all_result[i][j] = self.dfs(s, i, p, j + 2, all_result)
            else:
                all_result[i][j] = False
        else:
            if j + 1 < m and p[j + 1] == '*':
                if p[j] != '.' and p[j] != s[i]:
                    all_result[i][j] = self.dfs(s, i, p, j + 2, all_result)
                else:
                    all_result[i][j] = self.dfs(s, i, p, j + 2, all_result) or self.dfs(s, i + 1, p, j, all_result)
            else:
                if p[j] != '.' and p[j] != s[i]:
                    all_result[i][j] = False
                else:
                    all_result[i][j] = self.dfs(s, i + 1, p, j + 1, all_result)

        return all_result[i][j]

#### DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        all_result = [[None for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    all_result[i][j] = True
                elif j == m:
                    all_result[i][j] = False
                elif i == n:
                    if j + 1 < m and p[j + 1] == '*':
                        all_result[i][j] = all_result[i][j + 2]
                    else:
                        all_result[i][j] = False
                else:
                    if j + 1 < m and p[j + 1] == '*':
                        if p[j] != '.' and p[j] != s[i]:
                            all_result[i][j] = all_result[i][j + 2]
                        else:
                            all_result[i][j] = all_result[i][j + 2] or all_result[i + 1][j]
                    else:
                        if p[j] != '.' and p[j] != s[i]:
                            all_result[i][j] = False
                        else:
                            all_result[i][j] = all_result[i + 1][j + 1]
        return all_result[0][0]

# 换个方向的dp
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        l_s = len(s)
        l_p = len(p)
        f = [[False for j in range(l_p + 1)] for i in range(l_s + 1)]
        f[0][0] = True
        for i in range(1, l_p):
            if p[i] == '*' and f[0][i - 1]:
                f[0][i + 1] = True
        for i in range(0, l_s):
            for j in range(0, l_p):
                if p[j] == '.':
                    f[i + 1][j + 1] = f[i][j]
                if p[j] == s[i]:
                    f[i + 1][j + 1] = f[i][j]
                if p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        f[i + 1][j + 1] = f[i + 1][j] or f[i + 1][j - 1] or f[i][j + 1]

                    else:
                        f[i + 1][j + 1] = f[i + 1][j - 1]
        return f[l_s][l_p]

if __name__ == "__main__":

    s = "ab"
    p = "a.*"
    x = Solution()
    print(x.isMatch(s,p)) #T
    s = "aab"
    p = "c*a*b"
    print(x.isMatch(s, p))#T
    s = "aa"
    p = "a*"
    print(x.isMatch(s, p)) #T

