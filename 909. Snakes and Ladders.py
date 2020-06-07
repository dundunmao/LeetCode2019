from typing import List

import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if n == 0:
            return 0
        m = len(board[0])
        if m == 0:
            return 0
        visited = [None for i in range(n * n + 1)]
        mini = n * n
        q = collections.deque()
        q.append(1)
        moves = 0
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == n * n:
                    mini = min(mini, moves)
                for j in range(1, 7):
                    num = cur + j
                    if num > n * n:
                        break
                    if num == cur:
                        continue
                    row = n - (num - 1) // n - 1
                    if (n - row) % 2 != 0:
                        col = (num - 1) % n
                    else:
                        col = n - (num - 1) % n - 1
                    if visited[num] is None:
                        visited[num] = True
                        if board[row][col] == -1:
                            q.append(num)
                        else:
                            q.append(board[row][col])
            moves += 1
        return -1 if mini == n * n else mini
