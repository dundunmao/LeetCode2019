class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # edge case
        if dungeon == [] or len(dungeon[0]) == 0:
            return 0
        m = len(dungeon)
        n = len(dungeon[0])
        f = [[0 for i in range(n)] for j in range(m)]  # 为到达(i,j)之前血量有多少
        f[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)  # 如果这里是负的，到达这里之前血量要为减去这里的数之后为1;如果这里是正的，我们到达这里之前血量至少为1就可以，
        for i in range(m - 2, -1, -1):  # 右边一列
            f[i][n - 1] = max(f[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):  # 最下一排
            f[m - 1][j] = max(f[m - 1][j + 1] - dungeon[m - 1][j], 1)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = max(f[i + 1][j] - dungeon[i][j], 1)  #保证下面那格为正的
                right = max(f[i][j + 1] - dungeon[i][j], 1) #保证右面那格为正的
                f[i][j] = min(down, right) #保证上述两个方向最小的那个就行。

        return f[0][0]
if __name__ == "__main__":
    x = Solution()
    # a = [[0,0]]
    # print x.calculateMinimumHP(a)
    a = [[0, 5], [-2, -3]]
    print x.calculateMinimumHP(a)
