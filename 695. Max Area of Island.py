import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        queue = collections.deque()
        res = 0
        visited = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    queue.append((i, j))
                    visited[i][j] = True
                    area = 1
                    while len(queue) > 0:
                        # size = len(queue)
                        # for i in range(size):
                        row, col = queue.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == 1 and not visited[row - 1][col]:
                            area += 1
                            queue.append((row - 1, col))
                            visited[row - 1][col] = True
                        if row + 1 < n and grid[row + 1][col] == 1 and not visited[row + 1][col]:
                            area += 1
                            queue.append((row + 1, col))
                            visited[row + 1][col] = True
                        if col - 1 >= 0 and grid[row][col - 1] == 1 and not visited[row][col - 1]:
                            area += 1
                            queue.append((row, col - 1))
                            visited[row][col - 1] = True
                        if col + 1 < m and grid[row][col + 1] == 1 and not visited[row][col + 1]:
                            area += 1
                            queue.append((row, col + 1))
                            visited[row][col + 1] = True
                    res = max(res, area)
        return res

s = Solution()
# a = [[1,1,1]]
# print(s.maxAreaOfIsland(a))
# a = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# print(s.maxAreaOfIsland(a))

a = [[1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1],[1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,1],[1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0],[1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1],[1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,1],[1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,0],[0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1],[1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1],[0,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0],[0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1],[1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0],[1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0],[0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0],[1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0],[0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1],[1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1],[1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1],[1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0],[0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0],[1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0],[1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0],[0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1],[1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0],[0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1],[1,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0],[1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1],[0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0],[0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1],[0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0],[0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0],[0,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0],[0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,0],[0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0],[0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0],[0,0,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1],[0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1],[1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,1],[1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,1],[1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0],[0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0],[0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1],[1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1],[1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,0],[1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0],[0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0]]
print(s.maxAreaOfIsland(a))