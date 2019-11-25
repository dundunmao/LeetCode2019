class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        j = 0
        for i in range(0, size):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        # fake base case i=-1
        le = 0
        # general case i = [0, size)
        for i in range(0, size):
            if nums[i] != val:
                nums[le] = nums[i]
                le += 1
        return le

