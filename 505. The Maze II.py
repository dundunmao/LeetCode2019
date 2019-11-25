import collections
class Solution:
    def shortestDistance(self, maze, start, destination) -> int:
        q = collections.deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q.append([start[0], start[1], 0])
        visited = {}
        visited[(start[0], start[1])] = 0
        while q:
            cur = q.popleft()
            for direction in directions:
                temp = [cur[0], cur[1]]
                step = 0
                while self.valid(maze, temp, direction):
                    temp[0] += direction[0]
                    temp[1] += direction[1]
                    step += 1
                if (temp[0], temp[1]) not in visited or visited[(temp[0], temp[1])] > cur[2] + step:
                    q.append([temp[0], temp[1], cur[2] + step])
                    visited[(temp[0], temp[1])] = cur[2] + step
        if (destination[0], destination[1]) not in visited:
            return -1
        return visited[(destination[0], destination[1])]

    def valid(self, maze, cur, direction):
        if not 0 <= cur[0] + direction[0] < len(maze):
            return False
        if not 0 <= cur[1] + direction[1] < len(maze[0]):
            return False
        if maze[cur[0] + direction[0]][cur[1] + direction[1]] == 1:
            return False
        return True

s = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(s.shortestDistance(maze,start,destination)) #12



maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(s.shortestDistance(maze,start,destination)) #-1

maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print(s.shortestDistance(maze,start,destination))  #-1

maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
start = [0,0]
destination =[8,6]
print(s.shortestDistance(maze,start,destination))# 26
