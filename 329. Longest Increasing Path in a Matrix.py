class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0

        m = len(matrix[0])
        if m == 0:
            return 0

        all_results = [[None for i in range(m)] for j in range(n)]

        result = 0
        for i in range(0, n):
            for j in range(0, m):
                result = max(result, self.dfs(matrix, i, j, all_results))
        return result

    def dfs(self, a, row, col, all_results):
        if all_results[row][col] != None:
            return all_results[row][col]
        result = 1

        if row - 1 >= 0 and a[row - 1][col] > a[row][col]:
            result = max(result, 1 + self.dfs(a, row - 1, col, all_results))

        if row + 1 < len(a) and a[row + 1][col] > a[row][col]:
            result = max(result, 1 + self.dfs(a, row + 1, col, all_results))

        if col - 1 >= 0 and a[row][col - 1] > a[row][col]:
            result = max(result, 1 + self.dfs(a, row, col - 1, all_results))

        if col + 1 < len(a[0]) and a[row][col + 1] > a[row][col]:
            result = max(result, 1 + self.dfs(a, row, col + 1, all_results))

        all_results[row][col] = result

        return result









