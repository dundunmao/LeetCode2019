class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        res = collections.deque()
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                res.appendleft(A[i] * A[i])
                i += 1
            else:
                res.appendleft(A[j] * A[j])
                j -= 1
        return res
