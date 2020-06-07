class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = 1
        m2 = 1
        for ele in nums:
            if ele > m1:
                m2 = m1
                m1 = ele

            elif ele > m2:
                m2 = ele
        return (m1 - 1) * (m2 - 1)
