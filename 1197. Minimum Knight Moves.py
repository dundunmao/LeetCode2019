import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(-2, 1), (2, 1), (-1, 2), (1, 2), (-2, -1), (2, -1), (-1, -2), (1, -2)]
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        x = abs(x)
        y = abs(y)
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == (x, y):
                    return step
                for dir in directions:
                    new_x = cur[0] + dir[0]
                    new_y = cur[1] + dir[1]
                    if new_x > -2 and new_y > -2 and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))
            step += 1
