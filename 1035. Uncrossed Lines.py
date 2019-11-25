1153. String Transforms Into Another String
# DAG
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        res = [[float('-inf') for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(A, 0, B, 0, res)

    def dfs(self, A, i, B, j, res):
        if res[i][j] != float('-inf'):
            return res[i][j]
        n = len(A)
        m = len(B)
        if i == n or j == m:
            res[i][j] = 0
        else:
            if A[i] == B[j]:
                res[i][j] = max(1 + self.dfs(A, i + 1, B, j + 1, res), self.dfs(A, i + 1, B, j, res),
                                self.dfs(A, i, B, j + 1, res))
            else:
                res[i][j] = max(self.dfs(A, i + 1, B, j, res), self.dfs(A, i, B, j + 1, res))
        return res[i][j]
#DP
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        res = [[float('-inf') for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    res[i][j] = 0
                else:
                    if A[i] == B[j]:
                        res[i][j] = max(1 + res[i + 1][j + 1], res[i + 1][j], res[i][j + 1])
                    else:
                        res[i][j] = max(res[i + 1][j], res[i][j + 1])
        return res[0][0]


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        res = [[float('-inf') for i in range(m + 1)] for j in range(2)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n or j == m:
                    res[i % 2][j] = 0
                else:
                    if A[i] == B[j]:
                        res[i % 2][j] = max(1 + res[(i + 1) % 2][j + 1], res[(i + 1) % 2][j], res[i % 2][j + 1])
                    else:
                        res[i % 2][j] = max(res[(i + 1) % 2][j], res[i % 2][j + 1])
        return res[0][0]
