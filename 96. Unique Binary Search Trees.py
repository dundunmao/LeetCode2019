class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        nums = [0 for i in range(n+1)]
        nums[0] = 1
        nums[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                nums[i] += nums[i-j-1]*nums[j]
        return nums[n]