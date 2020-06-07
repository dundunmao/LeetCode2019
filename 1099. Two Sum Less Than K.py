class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        n = len(A)
        i = 0
        j = n - 1
        res = float('-inf')
        while i < j:
            if A[i] + A[j] < K:
                res = max(res, A[i] + A[j])
                i += 1

            else:
                j -= 1
        return -1 if res == float('-inf') else res
