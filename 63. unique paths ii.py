
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0 for col in range(n)] for row in range(m)]
        for i in range(0, m):
            if obstacleGrid[i][0] != 1:
                paths[i][0] = 1
            else:
                break

        for j in range(0, n):
            if obstacleGrid[0][j] != 1:
                paths[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                else:
                    paths[i][j] = 0

        return paths[m - 1][n - 1]

# 自己练习
class Solution4:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code
        # edge case
        if obstacleGrid[0][0] == 1:
            return 0
        # initial
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[None for i in range(n)] for j in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
        if f[0][0] == 0:
            return 0
        else:
            f[0][0] = 1
        for i in range(1,n):
            if f[0][i] != 0:
                f[0][i] = f[0][i-1]
        for j in range(1,m):
            if f[j][0] != 0:
                f[j][0] = f[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                if f[i][j] != 0:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
if __name__ == '__main__':
    s = Solution4()
    x = [[0,0],[0,0],[0,0],[1,0],[0,0]]
    print s.uniquePathsWithObstacles(x)
