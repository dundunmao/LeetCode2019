# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
# 这要考虑有0的情况，有一个0和多个0还不一样，
#     还有考虑有-的情况

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res

class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = float('inf')
        for i in nums:
            if nums[i] == 0:
                if index == float('inf'):
                    index = 0
                else:
                    return [0]*len(nums)
        if index != float('inf'):
            mult = 1
            for i in range(len(nums)):
                if i != index:
                    mult *= nums[i]
            for i in range(len(nums)):
                if i != index:
                    nums[i] = 0
                else:
                    nums[i] = mult
            return nums
        else:
            mult = 1
            for ele in nums:
                mult = mult*ele
            for i in range(len(nums)):
                nums[i] = mult/nums[i]
            return nums

class Solution2:
    def productExceptSelf(self, nums):
        pre_product_from_left = [1] * len(nums)
        pre_product_from_right = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                pre_product_from_left[i] = nums[i]
            else:
                pre_product_from_left[i] = pre_product_from_left[i - 1] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                pre_product_from_right[i] = nums[i]
            else:
                pre_product_from_right[i] = pre_product_from_right[i + 1] * nums[i]

        res = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = pre_product_from_right[i + 1]
            elif i == len(nums) - 1:
                res[i] = pre_product_from_left[i - 1]
            else:
                res[i] = (pre_product_from_left[i - 1] * pre_product_from_right[i + 1])
        return res

class Solution4:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_product = [0] * n
        # base case
        left_product[0] = 1
         # general case
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = [1] * n
        # base case
        right_product[n - 1] = 1
         # general case
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # result
        result = [1] * n
        for i in range(0, n):
            result[i] = left_product[i] * right_product[i]
        return result
s = Solution4()
print(s.productExceptSelf([1,2,3,4]))
