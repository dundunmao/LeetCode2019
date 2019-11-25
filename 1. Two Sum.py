# hash
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) <= 1:
            return None
        hash = {nums[0]: 0}
        for i in range(1, len(nums)):
            if hash.has_key(target - nums[i]):
                return [hash[target - nums[i]], i]
            else:
                hash[nums[i]] = i
        return None