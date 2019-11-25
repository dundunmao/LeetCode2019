import collections
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        queue = collections.deque()
        visited = [[False for i in range(m)] for j in range(n)]
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
        level = 0
        while len(queue) > 0:
            size = len(queue)
            level += 1
            for i in range(size):
                row, col = queue.popleft()
                if row - 1 >= 0 and matrix[row - 1][col] == 1 and not visited[row - 1][col]:
                    res[row - 1][col] = level
                    queue.append((row - 1, col))
                    visited[row - 1][col] = True
                if row + 1 < n and matrix[row + 1][col] == 1 and not visited[row + 1][col]:
                    res[row + 1][col] = level
                    queue.append((row + 1, col))
                    visited[row + 1][col] = True
                if col - 1 >= 0 and matrix[row][col - 1] == 1 and not visited[row][col - 1]:
                    res[row][col - 1] = level
                    queue.append((row, col - 1))
                    visited[row][col - 1] = True
                if col + 1 < m and matrix[row][col + 1] == 1 and not visited[row][col + 1]:
                    res[row][col + 1] = level
                    queue.append((row, col + 1))
                    visited[row][col + 1] = True
        return res
s = Solution()

a = [[0,0,0],[0,1,0],[0,0,0]]

print(s.updateMatrix(a))

a = [[0,0,0],[0,1,0],[1,1,1]]

print(s.updateMatrix(a))
