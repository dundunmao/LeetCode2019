class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        res = []
        while i < len(nums):
            temp = []
            temp.append(nums[i])
            j = i + 1
            while j < len(nums) and nums[i] + 1 == nums[j]:
                i += 1
                j += 1
            temp.append(nums[i])
            res.append(temp)
            i = j
        ans = []
        for ele in res:
            if ele[0] == ele[1]:
                ans.append(str(ele[0]))
            else:
                ans.append(str(ele[0]) + '->' + str(ele[1]))

        return ans
#######
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        start = 0
        res = []

        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                cur = self.group(start, i - 1, nums)
                res.append(cur)
                start = i

        cur = self.group(start, -1, nums)
        res.append(cur)
        return res

    def group(self, start, end, nums):
        if nums[end] == nums[start]:
            cur = str(nums[start])
        else:
            cur = str(nums[start]) + '->' + str(nums[end])
        return cur
