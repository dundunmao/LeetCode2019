class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_stack = []
        next_greater = [-1] * len(nums2)
        for i in range(len(nums2)):
            while len(index_stack) >0 and nums2[index_stack[-1]] < nums2[i]:
                index = index_stack.pop()
                next_greater[index] = nums2[i]
            index_stack.append(i)
        res = []
        for ele in nums1:
            index_in_nums2 = nums2.index(ele)
            res.append(next_greater[index_in_nums2])
        return res
