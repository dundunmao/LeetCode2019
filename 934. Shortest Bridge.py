import collections

class Solution:
    def shortestBridge(self, a) -> int:
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        if m == 0:
            return 0
        visited = [[False for i in range(m)] for j in range(n)]
        flag = False
        for i in range(n):
            if flag is True:
                break
            for j in range(m):
                if a[i][j] == 1 and not visited[i][j]:
                    # 染色，只要把其中一块都变成2就行
                    self.dfs_color(a, i, j, visited)
                    flag = True
                    break

        return self.bfs(a)


    def dfs_color(self, a, row, col, visited):
        a[row][col] = 2
        visited[row][col] = True
        # general case
        if row - 1 >= 0 and not visited[row - 1][col] and a[row - 1][col] == 1:
            self.dfs_color(a, row - 1, col, visited)

        if row + 1 < len(a) and not visited[row + 1][col] and a[row + 1][col] == 1:
            self.dfs_color(a, row + 1, col, visited)

        if col - 1 >= 0 and not visited[row][col - 1] and a[row][col - 1] == 1:
            self.dfs_color(a, row, col - 1, visited)

        if col + 1 < len(a) and not visited[row][col + 1] and a[row][col + 1] == 1:
            self.dfs_color(a, row, col + 1, visited)
    # 把所有的1都放进queue里，一起遍历，找到2就return
    def bfs(self, a):
        n = len(a)
        m = len(a[0])
        queue = collections.deque()
        visited_zero = [[False for i in range(m)] for j in range(n)]
        res = -1
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    queue.append((i, j))
                    visited_zero[i][j] = True
        while len(queue) > 0:
            size = len(queue)
            res += 1
            for i in range(size):
                cur_row, cur_col = queue.popleft()
                if cur_row - 1 >= 0 and a[cur_row - 1][cur_col] == 2:
                    return res
                if cur_row - 1 >= 0 and a[cur_row - 1][cur_col] == 0 and visited_zero[cur_row - 1][cur_col] is False:
                    queue.append((cur_row - 1, cur_col))
                    visited_zero[cur_row - 1][cur_col] = True
                if cur_row + 1 < len(a) and a[cur_row + 1][cur_col] == 2:
                    return res
                if cur_row + 1 < len(a) and a[cur_row + 1][cur_col] == 0 and visited_zero[cur_row + 1][cur_col] is False:
                    queue.append((cur_row + 1, cur_col))
                    visited_zero[cur_row + 1][cur_col] = True
                if cur_col - 1 >= 0 and a[cur_row][cur_col - 1] == 2:
                    return res
                if cur_col - 1 >= 0 and a[cur_row][cur_col - 1] == 0 and visited_zero[cur_row][cur_col - 1] is False:
                    queue.append((cur_row, cur_col - 1))
                    visited_zero[cur_row ][cur_col - 1] = True
                if cur_col + 1 < len(a) and a[cur_row][cur_col + 1] == 2:
                    return res
                if cur_col + 1 < len(a) and a[cur_row][cur_col + 1] == 0 and visited_zero[cur_row][cur_col + 1] is False:
                    queue.append((cur_row, cur_col + 1))
                    visited_zero[cur_row][cur_col + 1] = True
        return res

s = Solution()
a = [[0,0,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1,0]]
print(s.shortestBridge(a)) #5

a = [[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.shortestBridge(a)) #3

a = [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
print(s.shortestBridge(a))#1

a = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(s.shortestBridge(a))#1
a = [[0,1,0],[0,0,0],[0,0,1]]
print(s.shortestBridge(a))#2
a = [[0,1],[1,0]]
print(s.shortestBridge(a))#1
