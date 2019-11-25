# 给出一个具有重复数字的列表，找出列表所有不同的排列。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出列表 [1,2,2]，不同的排列有：
#
# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [] or nums is None:
            return []
        res = []
        path = []
        nums.sort()
        visit = [False]*len(nums)
        self.helper(nums, res, path,visit)
        return res

    def helper(self, nums, res, path,visit):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(0, len(nums)):
            if visit[i] == True or (i !=0 and nums[i] == nums[i-1] and visit[i-1] == False):
                continue
            path.append(nums[i])
            visit[i] = True
            self.helper(nums, res, path,visit)
            path.pop()
            visit[i] = False


#我的练习
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        last = None
        pos = []
        index = None
        nums.sort()
        self.helper(nums, res, path, last, pos, index)
        return res
    def helper(self, nums, res, path, last, pos, index):
        if len(path) == len(nums):
            if path not in res:
                res.append(path[:])
            return
        for i in range(len(nums)):
            if i not in pos:
                if last != nums[i] or len(path) != index:
                    path.append(nums[i])
                    pos.append(i)
                    self.helper(nums, res, path, last, pos, index)
                    index = len(path) - 1
                    last = path.pop()
                    pos.pop()

#放弃
class Solution2(object):
    def permuteUnique(self, nums):
        res = []
        res.append([])
        nums.sort()
        hash = {}
        for i in range(len(nums)):
            for j in range(len(res)):  #这个循环用来pop，pop时不用考虑duplicate
                list = res.pop(0)
                for k in range(len(list)+1): #这个循环用来append，因为是插好一个append一个，所以这个时候需要考虑duplicate
                    if nums[i] in hash and hash[nums[i]][-1] >= k:
                        continue
                    list.insert(k,nums[i])   #考虑结果的有序性会避免重复的结果，所以不要插在duplicate的前面
                    hash[nums[i]] = k
                    res.append(list[:])
                    list.pop(k)
                    del hash[nums[i]]
        return res

if __name__ == '__main__':
    # nums = [1,1,2]   #[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    nums = [3,3,0,3]   #[[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
    s= Solution2()
    print s.permuteUnique(nums)
