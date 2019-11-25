# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


#用hash
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        hash = {}
        for num in nums:
            if hash.has_key(num):
                hash[num] += 1
                if hash[num] > le / 2:
                    return num
            else:
                hash[num] = 1
                if hash[num] > le / 2:
                    return num


class Solution(object):
    def majorityElement(self, A):
        # class Solution(object):
        # def majority(A):
        le = len(A)
        left = self.helper(A)
        if left != [] and A.count(left[0]) > le / 2:
            return left[0]
        else:
            return None

    def helper(self, A):
        le = len(A)
        if le == 2:
            if A[0] != A[1]:
                return []
            else:
                return A
        if le == 1:
            return A
        left = self.helper(A[:le / 2 + 1])
        right = self.helper(A[le / 2 + 1:])
        if len(left) == len(right):
            if left == [] or left[0] != right[0]:
                return []
            else:
                return left + right
        else:
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] != right[j]:
                    del left[i]
                    del right[j]
                else:
                    break
            return left + right

def majorityElement(nums):
    count = 0
    candidate1 = 0
    for num in nums:    #找到挨着的一样的数,这个数出现的次数还大于一半
        if candidate1 == num:
            count +=1
        elif count == 0:
            candidate1 = num
            count +=1
        elif candidate1 != num:
            count-=1
    fre = nums.count(candidate1)
    if fre>len(nums)/2:
        return candidate1
    else:
        return -1
