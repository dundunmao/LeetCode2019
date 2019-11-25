class Solution:
    def maxDistance(self, grid):
        n = len(grid)
        m = len(grid[0])

        res_matrix = [[float('inf') for i in range(m)] for j in range(n)]
        res_matrix[0][0] = 0 if grid[0][0] == 1 else float('inf')
        for i in range(1, m):
            if grid[0][i] == 1:
                res_matrix[0][i] = 0
            else:
                res_matrix[0][i] = res_matrix[0][i - 1] + 1
        for i in range(1, n):
            if grid[i][0] == 1:
                res_matrix[i][0] = 0
            else:
                res_matrix[i][0] = res_matrix[i - 1][0] + 1

        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    res_matrix[i][j] = 0
                else:
                    res_matrix[i][j] = min(res_matrix[i-1][j], res_matrix[i][j-1]) + 1
        for i in range(m - 2, -1, -1):
            if grid[n - 1][i] == 1:
                res_matrix[n - 1][i] = 0
            else:
                res_matrix[n - 1][i] = min(res_matrix[n - 1][i], res_matrix[n - 1][i + 1] + 1)
        for i in range(n - 2, -1, -1):
            if grid[i][m - 1] == 1:
                res_matrix[i][m - 1] = 0
            else:
                res_matrix[i][m - 1] = min(res_matrix[i][m - 1], res_matrix[i + 1][m - 1] + 1)

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if grid[i][j] == 1:
                    res_matrix[i][j] = 0
                else:
                    res_matrix[i][j] = min(res_matrix[i][j], res_matrix[i + 1][j] + 1, res_matrix[i][j + 1] + 1)
        res = 0
        for i in range(0, n):
            for j in range(0, m):
                res = max(res, res_matrix[i][j])
        if res == 0 or res == float('inf'):
            return -1
        return res

s = Solution()
g = [[1,0,1],[0,0,0],[1,0,1]]
print(s.maxDistance(g))
g = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #-1
print(s.maxDistance(g))
g = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]] #-1
print(s.maxDistance(g))
g = [[0,0,1,1,1],[0,1,1,0,0],[0,0,1,1,0],[1,0,0,0,0],[1,1,0,0,1]]
print(s.maxDistance(g))
g = [[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]]
print(s.maxDistance(g))
g = [[1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],[1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],[0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],[0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],[1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],[0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],[1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],[0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],[0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],[1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],[1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],[0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]]
print(s.maxDistance(g))
