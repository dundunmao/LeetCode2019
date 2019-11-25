class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        all_result = []
        self.dfs(graph, 0, path, all_result)
        return all_result
    def dfs(self, graph, id, path, all_result):
        path.append(id)
        if id == len(graph) - 1:
            all_result.append(path[:])
        else:
            for child_id in graph[id]:
                self.dfs(graph, child_id, path, all_result)
        path.pop()
