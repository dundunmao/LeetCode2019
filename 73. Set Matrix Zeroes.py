

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        array_x = []
        array_y = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    array_x.append(i)
                    array_y.append(j)
        for i in array_x:
            matrix[i] = [0]*n
        for i in range(m):
            for j in array_y:
                matrix[i][j] = 0
        return matrix
if __name__ == "__main__":
    s = Solution()
    m = [
            [1, 2],
            [0, 3]
        ]

    print s.setZeroes(m)



