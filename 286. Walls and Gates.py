import collections
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])
        queue = collections.deque()
        # visited = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    # visited[i][j] = True
        level = 0
        while len(queue) > 0:
            size = len(queue)
            level += 1
            for i in range(size):
                row, col = queue.popleft()
                if row - 1 >= 0 and rooms[row - 1][col] == 2147483647:
                    rooms[row - 1][col] = level
                    queue.append((row - 1, col))
                if row + 1 < n and rooms[row + 1][col] == 2147483647:
                    rooms[row + 1][col] = level
                    queue.append((row + 1, col))
                if col - 1 >= 0 and rooms[row][col - 1] == 2147483647:
                    rooms[row][col - 1] = level
                    queue.append((row, col - 1))
                if col + 1 < m and rooms[row][col + 1] == 2147483647:
                    rooms[row][col + 1] = level
                    queue.append((row, col + 1))
        return rooms
s = Solution()
a = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(s.wallsAndGates(a))

a = [[0,0,0,0,2147483647,2147483647],[-1,0,-1,2147483647,0,-1],[-1,-1,0,0,2147483647,0],[-1,-1,2147483647,2147483647,2147483647,-1],[2147483647,2147483647,-1,2147483647,-1,2147483647],[2147483647,2147483647,0,-1,-1,0],[0,0,0,2147483647,-1,0],[0,-1,0,-1,0,0],[2147483647,0,-1,-1,2147483647,2147483647],[0,0,-1,-1,-1,2147483647]]
print(s.wallsAndGates(a))
