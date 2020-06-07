import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.bfs(rooms, visited)
        return len(rooms) == len(visited)

    def bfs(self, rooms, visited):
        q = collections.deque()
        q.append(0)
        visited.add(0)
        while q:
            cur = q.popleft()
            for node in rooms[cur]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(0, rooms, visited)
        return len(rooms) == len(visited)

    def dfs(self, cur, rooms, visited):
        # base
        if cur in visited:
            return
        visited.add(cur)
        # general
        for node in rooms[cur]:
            self.dfs(node, rooms, visited)
s = Solution()
a = [[1],[2],[3],[]]
print((s.canVisitAllRooms(a)))
a = [[1,3],[3,0,1],[2],[0]]
print((s.canVisitAllRooms(a)))

