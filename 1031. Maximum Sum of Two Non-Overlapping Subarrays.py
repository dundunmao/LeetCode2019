from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix = [A[0]]
        for i in range(1, len(A)):
            prefix.append(prefix[i - 1] + A[i])

        res = prefix[L + M - 1]
        Lmax = prefix[L - 1]
        Mmax = prefix[M - 1]
        for i in range(L + M, len(prefix)):
            Lmax = max(Lmax, prefix[i - M] - prefix[i - L - M])
            Mmax = max(Mmax, prefix[i - L] - prefix[i - L - M])
            res = max(res, Lmax + prefix[i] - prefix[i - M], Mmax + prefix[i] - prefix[i - L])
        return res


s = Solution()
A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2
print(s.maxSumTwoNoOverlap(A, L, M))

A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
print(s.maxSumTwoNoOverlap(A, L, M))
