from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        pre_sum = [[0 for i in range(m)] for j in range(n + 1)]
        for j in range(m):
            for i in range(n):
                pre_sum[i + 1][j] = pre_sum[i][j] + matrix[i][j]
        res = 0
        hash_sum = {}
        for row_start in range(n):
            for row_end in range(row_start, n):
                hash_sum.clear()
                sum_up = 0
                for col in range(m):
                    sum_up += pre_sum[row_end + 1][col] - pre_sum[row_start][col]
                    if sum_up == target:
                        res += 1
                    offset = sum_up - target
                    if offset in hash_sum:
                        res += hash_sum[offset]
                    if sum_up in hash_sum:
                        hash_sum[sum_up] += 1
                    else:
                        hash_sum[sum_up] = 1
        return res
