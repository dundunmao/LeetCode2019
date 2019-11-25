class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        if m > 0:
            n = len(matrix[0])
        else:
            return result
        f = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            f[i][0] = matrix[i][0]
            result = max(f[i][0], result)
            for j in range(1,n):
                if i>0:
                    if matrix[i][j]>0:
                        f[i][j] = min(f[i-1][j], min(f[i][j-1], f[i-1][j-1]))+1
                    else:
                        f[i][j] = 0
                else:
                    f[i][j] = matrix[i][j]
                result = max(f[i][j], result)
        return result*result

    def maxSquare1(self, matrix):
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        if m > 0:
            n = len(matrix[0])
        else:
            return result
        f = [[0 for i in range(n)] for j in range(2)]
        for i in range(m):
            f[i%2][0] = matrix[i][0]
            result = max(f[i%2][0], result)
            for j in range(1, n):
                if i > 0:
                    if matrix[i][j] > 0:
                        f[i%2][j] = min(f[(i - 1)%2][j], min(f[i%2][j - 1], f[(i-1)%2][j - 1])) + 1
                    else:
                        f[i%2][j] = 0
                else:
                    f[i%2][j] = matrix[i%2][j]
                result = max(f[i%2][j], result)
        return result * result


class Solution:
    def maximalSquare(self, matrix):
        if matrix == [] or matrix == [[]]:
            return 0
        res = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
        if matrix[0][0] == '0':
            res[0][0] = Node(0, 0, 0)
            result = 0
        else:
            res[0][0] = Node(1, 1, 1)
            result = 1

        for i in range(1, len(matrix)):
            res[i][0] = Node(0, 0, 0) if matrix[i][0] == '0' else Node(1, res[i - 1][0].vertical + 1, 1)
            result = max(result, res[i][0].squre_side)
        for j in range(1, len(matrix[0])):
            res[0][j] = Node(0, 0, 0) if matrix[0][j] == '0' else Node(1, 1, res[0][j - 1].horizontal + 1)
            result = max(result, res[0][j].squre_side)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    res[i][j] = Node(0, 0, 0)
                else:
                    vertical = res[i - 1][j].vertical + 1
                    horizontal = res[i][j - 1].horizontal + 1
                    squre_side = min(res[i - 1][j - 1].squre_side + 1, vertical, horizontal)
                    result = max(result, squre_side)
                    res[i][j] = Node(squre_side, vertical, horizontal)
        return result ** 2

class Node:
    def __init__(self, squre_side, vertical, horizontal):
        self.squre_side = squre_side
        self.vertical = vertical
        self.horizontal = horizontal

s = Solution()
x = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalSquare(x))
x = [["0"]]
print(s.maximalSquare(x))

