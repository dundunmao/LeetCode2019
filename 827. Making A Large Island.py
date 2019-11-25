import collections
class Solution:
    def largestIsland(self, a) -> int:
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        if m == 0:
            return 0
        colors = [[0 for i in range(m)] for j in range(n)]
        visited = [[False for i in range(m)] for j in range(n)]
        color_id_to_area = []
        color_id_to_area.append(-1) # 占index为0的位置，让记录从index=1开始
        result = 0
        color_id = 1
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1 and not visited[i][j]:
                    # 染色 + 算color_id代表多少面积

                    # area = self.bfs(a, i, j, visited, colors, color_id)
                    area = self.dfs(a, i, j, colors, color_id)
                    color_id += 1
                    color_id_to_area.append(area)
                    result = max(result, area)

        for row in range(n):
            for col in range(m):
                if a[row][col] == 0:
                    neighbor_ids = set()
                    if row - 1 >= 0 and a[row - 1][col] == 1:
                        neighbor_ids.add(colors[row - 1][col])

                    if row + 1 < len(a) and a[row + 1][col] == 1:
                        neighbor_ids.add(colors[row + 1][col])

                    if col - 1 >= 0 and a[row][col - 1] == 1:
                        neighbor_ids.add(colors[row][col - 1])

                    if col + 1 < len(a) and a[row][col + 1] == 1:
                        neighbor_ids.add(colors[row][col + 1])

                    sum_up = 1
                    for neighbor_id in neighbor_ids:
                        sum_up += color_id_to_area[neighbor_id]
                    result = max(sum_up, result)
        return result

    def bfs(self, a, start_row, start_col, visited, colors, color_id):
        queue = collections.deque()
        queue.append((start_row, start_col))
        visited[start_row][start_col] = True
        result = 0
        while len(queue) > 0:
            row, col = queue.popleft()

            colors[row][col] = color_id
            result += 1

            # general case
            if row - 1 >= 0 and a[row - 1][col] == 1 and visited[row - 1][col] is False:
                queue.append((row - 1, col))
                visited[row - 1][col] = True

            if row + 1 < len(a) and a[row + 1][col] == 1 and visited[row + 1][col] is False:
                queue.append((row + 1, col))
                visited[row + 1][col] = True

            if col - 1 >= 0 and a[row][col - 1] == 1 and visited[row][col - 1] is False:
                queue.append((row, col - 1))
                visited[row][col - 1] = True

            if col + 1 < len(a) and a[row][col + 1] == 1 and visited[row][col + 1] is False:
                queue.append((row, col + 1))
                visited[row][col + 1] = True

        return result

    def dfs(self, a, row, col, colors, color_id):
        if colors[row][col] != 0:
            return 0
        colors[row][col] = color_id
        result = 1
        # general case
        if row - 1 >= 0 and a[row - 1][col] == 1:
            result += self.dfs(a, row - 1, col, colors, color_id)

        if row + 1 < len(a) and a[row + 1][col] == 1:
            result += self.dfs(a, row + 1, col, colors, color_id)

        if col - 1 >= 0 and a[row][col - 1] == 1:
            result += self.dfs(a, row, col - 1, colors, color_id)

        if col + 1 < len(a) and a[row][col + 1] == 1:
            result += self.dfs(a, row, col + 1, colors, color_id)

        return result

s = Solution()
a = [[1, 0], [0, 1]]
print(s.largestIsland(a))
a = [[1, 1], [1, 0]]
print(s.largestIsland(a))
a = [[1, 1], [1, 1]]
print(s.largestIsland(a))
