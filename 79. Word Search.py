

from collections import deque
import copy
# 这里我用了bfs，但是要记得每一个路线都要有自己的hash，我只是initail的时候有几个起点，就创建了几个hash，但如果后面分叉多，hash并不会增加
# 所以这里每次往q里添加新的node时，hash都是用的硬拷贝。
class Solution2(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(board)
        n = len(board[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    q.append([(i, j), 0, {(i, j): True}])
        if len(word) == 1:
            return len(q) != 0
        while q:
            size = len(q)
            for k in range(size):
                cur, pos, hash_cur = q.popleft()
                if pos == len(word) - 1:
                    return False
                for i, j in cor:
                    if cur[0] + i > -1 and cur[0] + i < m and cur[1] + j > -1 and cur[1] + j < n:
                        if pos + 1 == len(word) - 1 and (cur[0] + i, cur[1] + j) not in hash_cur and board[cur[0] + i][cur[1] + j] == word[pos + 1]:
                            return True
                        if (cur[0] + i, cur[1] + j) not in hash_cur and board[cur[0] + i][cur[1] + j] == word[pos + 1]:
                            hash_i = copy.deepcopy(hash_cur)
                            hash_i[(cur[0] + i, cur[1] + j)] = True
                            q.append([(cur[0] + i, cur[1] + j), pos + 1, hash_i ])
        return False

# 下面享用global的visit代替hash，事实证明，不行
from collections import deque
class Solution3(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(board)
        n = len(board[0])
        q = deque()
        visit = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    q.append([(i, j), 0])
        if len(word) == 1:
            return len(q) != 0
        while q:
            size = len(q)
            for k in range(size):
                cur, pos = q.popleft()
                if pos == len(word) - 1:
                    return False
                for i, j in cor:
                    if cur[0] + i > -1 and cur[0] + i < m and cur[1] + j > -1 and cur[1] + j < n:
                        if pos + 1 == len(word) - 1 and visit[cur[0] + i][cur[1] + j] == False and board[cur[0] + i][cur[1] + j] == word[pos + 1]:
                            return True
                        if visit[cur[0] + i][cur[1] + j] == False and board[cur[0] + i][cur[1] + j] == word[pos + 1]:
                            visit[cur[0] + i][cur[1] + j] = True
                            q.append([(cur[0] + i, cur[1] + j), pos + 1 ])
        return False


class Solution5:
    def exist(self, board, word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                if self.dfs(board, i, j, visited, 0, word, direction):
                    return True
                visited[i][j] = False
        return False

    def dfs(self, board, row, col, visited, depth, word, direction):
        if word[depth] != board[row][col]:
            return False
        if depth == len(word) - 1:
            return True
        for ele in direction:
            cur_row = row + ele[0]
            cur_col = col + ele[1]
            if cur_row >= 0 and cur_row < len(board) and cur_col >= 0 and cur_col < len(board[0]) and visited[cur_row][cur_col] is False:
                visited[cur_row][cur_col] = True
                if self.dfs(board, cur_row, cur_col, visited, depth + 1, word, direction):
                    return True
                visited[cur_row][cur_col] = False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                if self.dfs(board, i, j, visited, 0, word, direction):
                    return True
                visited[i][j] = False
        return False

    def dfs(self, board, row, col, visited, depth, word, direction):
        if word[depth] != board[row][col]:
            return False
        if depth == len(word) - 1:
            return True
        for ele in direction:
            cur_row = row + ele[0]
            cur_col = col + ele[1]
            if cur_row >= 0 and cur_row < len(board) and cur_col >= 0 and cur_col < len(board[0]) and visited[cur_row][cur_col] is False:
                visited[cur_row][cur_col] = True
                if self.dfs(board, cur_row, cur_col, visited, depth + 1, word, direction):
                    return True
                visited[cur_row][cur_col] = False

if __name__ == '__main__':
    s = Solution5()
    a = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    b = "AB"  #t
    print(s.exist(a,b))
    b = "ABCCED"  #f
    print(s.exist(a,b))
    b = 'SEE' #t
    print(s.exist(a,b))
    b = 'ABCB'  #f
    print(s.exist(a,b))
