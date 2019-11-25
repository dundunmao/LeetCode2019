class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        record_hash = {}
        record = [[None for i in range(len(board)[0])] for j in range(len(board))]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    self.dfs(i, j, record, n, m)

    def dfs(self, i, j, record, n, m, record_hash, board):
        if (i, j) in record_hash:
            return record_hash[(i, j)]
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            record_hash[(i, j)] = False
            return False
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for ele in direction:
            if board[i + ele[0]][j + ele[1]] == 'O':
                result = self.dfs(i + ele[0], j + ele[1], record)
                if result is False:
                    record_hash[i][j] = False
                    return False
        board[i][j] = 'X'
        record_hash[(i, j)] = True
        return True
