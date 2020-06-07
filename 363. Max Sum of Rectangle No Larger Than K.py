import bisect
class Solution:
    def maxSumSubmatrix(self, matrix, K: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = float('-inf')
        if n > m:
            new_matrix = [[0 for i in range(n)] for j in range(m)]
            for i in range(n):
                for j in range(m):
                    new_matrix[j][i] = matrix[i][j]
            return self.maxSumSubmatrix(new_matrix, K)

        for i in range(n):
            temp = [0 for i in range(m)]
            for j in range(i, n):
                for k in range(m):
                    temp[k] = temp[k] + matrix[j][k]
                res = max(res, self.helper(temp, K))
        return res

    def helper(self, nums, K):
        n = len(nums)
        presum = 0
        res = float('-inf')
        biset = []
        bisect.insort(biset, 0)
        for j in range(n):
            presum += nums[j]
            pos = bisect.bisect_left(biset, presum - K)
            if pos != len(biset):
                res = max(res, presum - biset[pos])
            bisect.insort(biset, presum)
        return res


class Solution1:
    def maxSumSubmatrix(self, matrix, K: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = float('-inf')

        if n > m:
            new_matrix = [[0 for i in range(n)] for j in range(m)]
            for i in range(n):
                for j in range(m):
                    new_matrix[j][i] = matrix[i][j]
            return self.maxSumSubmatrix(new_matrix, K)
        prefix_matrix = [[0 for i in range(m)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m):
                prefix_matrix[i][j] = prefix_matrix[i - 1][j] + matrix[i - 1][j]

        for i in range(0, n):
            temp = [0 for i in range(m)]
            for j in range(i + 1, n + 1):
                for k in range(m):
                    temp[k] = prefix_matrix[j][k] - prefix_matrix[i][k]
                res = max(res, self.helper(temp, K))
        return res

    def helper(self, nums, K):
        n = len(nums)
        presum = 0
        res = float('-inf')
        biset = []
        bisect.insort(biset, 0)
        for j in range(n):
            presum += nums[j]
            pos = bisect.bisect_left(biset, presum - K)
            if pos != len(biset):
                res = max(res, presum - biset[pos])
            bisect.insort(biset, presum)
        return res

s = Solution1()
a = [[2,2,-1]]
k = 0
print(s.maxSumSubmatrix(a,k))
