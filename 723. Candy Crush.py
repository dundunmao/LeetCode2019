from typing import List
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])
        # repeat crush and drop
        while True:
            candy = set()
            # check every row
            for i in range(n):
                for j in range(2, m):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        candy.add((i, j))
                        candy.add((i, j - 1))
                        candy.add((i, j - 2))
            # check every col
            for j in range(m):
                for i in range(2, n):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        candy.add((i, j))
                        candy.add((i - 1, j))
                        candy.add((i - 2, j))

            if not candy:
                break
            for i, j in candy:
                board[i][j] = 0
            # moving zeros
            for j in range(m):
                start = n - 1
                for i in range(n - 1, -1, -1):
                    if board[i][j] != 0:
                        board[i][j], board[start][j] = board[start][j], board[i][j]
                        start -= 1

        return board
s = Solution()
a = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
print((s.candyCrush(a)))
