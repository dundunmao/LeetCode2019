# 给一个array找其中最大最小值相差正好为1的Subsequence
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 方法一，放入hash里，然后双循环查每一个对应其他的差是不是1


class Solution_leet(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for ele in nums:
            if dic.has_key(ele):
                dic[ele] += 1
            else:
                dic[ele] = 1
        for k in dic:
            if k + 1 in dic:
                ans = max(ans, dic[k] + dic[k + 1])
        return ans


