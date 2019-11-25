class Solution:
    def splitArray(self, nums, m: int) -> int:
        start = max(nums)
        end = sum(nums)
        while start + 1 < end:
            # size of the bucket
            mid = start + (end - start) // 2
            if self.helper(mid, nums) > m:
                start = mid
            else:
                end = mid
        if self.helper(start, nums) == m:
            return start
        elif self.helper(end, nums) == m:
            return end
        else:
            return start

    # return how many bucket needed
    def helper(self, target, nums):
        res = 0
        i = 0
        sum_up = 0
        while i < len(nums):
            sum_up += nums[i]
            if sum_up > target:
                res += 1
                sum_up = 0
            else:
                i += 1
        if sum_up > 0:
            return res + 1
        return res


s = Solution()
# nums = [7,2,5,10,8]
# m = 2
# print(s.splitArray(nums, m))
#
# nums = [3, 7, 4, 6, 5, 8, 2, 4]
# m = 5
# print(s.splitArray(nums, m))

nums =[2,3,1,1,1,1,1]
m = 5
print(s.splitArray(nums, m))
