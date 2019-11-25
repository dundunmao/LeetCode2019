# 超时dfs
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        is_palindrome_set = {}
        visited = {}
        return self.dfs(s, k, is_palindrome_set, visited)

    def dfs(self, s, k, is_palindrome_set, visited):
        if (s, k) in visited:
            return visited[(s, k)]
        if k == 0:
            if s in is_palindrome_set:
                res = is_palindrome_set[s]
            else:
                res = self.is_palindrome(s)
            if res:
                is_palindrome_set[s] = True
                return True
            else:
                is_palindrome_set[s] = False
                return False
        res = False
        for i in range(len(s)):
            new = s[:i] + s[i + 1:]
            res |= self.dfs(new, k - 1, is_palindrome_set, visited)
        visited[(s, k)] = res
        return res

    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
# DP

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        f = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i + 1 == j:
                        f[i][j] = 0
                    else:
                        f[i][j] = f[i + 1][j - 1]
                else:
                    f[i][j] = 1 + min(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1] <= k
