
# class Solution(object):
#     def numRollsToTarget(self, d, f, target):
#         A = []
#         for i in range(f):
#             A.append(i + 1)
#
#         n = len(A)
#         dp = [[[0 for _ in range(target+1)] for _ in range(d+1)] for _ in range(n+1)]
#         dp[0][0][0] = 1
#         for i in range(1, n + 1):
#                 for j in range(0, d + 1):
#                         for t in range(0, target + 1):
#                                 dp[i][j][t] = dp[i - 1][j][t]
#                                 if t >= A[i - 1] and j >= 1:
#                                         dp[i][j][t] = dp[i][j][t] + dp[i - 1][j - 1][t - A[i - 1]]
#         return dp[n][d][target]
# s = Solution()
# d = 2
# f = 6
# target = 7 #6
# print(s.numRollsToTarget(d, f, target))


# class MajorityChecker(object):
#
#     def __init__(self, arr):
#         """
#         :type arr: List[int]
#         """
#         self.arr_set = set(arr)
#         self.arr_hash_prefixt = {}
#         arr_hash = {}
#         for ele in self.arr_set:
#             arr_hash[ele] = 0
#         self.init_arr_hash = arr_hash.copy()
#         for i in range(len(arr)):
#             freq = arr_hash[arr[i]]
#             arr_hash[arr[i]] = freq + 1
#             self.arr_hash_prefixt[i] = arr_hash.copy()
#
#     def query(self, left, right, threshold):
#         """
#         :type left: int
#         :type right: int
#         :type threshold: int
#         :rtype: int
#         """
#         if left == 0:
#             first = self.init_arr_hash
#         else:
#             first = self.arr_hash_prefixt[left - 1]
#         second = self.arr_hash_prefixt[right]
#         for ele in self.arr_set:
#             if second[ele] - first[ele] >= threshold:
#                 return ele
#         return -1
# a = [1,1,2,2,1,1]
# s = MajorityChecker(a)
# print(s.query(0,5,4))
# print(s.query(0,3,3))
# print(s.query(2,3,2))


