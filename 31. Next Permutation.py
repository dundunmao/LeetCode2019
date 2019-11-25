
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >=0 and nums[i + 1] <= nums[i]:
            i -=1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j]<= nums[i]:
                j -=1
            nums[i],nums[j] = nums[j],nums[i]
        self.reverse_part(nums, i+1, len(nums)-1)

    def reverse_part(self,nums,i,j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
