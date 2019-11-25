# 方法一：recursive
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        path = []
        nums.sort()
        self.helper(nums, res, path)
        return res
    def helper(self, nums, res, path):
        for i in range(len(nums)):
            path.append(nums[i])
            if path not in res:
                res.append(path[:])
                self.helper(nums[i+1:], res, path)
            path.pop()


# 方法二：bit法
class Solution(object):
    def subsetsWithDup(self, nums):


        nums.sort()
        le = len(nums)
        total = 2 ** le
        res = []

        for j in range(total):  # 第几个case
            temp = []
            for i in range(le):  # 第几个element
                shift = le - 1 - i
                if ((j >> shift) & 1):
                    temp.append(nums[i])
            if temp not in res:
                res.append(temp)
        return res


class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        le = len(nums)
        nums.sort()
        total=2**le
        res=[]*total

        for i in range(total):
            res.append([])

        for i in range(le):  #第几个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(total):  #第几个case
                shift = le-1-i
                if ((j>>shift)&1):
                    res[j].append(nums[i])
        return res


# 方法三：iteration

class Solution2(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        # i= -1
        result = [[]]
        size_2 = 1
        # i= 0
        result.append([nums[0]])
        len_result = len(result)
        # i = 1:n
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                start = size_2
            else:
                start = 0
            for j in range(start,len_result):
                temp = result[j][:]+[nums[i]]
                result.append(temp)
            size_2 = len_result  #这个new_start搁在新生的ele的起始位置
            len_result = len(result)
        return result
if __name__ == '__main__':
    s = Solution2()
    a = [1,2,2]
    print s.subsetsWithDup(a)
