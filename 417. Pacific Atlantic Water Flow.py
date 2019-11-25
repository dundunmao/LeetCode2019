import collections
class Solution:
    def pacificAtlantic(self, matrix):
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []
        to_left_top = self.to_sea(matrix, 0, 0)
        to_right_bottom = self.to_sea(matrix, n - 1, m - 1)
        results = []
        for i in range(n):
            for j in range(m):
                if to_left_top[i][j] is True and to_right_bottom[i][j] is True:
                    res = []
                    res.append(i)
                    res.append(j)
                    results.append(res)
        return results

    def to_sea(self, matrix, start_row, start_col):
        n = len(matrix)
        m = len(matrix[0])
        queue = collections.deque()
        to_edge = [[False for i in range(m)] for j in range(n)]
        # 把第一行都放入queue里
        for i in range(m):
            to_edge[start_row][i] = True
            queue.append((start_row, i))
        # 把第一列放入queue里
        for i in range(n):
            to_edge[i][start_col] = True
            queue.append((i, start_col))

        while len(queue) > 0:
            row, col = queue.popleft()

            to_edge[row][col] = True

            if row - 1 >= 0 and matrix[row][col] <= matrix[row - 1][col] and to_edge[row - 1][col] is False:
                queue.append((row - 1, col))

            if row + 1 <len(matrix) and matrix[row][col] <= matrix[row + 1][col] and to_edge[row + 1][col] is False:
                queue.append((row + 1, col))

            if col - 1 >= 0 and matrix[row][col] <= matrix[row][col - 1] and to_edge[row][col - 1] is False:
                queue.append((row, col - 1))

            if col + 1 <len(matrix[0]) and matrix[row][col] <= matrix[row][col + 1] and to_edge[row][col + 1] is False:
                queue.append((row, col + 1))

        return to_edge

s = Solution()
a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(s.pacificAtlantic(a))
