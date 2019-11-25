class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[0 for i in range(N)] for j in range(N)]
        # 按题意更新grid
        for i in range(len(mines)):
            row = mines[i][0]
            col = mines[i][1]
            grid[row][col] = 1
        # （i,j）这点的左臂能多长（往左能走多远）
        left_range = [[0 for i in range(N)] for j in range(N)]
        right_range = [[0 for i in range(N)] for j in range(N)]
        # （i,j）这点的上臂能多长（往上能走多远）
        up_range = [[0 for i in range(N)] for j in range(N)]
        down_range = [[0 for i in range(N)] for j in range(N)]

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    if i > 0:
                        up_range[i][j] = up_range[i - 1][j] + 1
                    else:
                        up_range[i][j] = 1

                    if j > 0:
                        left_range[i][j] = left_range[i][j - 1] + 1
                    else:
                        left_range[i][j] = 1

        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if grid[i][j] == 0:
                    if i < N - 1:
                        down_range[i][j] = down_range[i + 1][j] + 1
                    else:
                        down_range[i][j] = 1

                    if j < N - 1:
                        right_range[i][j] = right_range[i][j + 1] + 1
                    else:
                        right_range[i][j] = 1

        res = 0
        for i in range(N):
            for j in range(N):
                #检查每一个为0的点，上下取最短，左右取最短，就是该店的order
                if grid[i][j] == 0:
                    horizon_range = min(left_range[i][j], right_range[i][j])
                    vertical_range = min(up_range[i][j], down_range[i][j])
                    cur_range = min(horizon_range, vertical_range)
                    res = max(cur_range, res)

        return res


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0 for i in range(N)] for j in range(N)]
        ans = 0


        #从上到下，横着做一遍
        for r in range(N):
            count = 0
            # 从左到右的遍历。
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            # 从右到左的遍历。
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                # 跟从左到右的比较一下，取最小
                if count < dp[r][c]:
                    dp[r][c] = count
        # 从左到右，竖着做一遍，同时更新ans
        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]
        return ans
