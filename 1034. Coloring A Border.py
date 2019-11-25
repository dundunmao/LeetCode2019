import collections
class Solution:
    def colorBorder(self, A, r0, c0, color):
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        if m == 0:
            return 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        hash = [[False for i in range(m)] for j in range(n)]
        cur_color = A[r0][c0]
        hash[r0][c0] = True
        self.bfs(r0, c0, directions, n, m, A, hash, cur_color, res)
        for row, col in res:
            A[row][col] = color
        return A

    def bfs(self, row, col, directions, n, m, A, hash, cur_color, res):
        queue = collections.deque()
        queue.append((row, col))

        while len(queue):
            row, col = queue.popleft()
            if not ((row - 1 >= 0 and A[row - 1][col] == cur_color) and (row + 1 < n and A[row + 1][col] == cur_color) and (
                    col - 1 >= 0 and A[row][col - 1] == cur_color) and (col + 1 < m and A[row][col + 1] == cur_color)):
                res.append([row, col])
            for x, y in directions:
                if 0 <= row + x < n and 0 <= col + y < m and not hash[row + x][col + y] and A[row + x][col + y] == cur_color:
                    queue.append((row + x, col + y))
                    hash[row + x][col + y] = True


s = Solution()
a = [[2,1,2,2,1],[1,1,1,1,1],[2,2,2,1,2],[1,2,2,1,2],[2,1,1,1,2]]
r0 = 1
c0 = 4
color = 2
print(s.colorBorder(a, r0, c0, color))
