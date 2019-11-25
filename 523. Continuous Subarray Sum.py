class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_to_index_hash = {}
        pre_sum = 0
        mod_to_index_hash[0] = -1
        for i in range(len(nums)):
            pre_sum += nums[i]
            if k != 0:
                pre_sum = pre_sum % k
            if pre_sum in mod_to_index_hash:
                if i - mod_to_index_hash[pre_sum] > 1:
                    return True
            else:
                mod_to_index_hash[pre_sum] = i
        return False

