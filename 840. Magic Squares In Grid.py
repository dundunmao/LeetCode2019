from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if grid[i + 1][j + 1] != 5:
                    continue
                if self.magic(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                              grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                              grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]):
                    ans += 1
        return ans
    def magic(self, a1, a2, a3, b1, b2, b3, c1, c2, c3):
        return sorted([a1, a2, a3, b1, b2, b3, c1, c2, c3]) == [1,2,3,4,5,6,7,8,9] and \
               (a1 + a2 + a3 == b1 + b2 + b3 == c1 + c2 + c3 == a1 + b1 + c1 == a2 + b2 + c2 == a3 + b3 + c3 == a1 + b2 + c3 == a3 + b2 + c1 == 15)
s = Solution()
a = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(s.numMagicSquaresInside(a))
