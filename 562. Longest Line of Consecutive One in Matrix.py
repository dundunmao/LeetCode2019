class Solution:
    def longestLine(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        horizontal = [[0 for j in range(m)] for i in range(n)]
        vertical = [[0 for j in range(m)] for i in range(n)]
        diagnal = [[0 for j in range(m)] for i in range(n)]
        antidiagnal = [[0 for j in range(m)] for i in range(n)]

        maxi = 0
        result = 0

        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    horizontal[i][j] = 0
                    vertical[i][j] = 0
                    diagnal[i][j] = 0
                    antidiagnal[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        horizontal[i][j] = 1
                        vertical[i][j] = 1
                        diagnal[i][j] = 1
                        antidiagnal[i][j] = 1
                    elif i == 0:
                        horizontal[i][j] = horizontal[i][j - 1] + 1
                        vertical[i][j] = 1
                        diagnal[i][j] = 1
                        antidiagnal[i][j] = 1
                    elif j == 0:
                        horizontal[i][j] = 1
                        vertical[i][j] = vertical[i - 1][j] + 1
                        diagnal[i][j] = 1
                        antidiagnal[i][j] = 1 if j == m - 1 else antidiagnal[i - 1][j + 1] + 1
                    else:
                        horizontal[i][j] = horizontal[i][j - 1] + 1
                        vertical[i][j] = vertical[i - 1][j] + 1
                        diagnal[i][j] = diagnal[i - 1][j - 1] + 1
                        antidiagnal[i][j] = 1 if j == m - 1 else antidiagnal[i - 1][j + 1] + 1
                result = max(result, horizontal[i][j], vertical[i][j], diagnal[i][j], antidiagnal[i][j])
        return result

s = Solution()
a = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
print(s.longestLine(a))
