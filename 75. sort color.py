
class Solution3(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        i = 0
        j = len(nums)-1
        point = self.partition(nums, i,j,2)
        i = 0
        j = point
        x = self.partition(nums, i,j,1)
        return nums
    def partition(self, nums,i,j, k):
        while i < j:
            while i < j and nums[i] < k:
                i += 1
            while i < j and nums[j] >= k:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return i
#方法2：跟625题一样，注意i与left互换后，两人一起往后走，i与right互换后，只有right往前走，i并不往后走
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l], nums[i]
                l += 1
                i += 1  # 注意这里走下一步了，而elif里面没有往下走
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1



if __name__ == "__main__":

    A = [1,2,0,0,2,2,1,1,0,2,1]
    B = [1,1]
    s = Solution()

    print s.sortColors(A)
