class Solution:
    def __init__(self):
        self.res = 0
        self.min = float('inf')

    def assignBikes(self, workers, bikes) -> int:
        n = len(workers)
        m = len(bikes)
        matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                matrix[i][j] = dist
        worker_set = set()
        bike_set = set()
        for j in range(m):
            self.dfs(0, j, worker_set, bike_set, matrix)
        return self.min

    def dfs(self, w, b, worker_set, bike_set, matrix):
        # worker_set.add(w)
        bike_set.add(b)
        self.res += matrix[w][b]
        # base case
        if w == len(matrix) - 1:
            self.min = min(self.min, self.res)
        else:

            for j in range(len(matrix[0])):
                if j not in bike_set:
                    self.dfs(w + 1, j, worker_set, bike_set, matrix)
        self.res -= matrix[w][b]
        bike_set.remove(b)




class Solution1:

    def assignBikes(self, workers, bikes) -> int:
        n = len(workers)
        m = len(bikes)
        matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                matrix[i][j] = dist
        dp = [[float('inf') for j in range(1 << m)] for i in range(n + 1)]
        dp[0][0] = 0
        # worker_hash = {}
        # bike_set = set()
        res = float('inf')
        for i in range(1, n + 1):
            for s in range(1, (1 << m)):
                for j in range(m):
                    if (s & (1 << j)) == 0:
                        continue
                    prev = s ^ (1 << j)
                    dp[i][j] = min(dp[i - 1][prev] + matrix[i - 1][j], dp[i][s])
                    if i == n:
                        res = min(res, dp[i][s])
        return res

s = Solution1()
# w = [[0,0],[2,1]]
# b = [[1,2],[3,3]]
# print(s.assignBikes(w,b)) # 6
# workers = [[0,0],[1,1],[2,0]]
# bikes = [[1,0],[2,2],[2,1]]
# print(s.assignBikes(workers,bikes)) # 4
workers = [[815,60],[638,626],[6,44],[103,90],[591,880]]
bikes = [[709,161],[341,339],[755,955],[172,27],[433,489]]
print(s.assignBikes(workers,bikes)) #1458
