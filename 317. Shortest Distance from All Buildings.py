import collections
class Solution:
    def shortestDistance(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        count_building = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = [[0 for i in range(m)] for j in range(n)]
        can_reach = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    res[i][j] = float('inf')
                if grid[i][j] == 1:
                    count_building += 1
                    visited = set()
                    self.bfs(grid, i, j, directions, visited, res, can_reach)
        ans = float('inf')
        for i in range(n):
            for j in range(m):
                if can_reach[i][j] == count_building:
                    ans = min(ans, res[i][j])
        return ans

    def bfs(self, grid, i, j, directions, visited, res, can_reach):
        q = collections.deque()
        q.append((i, j))
        step = 1
        visited.add((i, j))
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                for direction in directions:
                    if self.valid(grid, cur, direction) and (cur[0] + direction[0], cur[1] + direction[1]) not in visited:
                        res[cur[0] + direction[0]][cur[1] + direction[1]] += step
                        can_reach[cur[0] + direction[0]][cur[1] + direction[1]] += 1
                        q.append((cur[0] + direction[0], cur[1] + direction[1]))
                        visited.add((cur[0] + direction[0], cur[1] + direction[1]))
            step += 1

    def valid(self, grid, cur, direction):
        if not 0 <= cur[0] + direction[0] < len(grid):
            return False
        if not 0 <= cur[1] + direction[1] < len(grid[0]):
            return False
        if grid[cur[0] + direction[0]][cur[1] + direction[1]] != 0:
            return False
        return True
s = Solution()
a = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(s.shortestDistance(a))
