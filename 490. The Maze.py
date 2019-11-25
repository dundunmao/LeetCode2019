import collections
class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(maze)
        m = len(maze[0])
        visited = [[False for i in range(m)] for j in range(n)]
        q = collections.deque()
        q.append([start[0], start[1]])
        visited[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in direction:
                new_x = x
                new_y = y
                # 一路走到不能再走
                while 0 <= new_x + dx < n and 0 <= new_y + dy < m and maze[new_x + dx][new_y + dy] == 0:
                    new_x = new_x+ dx
                    new_y = new_y + dy
                # 如果这个node没加过，就加进queue里
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    q.append([new_x, new_y])
        return False
s = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(s.hasPath(maze,start,destination))



maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(s.hasPath(maze,start,destination))





