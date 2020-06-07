from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return board
        m = len(board[0])
        if m == 0:
            return board
        record = [[False for i in range(m)] for j in range(n)]
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and board[i][j] == 'O':
                    record[i][j] = True
                    self.dfs(i, j, board, record, n, m, direction)
        # print(record)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not record[i][j]:
                    board[i][j] = 'X'

    def dfs(self, i, j, board, record, n, m, direction):

        for ele in direction:
            if 0 <= i + ele[0] < n and 0 <= j + ele[1] < m and board[i + ele[0]][j + ele[1]] == 'O' and not \
            record[i + ele[0]][j + ele[1]]:
                record[i + ele[0]][j + ele[1]] = True
                self.dfs(i + ele[0], j + ele[1], board, record, n, m, direction)
