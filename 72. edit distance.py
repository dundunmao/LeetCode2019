
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        f = [[float('inf') for i in range(m + 1)] for j in range(n + 1)]
        f[0][0] = 0

        for i in range(1, m + 1):
            f[0][i] = i

        for i in range(1, n + 1):
            f[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])

        return f[n][m]

# dp 滚动数组
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        f = [[float('inf') for i in range(m + 1)] for j in range(2)]
        f[0][0] = 0

        for i in range(1, m + 1):
            f[0][i] = i

        for i in range(1, n + 1):
            for j in range(0, m + 1):
                if j == 0:
                    f[i % 2][j] = i
                    continue
                if word1[i - 1] == word2[j - 1]:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1]
                else:
                    f[i % 2][j] = 1 + min(f[(i - 1) % 2][j], f[i % 2][j - 1], f[(i - 1) % 2][j - 1])

        return f[n % 2][m]


###################################
import collections
# bfs
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        queue = collections.deque()
        cur = Node(0, 0)
        queue.append(cur)
        visited = set()
        visited.add(cur)
        level = 0

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                visited.add(node)
                while node.i < n and node.j < m and word1[node.i] == word2[node.j]:
                    node.i += 1
                    node.j += 1
                if node.i == n and node.j == m:
                    return level
                if node.i < n:
                    temp = Node(node.i + 1, node.j)
                    if temp not in visited:
                        queue.append(temp)
                        visited.add(temp)

                if node.j < m:
                    temp = Node(node.i, node.j + 1)
                    if temp not in visited:
                        queue.append(temp)
                        visited.add(temp)

                if node.i < n and node.j < m:
                    temp = Node(node.i + 1, node.j + 1)
                    if temp not in visited:
                        queue.append(temp)
                        visited.add(temp)
            level += 1
        return level


class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __hash__(self):
        return hash((self.i, self.j))

    def __eq__(self, other):
        return ((self.i, self.j) == (other.i, other.j))


# dfs
class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        hash = [[None for i in range(m + 1)] for j in range(n + 1)]
        return self.dfs(word1, word2, n, m, n, m, hash)

    def dfs(self, word1, word2, i, j, n, m, hash):
        # base case
        if hash[i][j] is not None:
            return hash[i][j]
        if i == 0 and j == 0:
            return 0
        if i == 0:
            return j
        if j == 0:
            return i

        # general case
        if word1[i - 1] == word2[j - 1]:
            res = self.dfs(word1, word2, i - 1, j - 1, n, m, hash)
        else:
            res = 1 + min(self.dfs(word1, word2, i - 1, j - 1, n, m, hash),
                          self.dfs(word1, word2, i - 1, j, n, m, hash), self.dfs(word1, word2, i, j - 1, n, m, hash))
        hash[i][j] = res
        return res

s = Solution3()
# w1 = "horse"
# w2 = "ros"
# print(s.minDistance(w1, w2))
# w1 = "intention"
# w2 = "execution"
# print(s.minDistance(w1, w2))
# w1 = "b"
# w2 = ""
# print(s.minDistance(w1, w2))
w1 = "dinitrophenylhydrazine"
w2 = "benzalphenylhydrazone"
print(s.minDistance(w1, w2))
