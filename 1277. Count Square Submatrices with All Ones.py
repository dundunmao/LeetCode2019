class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for j in range(C + 1)] for J in range(R+1)] # new int[R+1][C+1];
        ans = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j]:
                    dp[i+1][j+1] = 1+min(dp[i][j+1], dp[i+1][j], dp[i][j])
                    ans += dp[i+1][j+1]
        return ans     
