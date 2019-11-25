class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            return False
        C = [[0 for j in range(l)] for i in range(m)]
         
        for i in range(m):
            for j in range(l):
                for k in range(n):
                    if A[i][k] != 0 and B[k][j] != 0:
                            C[i][j] += A[i][k] * B[k][j]
        return C




class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        hash_a = {}
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    if i in hash_a:
                        hash_a[i][k] = A[i][k]
                    else:
                        hash_a[i] = {k: A[i][k]}
        hash_b = {}
        for k in range(len(B)):
            for j in range(len(B[0])):
                if B[k][j] != 0:
                    if j in hash_b:
                        hash_b[j][k] = B[k][j]
                    else:
                        hash_b[j] = {k: B[k][j]}

        res = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                temp = 0
                for k in range(len(B)):
                    if i in hash_a and j in hash_b and k in hash_a[i] and k in hash_b[j]:
                        temp += hash_a[i][k] * hash_b[j][k]
                res[i][j] = temp

        return res
