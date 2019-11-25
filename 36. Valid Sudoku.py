
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #  对于每一行
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] != '.' and row.has_key(board[i][j]):
                    return False
                else:
                    row[board[i][j]]=True
        #  对于每一列
        for j in range(9):
            col = {}
            for i in range(9):
                if board[i][j] != '.' and col.has_key(board[i][j]):
                    return False
                else:
                    col[board[i][j]] = True
        #  对于每一个cube
        for i in range(9):
            cube = {}
            for j in range(9):
                row_index = 3*(i/3)
                col_index = 3*(i%3)
                if board[row_index+j/3][col_index + j%3] != '.' and cube.has_key(board[row_index + j/3][col_index + j%3]):
                    return False
                else:
                     cube[board[row_index + j/3][col_index + j%3]] = True
        return True


class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #  对于每一行
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] != '.' and row.has_key(board[i][j]):
                    return False
                else:
                    row[board[i][j]] = True
        # 对于每一列
        for j in range(9):
            col = {}
            for i in range(9):
                if board[i][j] != '.' and col.has_key(board[i][j]):
                    return False
                else:
                    col[board[i][j]] = True

        cell = {}
        for i in range(0, 9):
            x = i / 3
            for j in range(0, 9):
                y = j / 3
                string = str(board[i][j]) + 'in id' + str(x) + str(y)
                if board[i][j] == '.':
                    continue
                elif cell.has_key(string):
                    return False
                else:
                    cell[string] = True
        return True



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            num_set = [None for i in range(9)]
            for j in range(9):
                if board[i][j] != '.':
                    if num_set[int(board[i][j]) - 1] != None:
                        print(str(i)+'.'+ str(j)+'line8')
                        return False
                    num_set[int(board[i][j]) - 1] = True
        for i in range(9):
            num_set = [None for i in range(9)]
            for j in range(9):
                if board[j][i] != '.':
                    if num_set[int(board[j][i]) - 1] != None:
                        print(str(i)+'.'+ str(j)+'line16')
                        return False
                    num_set[int(board[j][i]) - 1] = True
        cell = set()
        for i in range(9):
            x = i // 3
            for j in range(9):
                y = j // 3
                if board[i][j] != '.':
                    string = board[i][j] + 'in id: ' + str(x) + str(y)
                    if string in cell:
                        print(string+'line27')
                        return False
                    else:
                        cell.add(string)
        return True
    
if __name__ == '__main__':
    s = Solution8()
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    print(s.isValidSudoku(board))
