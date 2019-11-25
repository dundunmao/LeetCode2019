class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        end = 0
        start = 0
        while start < n:
            if end + 1 < n and A[end] < A[end + 1]:
                while end + 1 < n and A[end] < A[end + 1]:
                    end += 1
                if end + 1 < n and A[end] > A[end + 1]:
                    while end + 1 < n and A[end] > A[end + 1]:
                        end += 1
                    res = max(res, end - start + 1)
            else:
                end += 1
            start = end
        return res
x = Solution()
a = [2,1,4,7,3,2,5]
print(x.longestMountain(a))
