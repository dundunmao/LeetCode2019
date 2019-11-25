class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        count = 0
        i = 0
        for i in range(len(A) - K + 1):
            if A[i] == 0:
                self.flip(A, i, K)
                count += 1
        for j in range(i, len(A)):
            if A[i] == 0:
                return 0
        return count

    def flip(self, A, start, K):
        for i in range(start, start + K):
            A[i] = 1 if A[i] == 0 else 0

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        curr = 0 # To save total number of flips so far
        for i in range(n):
            if i >= K:
                prev_count = curr - A[i-K]  # index i is affected by only by flips [i-K+1 to i-1]
            else:
                prev_count = curr
            if ((prev_count % 2 == 0 and A[i] == 0) or (prev_count % 2 == 1 and A[i] == 1)): # 需要flip
                if i > n-K: # if there is a flip required in last k-1 indices return -1
                    return -1
                curr = curr + 1
            A[i] = curr # save total number of flips until i at A[i]
        return curr
