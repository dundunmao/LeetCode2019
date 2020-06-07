class Solution:
    def __init__(self):
        self.res = float('inf')
    def minSwap(self, A: List[int], B: List[int]) -> int:
        self.dfs(A, B, 1, 0)
        return self.res
    def dfs(self, A, B, pos, times):
        if times == self.res:
            return
        if pos == len(A):
            self.res = min(self.res, times)
            return
        if A[pos] > A[pos - 1] and B[pos] > B[pos - 1]:
            self.dfs(A, B, pos + 1, times)
        if A[pos] > B[pos - 1] and B[pos] > A[pos - 1]:
            A[pos], B[pos] = B[pos], A[pos]
            self.dfs(A, B, pos + 1, times + 1)
            A[pos], B[pos] = B[pos], A[pos]

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        keep = [float('inf') for i in range(n)]
        keep[0] = 0
        swap = [float('inf') for i in range(n)]
        swap[0] = 1
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
                # self.dfs(A, B, i + 1, times)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = min(swap[i], keep[i - 1] + 1)
                keep[i] = min(keep[i], swap[i - 1])
        return min(keep[-1], swap[-1])
