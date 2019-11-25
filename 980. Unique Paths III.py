class Solution:
    def __init__(self):
        self.start = 1
        self.end = 2
        self.zero = 0
        self.obstacle = -1

    def uniquePathsIII(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        start_row = -1
        start_col = -1
        zero_total = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == self.start:
                    start_row = i
                    start_col = j
                elif grid[i][j] == self.zero:
                    zero_total += 1
        return self.dfs(grid, start_row, start_col, zero_total, visited, 1)

    def dfs(self, grid, row, col, zero_total, visited, depth):
        visited[row][col] = True
        result = 0
        # base case
        if grid[row][col] == self.end and depth == zero_total + 2:
            result = 1
        # general case
        else:
            if row - 1 >= 0 and grid[row - 1][col] != self.obstacle and visited[row - 1][col] is False:
                result += self.dfs(grid, row - 1, col, zero_total, visited, depth + 1)

            if row + 1 < len(grid) and grid[row + 1][col] != self.obstacle and visited[row + 1][col] is False:
                result += self.dfs(grid, row + 1, col, zero_total, visited, depth + 1)

            if col - 1 >= 0 and grid[row][col - 1] != self.obstacle and visited[row][col - 1] is False:
                result += self.dfs(grid, row, col - 1, zero_total, visited, depth + 1)

            if col + 1 < len(grid[0]) and grid[row][col + 1] != self.obstacle and visited[row][col + 1] is False:
                result += self.dfs(grid, row, col + 1, zero_total, visited, depth + 1)

        visited[row][col] = False

        return result

s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(s.uniquePathsIII(grid))
