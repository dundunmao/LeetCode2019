class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # base case
        product = nums[0]
        if product >= k:
            return 0
        start = 0
        res = 1
        # general case
        for i in range(1, len(nums)):
            # add me
            product *= nums[i]
            # kick from start
            while product >= k:
                product = product // nums[start]
                start += 1
            res += i - start + 1
        return res
