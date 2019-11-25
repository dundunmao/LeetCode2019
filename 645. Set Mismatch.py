class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:   #标记数组，把存在的index都标成负的
            index = abs(num) - 1   #这里用abs，是因为在变负的过程中，可能没遍历到的，已经被变负了。
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                ans.append(index+1)   #如果是负的，说明yij 标记过， 说明这个是duplicate的那个

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)   #这个为正的是Miss的那个
        return  ans
if __name__ == "__main__":
    x = Solution()
    s = [2,2]
    print(x.findErrorNums(s))
