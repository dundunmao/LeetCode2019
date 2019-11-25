class Solution:

    def eventualSafeNodes(self, graph):
        res = []
        n = len(graph)

        for i in range(len(graph)):
            visited_passby = [False] * n
            visited_result = [None] * n
            if self.dfs(graph, i, visited_result, visited_passby):
                res.append(i)
        return res

    def dfs(self, graph, i, visited_result, visited_passby):
        if visited_result[i] is True or visited_result[i] is False:
            return visited_result[i]
        if visited_passby[i] is True:
            visited_result[i] = False
            return False
        visited_passby[i] = True

        for child_id in graph[i]:
            if not self.dfs(graph, child_id, visited_result, visited_passby):
                return False
        visited_result[i] = True
        return True



class Solution1:

    def eventualSafeNodes(self, graph):
        res = []
        n = len(graph)
        visited_passby = [False] * n
        visited_result = [None] * n
        for i in range(len(graph)):

            if self.dfs(graph, i, visited_result, visited_passby):
                res.append(i)
        return res

    def dfs(self, graph, i, visited_result, visited_passby):
        if visited_result[i] is True or visited_result[i] is False:
            return visited_result[i]
        if visited_passby[i] is True:
            visited_result[i] = False
            return False
        visited_passby[i] = True

        for child_id in graph[i]:
            if not self.dfs(graph, child_id, visited_result, visited_passby):
                return False
        visited_result[i] = True
        return True



s = Solution1()
# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# print(s.eventualSafeNodes(graph))
graph = [[],[0,2,3,4],[3],[4],[]]
print(s.eventualSafeNodes(graph))

