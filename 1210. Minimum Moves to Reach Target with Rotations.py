import collections
class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        head = (0, 0)
        tail = (0, 1)
        snake = Snake(head, tail)
        visited = set()
        n = len(grid)
        return self.bfs(snake, visited, grid, n)

    def bfs(self, snake, visited, grid, n):
        visited.add(snake)
        q = collections.deque()
        q.append(snake)
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.head[0] == n - 1 and cur.head[1] == n - 2 and cur.tail[0] == n - 1 and cur.tail[1] == n - 1 and \
                        grid[n - 1][n - 2] == 0 and grid[n - 1][n - 1] == 0:
                    return step
                # 横着的蛇
                if cur.head[0] == cur.tail[0]:
                    # 横着走
                    if cur.tail[1] + 1 < n and grid[cur.tail[0]][cur.tail[1] + 1] == 0:
                        new = Snake((cur.head[0], cur.head[1] + 1), (cur.tail[0], cur.tail[1] + 1))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
                    # 竖着走
                    if cur.tail[0] + 1 < n and grid[cur.head[0] + 1][cur.head[1]] == 0 and grid[cur.tail[0] + 1][
                        cur.tail[1]] == 0:
                        new = Snake((cur.head[0] + 1, cur.head[1]), (cur.tail[0] + 1, cur.tail[1]))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
                    # 转着走
                    if cur.head[0] + 1 < n and grid[cur.head[0] + 1][cur.head[1]] == 0 and grid[cur.tail[0] + 1][cur.tail[1]] == 0:
                        new = Snake((cur.head[0], cur.head[1]), (cur.head[0] + 1, cur.head[1]))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
                # 竖着的蛇
                elif cur.head[1] == cur.tail[1]:
                    # 横着走
                    if cur.tail[1] + 1 < n and grid[cur.head[0]][cur.head[1] + 1] == 0 and grid[cur.tail[0]][cur.tail[1] + 1] == 0:
                        new = Snake((cur.head[0], cur.head[1] + 1), (cur.tail[0], cur.tail[1] + 1))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
                    # 竖着走
                    if cur.tail[0] + 1 < n and grid[cur.tail[0] + 1][cur.tail[1]] == 0:
                        new = Snake((cur.head[0] + 1, cur.head[1]), (cur.tail[0] + 1, cur.tail[1]))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
                    # 转着走
                    if cur.head[1] + 1 < n and grid[cur.head[0]][cur.head[1] + 1] == 0 and grid[cur.tail[0]][cur.tail[1] + 1] == 0:
                        new = Snake((cur.head[0], cur.head[1]), (cur.head[0], cur.head[1] + 1))
                        if new not in visited:
                            q.append(new)
                            visited.add(new)
            step += 1
        return -1


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __hash__(self):
        return hash((self.head, self.tail))

    def __eq__(self, other):
        return (self.head, self.tail) == (other.head, other.tail)
s = Solution()
a = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,1,1,0,0,1,0,0,0,0,1,0,0],
     [0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,1,0,0,1,0,0,0,1,0,0],
     [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
     [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0]]
print(s.minimumMoves(a))
a = [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]
print(s.minimumMoves(a))

