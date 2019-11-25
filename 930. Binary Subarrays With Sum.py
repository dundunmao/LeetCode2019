class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        num_to_freq_hash = {}
        # base case
        num_to_freq_hash[0] = 1
        n = len(nums)
        pre_sum = 0
        res = 0
        for i in range(n):
            pre_sum += nums[i]
            if pre_sum - k in num_to_freq_hash:
                res += num_to_freq_hash[pre_sum - k]
            if pre_sum not in num_to_freq_hash:
                num_to_freq_hash[pre_sum] = 1
            else:
                num_to_freq_hash[pre_sum] += 1
        return res
