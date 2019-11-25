import collections
class Solution:
    def numEnclaves(self, A):
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        if m == 0:
            return 0
        hash = [[False for i in range(m)] for j in range(n)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and A[i][j] == 1:
                    A[i][j] = 0
                    self.bfs(i, j, directions, n, m, A)
        res = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    res += 1
        return res

    def bfs(self, row, col, directions, n, m, A):
        queue = collections.deque()
        queue.append((row, col))
        while len(queue):
            row, col = queue.popleft()
            for x, y in directions:
                if 0 <= row + x < n and 0 <= col + y < m and A[row + x][col + y] == 1:
                    A[row + x][col + y] = 0
                    queue.append((row + x, col + y))

s = Solution()
a = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.numEnclaves(a))
a = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(s.numEnclaves(a))

