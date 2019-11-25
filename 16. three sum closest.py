
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # edge case
        if len(nums) < 3:
            return sum(nums)
#         main part
        res = 0
        diff = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum_three = nums[i] + nums[j] + nums[k]
                if sum_three == target:
                    return sum_three
                if abs(sum_three - target) < diff:
                    res = sum_three
                    diff = abs(sum_three - target)
                if sum_three < target:
                    j += 1
                else:
                    k -= 1
        return res

#########
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        diff = float('inf')
        res = float('inf')
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_three = nums[i] + nums[j] + nums[k]
                if sum_three == target:
                    return sum_three
                if abs(sum_three - target) < diff:
                    res = sum_three
                    diff = abs(sum_three - target)
                if sum_three < target:
                    j += 1
                else:
                    k -= 1
        return res
