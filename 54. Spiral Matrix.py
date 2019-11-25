class Solution:
    def spiralOrder(self, matrix):
        result = []
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        row_start = 0
        col_start = 0
        row_end = n - 1
        col_end = m - 1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1

            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
            row_end -= 1

            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
            col_start += 1

        return result
s = Solution()
a = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(a))
