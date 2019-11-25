class Solution:
    def nextGreaterElements(self, nums):
        index_stack = []
        new_nums = nums + nums
        next_greater = [-1] * len(new_nums)
        for i in range(len(new_nums)):
            while len(index_stack) > 0 and new_nums[index_stack[-1]] < new_nums[i]:
                index = index_stack.pop()
                next_greater[index] = new_nums[i]
            index_stack.append(i)

        return next_greater[: len(nums)]
nums = [1,2,1]
s = Solution()
print(s.nextGreaterElements(nums))
