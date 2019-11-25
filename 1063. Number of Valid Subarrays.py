class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            j = i
            while j < len(nums) and nums[j] >= nums[i]:
                j += 1
            res += (j - i)
        return res

# stack 法

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        res = 0
        index_stack = []
        index_stack.append(0)

        for i in range(1, len(nums)):
            # 没进去一个数，要把他之前比他大的都踢出去，并且更新res
            while len(index_stack) > 0 and nums[i] < nums[index_stack[-1]]:
                index = index_stack.pop()
                res += i - index
            index_stack.append(i)
        # 最后剩下的是没有找到比他小的，那他的结果就是 从他开始的全部，也就是n-index
        for ele in index_stack:
            res += len(nums) - ele
        return res
