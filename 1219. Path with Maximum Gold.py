from typing import List


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # all_res = [[0 for i in range(m)] for j in range(n)]
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    visited.add((i, j))
                    res = max(res, self.dfs(i, j, visited, all_res, grid, directions))
                    visited.remove((i, j))
        return res

    def dfs(self, i, j, visited, all_res, grid, directions):
        # if all_res[i][j] > 0:
        #     return all_res[i][j]
        result = 0
        for r, c in directions:
            row = i + r
            col = j + c
            if self.valid(row, col, grid, visited):
                visited.add((row, col))
                result = max(result, self.dfs(row, col, visited, all_res, grid, directions))
                visited.remove((row, col))
        # all_res[i][j] = result + grid[i][j]
        return all_res[i][j]

    def valid(self, i, j, grid, visited):
        if (i, j) in visited:
            return False
        if i < 0 or i >= len(grid):
            return False
        if j < 0 or j >= len(grid[0]):
            return False
        if grid[i][j] == 0:
            return False
        return True


s = Solution()
a = [[0,6,0],[5,8,7],[0,9,0]]
print(s.getMaximumGold(a))
# a = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# print(s.getMaximumGold(a))

