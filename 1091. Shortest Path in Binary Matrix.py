# dfs Time Limit Exceeded
class Solution:
    def __init__(self):
        self.end_row = 0
        self.end_col = 0

    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        self.end_row = n - 1
        self.end_col = n - 1
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        dirction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        result = Result(float('inf'))
        row_path = []
        col_path = []
        path_set = set()
        self.dfs(grid, 1, 0, 0, row_path, col_path, dirction, result, path_set)
        return result.res if result.res != float('inf') else -1

    def dfs(self, grid, depth, row, col, row_path, col_path, dirction, result, path_set):
        if row == self.end_row and col == self.end_col:
            result.res = min(result.res, depth)
            return
        for ele in dirction:
            cur_row = row + ele[0]
            cur_col = col + ele[1]
            # print(cur_row, cur_col)
            if (cur_row,
                cur_col) not in path_set and cur_row >= 0 and cur_row <= self.end_row and cur_col >= 0 and cur_col <= self.end_col and \
                    grid[cur_row][
                        cur_col] == 0:
                row_path.append(cur_row)
                col_path.append(cur_col)
                path_set.add((cur_row, cur_col))
                self.dfs(grid, depth + 1, cur_row, cur_col, row_path, col_path, dirction, result, path_set)
                path_set.remove((cur_row, cur_col))
                row_path.pop()
                col_path.pop()

class Result:
    def __init__(self, res):
        self.res = res


import collections

class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        dirction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        path_set = set()
        path_deque = collections.deque()
        path_deque.append((0, 0, 1))
        while len(path_deque) > 0:
            cur = path_deque.popleft()
            if cur[0] == n - 1 and cur[1] == n - 1:
                return cur[2]
            for ele in dirction:
                cur_row = cur[0] + ele[0]
                cur_col = cur[1] + ele[1]
                if (cur_row, cur_col) not in path_set and cur_row >= 0 and cur_row < n and cur_col >= 0 and cur_col < n and grid[cur_row][cur_col] == 0:
                    path_set.add((cur_row, cur_col))
                    path_deque.append((cur_row, cur_col, cur[2] + 1))
        return -1

s = Solution1()

a = [[0,1],[1,0]] #2
print(s.shortestPathBinaryMatrix(a))

a = [[0,0,0],[1,1,0],[1,1,0]] #4
print(s.shortestPathBinaryMatrix(a))

a = [[1,0,0],[1,1,0],[1,1,0]] #-1
print(s.shortestPathBinaryMatrix(a))

a = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
print(s.shortestPathBinaryMatrix(a))

