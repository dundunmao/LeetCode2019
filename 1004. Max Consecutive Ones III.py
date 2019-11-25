class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        j = 0
        pre_sum_zero = 0
        n = len(A)
        res = 0
        while j < n:
            if A[j] == 0:
                if pre_sum_zero == K:
                    res = max(res, j - i)
                    while A[i] != 0 and i < j:
                        i += 1
                    i += 1
                else:
                    pre_sum_zero += 1
            j += 1
        # 最后要考虑【0，0，0，1】 k = 4，这种情况：就是j到头了，0还没到k
        res = max(res, j - i)
        return res
