# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res



class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
        n = len(A)
        result = 1
        length = 1
        # from left to right
        for i in range(1,n):
            if A[i] > A[i-1]:
                length+=1
            else:
                length =1
            result = max(result, length)
        # from right to left
        length = 1
        for i in range(n-2, -1,-1):
            if A[i]>A[i+1]:
                length +=1
            else:
                length = 1
            result = max(result, length)
        return result
