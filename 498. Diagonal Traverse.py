class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        n = len(matrix)
        m = len(matrix[0])
        res = [0] * m * n
        row = 0
        col = 0
        d = 0
        dirs = [(-1, 1), (1, -1)]

        for i in range(m * n):
            res[i] = matrix[row][col]
            row += dirs[d][0]
            col += dirs[d][1]

            if row >= n:
                row = n - 1
                col += 2
                d = 1 - d

            if col >= m:
                col = m - 1
                row += 2
                d = 1 - d

            if row < 0:
                row = 0
                d = 1 - d

            if col < 0:
                col = 0
                d = 1 - d

        return res
