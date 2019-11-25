class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        t = s[::-1]
        f = [[0 for i in range(n + 1)] for j in range(n + 1)]
        # print(f)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    f[i][j] = 1 + f[i + 1][j + 1]
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j + 1])
        return f[0][0]


class Solution1(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [[1 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i + 1 == j:
                        f[i][j] = 2
                    else:
                        f[i][j] = 2 + f[i + 1][j - 1]
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]

s = Solution1()
a = 'bbbab'
print(s.longestPalindromeSubseq(a))
