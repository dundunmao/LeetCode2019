class NumMatrix:

    def __init__(self, matrix):

        n = len(matrix)
        m = len(matrix[0])

        self.presum_matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            presum_row = 0
            for j in range(m):
                presum_row += matrix[i][j]
                if i == 0:
                    self.presum_matrix[i][j] = presum_row
                else:
                    self.presum_matrix[i][j] = presum_row + self.presum_matrix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if row1 - 1 == -1 and col1 - 1 == -1:
            res = self.presum_matrix[row2][col2]
        elif row1 -1 == -1:
            res = self.presum_matrix[row2][col2]
            res -= self.presum_matrix[row2][col1 - 1]
        elif col1 - 1 == -1:
            res = self.presum_matrix[row2][col2]
            res -= self.presum_matrix[row1 - 1][col2]
        else:
            res = self.presum_matrix[row2][col2]
            res -= self.presum_matrix[row1 - 1][col2]
            res -= self.presum_matrix[row2][col1 - 1]
            res += self.presum_matrix[row1 - 1][col1 - 1]
        return res











