
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        sum = [[0 for col in range(n)] for row in range(m)]
        for i in range(0,m):
            sum[i][0] = 1
        for j in range(0,n):
            sum[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                sum[i][j] = sum[i-1][j]+ sum[i][j-1]
        return sum[m-1][n-1]
