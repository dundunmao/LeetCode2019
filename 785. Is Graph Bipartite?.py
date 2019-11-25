class Solution:
    def isBipartite(self, graph) -> bool:
        size = len(graph)
        colors = [0] * size
        for i in range(size):
            if colors[i] == 0:
                if not self.dfs(graph, colors, 1, i):
                    return False
        return True
    # 当前node该图color这个颜色，基于这个往下遍历，是否是bipartite的
    def dfs(self, graph, colors, color, node):
        if colors[node] != 0:
            return colors[node] == color
        else:
            colors[node] = color
            for child in graph[node]:
                if not self.dfs(graph, colors, -color, child):
                    return False
        return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0:
                q = collections.deque()
                q.append(i)
                color = 1
                while q:
                    size = len(q)
                    for i in range(size):
                        cur = q.popleft()
                        if colors[cur] == 0:
                            colors[cur] = color
                            for ele in graph[cur]:
                                q.append(ele)
                        else:
                            if colors[cur] != color:
                                return False

                    color = -color
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0:
                if not self.bfs(i, colors, graph):
                    return False
        return True

    def bfs(self, node, colors, graph):
        q = collections.deque()
        q.append(node)
        color = 1
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if colors[cur] == 0:
                    colors[cur] = color
                    for ele in graph[cur]:
                        q.append(ele)
                else:
                    if colors[cur] != color:
                        return False

            color = -color
        return True



s = Solution1()

a = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(s.isBipartite(a))

