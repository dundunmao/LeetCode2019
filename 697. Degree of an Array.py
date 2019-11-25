class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        max_value = 1 # 找最大的frequency
        for i in range(len(nums)):
            if nums[i] in hash_map:
                value, first, last = hash_map[nums[i]]
                value += 1
                last = i
                hash_map[nums[i]] = [value, first, last]
                max_value = max(max_value, value)
            else:
                hash_map[nums[i]] = [1, i, i]
        high_frequency = [ele[2] - ele[1] + 1 for ele in hash_map.values() if ele[0] == max_value]

        return min(high_frequency)
