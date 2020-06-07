class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        res = 0
        for i in range(2, len(A)):
            if A[i - 2] < A[i - 1] > A[i]:
                return i - 1
        return -1
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        s = 0
        e = len(A)
        while s + 1 < e:
            mid = s + (e - s) // 2
            if A[mid - 1] < A[mid]:
                s = mid
            else:
                e = mid
        if A[s] > A[e]:
            return s
        else:
            return e
