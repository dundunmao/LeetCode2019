class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # 以最上一行为起点
        for i in range(m):
            cur = matrix[0][i]
            row = 0
            col = i
            while row < n and col < m:
                if matrix[row][col] != cur:
                    return False
                row += 1
                col += 1
        # 以最左一列为起点
        for i in range(n):
            cur = matrix[i][0]
            row = i
            col = 0
            while row < n and col < m:
                if matrix[row][col] != cur:
                    return False
                row += 1
                col += 1
        return True
