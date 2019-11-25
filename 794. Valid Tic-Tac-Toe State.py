class Solution:
    def validTicTacToe(self, board):
        count_x = 0
        count_o = 0
        for ele in board:
            for cha in ele:
                if cha == 'O':
                    count_o += 1
                elif cha == 'X':
                    count_x += 1
        # 如果不相等，o不只比x多1个，就False
        if count_o != count_x and count_o + 1 != count_x:
            return False
        # 如果 X 赢了，x必须比o多一个
        if self.win(board, 'X') and count_o != count_x - 1:
            return False
        # 如果 O 赢了，他俩必须count相等
        if self.win(board, 'O') and count_o != count_x:
            return False
        return True

    def win(self, board, player):
        for i in range(3):
            # 如果player一排满了，赢
            if player == board[0][i] and player == board[1][i] and player == board[2][i]:
                return True
            # 如果player一列满了，赢
            if player == board[i][0] and player == board[i][1] and player == board[i][2]:
                return True
        # 如果左斜都是player，赢
        if player == board[0][0] and player == board[1][1] and player == board[2][2]:
            return True
        # 如果右斜都是player，赢
        if player == board[0][2] and player == board[1][1] and player == board[2][0]:
            return True
        return False
s = Solution()
a = ["   ","   ","   "]
print(s.validTicTacToe(a))
