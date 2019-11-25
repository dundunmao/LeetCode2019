class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=='':
            return True
        if t == '':
            return False
        j = 0
        i = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]: #如果找到i就往后走
                i +=1
            j += 1     #找不找得到j都往后走

        return i == len(s)

# 二维dp
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        f = [[False for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    f[i][j] = True
                elif j == m:
                    f[i][j] = False
                elif i == n:
                    f[i][j] = True
                else:
                    if s[i] == t[j]:
                        f[i][j] = f[i + 1][j + 1]
                    else:
                        f[i][j] = f[i][j + 1]
        return f[0][0]

# 一维dp
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        cur = [False for j in range(m + 1)]
        prev = [False for j in range(m + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    cur[j] = True
                elif j == m:
                    cur[j] = False
                elif i == n:
                    cur[j] = True
                else:
                    if s[i] == t[j]:
                        cur[j] = prev[j + 1]
                    else:
                        cur[j] = cur[j + 1]
            cur, prev = prev, cur
        return prev[0]

# 线模型

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == n
