class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum_to_count = {}
        presum_to_count[0] = 1
        presum = 0
        res = 0
        for i in range(len(A)):
            presum += A[i]
            if K != 0:
                presum = presum % K
            if presum in presum_to_count:
                res += presum_to_count[presum]
                presum_to_count[presum] += 1
            else:
                presum_to_count[presum] = 1
        return res
