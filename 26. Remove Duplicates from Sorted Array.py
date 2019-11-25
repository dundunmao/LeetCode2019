
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[cur - 1] != nums[i]:
                nums[cur] = nums[i]
                cur += 1
        return cur

class Solution1:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        if len(A) == 1:
            return 1
        count = 0
        i = 0
        while i < len(A):
            if A[i] == A[i-1]:
                i+=1
            else:
                A[count] = A[i]
                count += 1
                i+=1
        return count


# i是遍历找非dup，j是需要被换的地方
    def removeDuplicates_leet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # normal case
        i = 1
        j = 1
        flag = nums[0]
        while i < len(nums): #i去遍历每个数，j停在重复的位置等i给他找不重复的数
            if nums[i] == flag:
                i += 1  #如果遍历到dup,就继续往后找，直到找到非dup
            else:       #遇到非dup了，j的位置和flag都有换成这个非dup。同时i，j往后走。
                nums[j] = nums[i]
                flag = nums[i]
                i += 1
                j += 1
        return j


if __name__ == "__main__":
    a = [1,2,2,2,2,4,4]
    # a = [1,1]
    # dict = ["a"]
    x = Solution()
    print x.removeDuplicates(a)
