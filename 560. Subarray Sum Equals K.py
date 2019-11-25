# O(n^2)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count
    def subarraySum1(self, nums, k):
        count = 0
        sum = 0
        hash = {}
        hash[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if hash.has_key(sum - k):
                count += hash[sum - k]
            if hash.has_key(sum):
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count









