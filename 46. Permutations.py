
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [] or nums is None:
            return []
        hash = {}
        res = []
        path = []
        self.helper(nums, res, path,hash)
        return res

    def helper(self, nums, res, path,hash):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(0, len(nums)):
            if i not in hash:
                hash[i] = True
                path.append(nums[i])
                self.helper(nums, res, path,hash)
                path.pop()
                del hash[i]

class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for i in range(len(nums)):
            size = len(res) # 这一层有多少个ele
            while size > 0:
                ele = res.pop(0) # 每次pop出一个ele
                size -= 1
                for k in range(len(ele) + 1): # 往这个ele的每个位置插数
                    ele.insert(k, nums[i])
                    res.append(ele[:])
                    ele.pop(k)
        return res


class Solution:
    def permute(self, a):
        res = []
        path = []
        self.dfs(a, 0, res, path)
        return res
    def dfs(self, a, start, res, path):
        if start == len(a):
            res.append(path[:])
        else:
            for i in range(start, len(a)):
                a[i], a[start] = a[start], a[i]
                path.append(a[start])
                self.dfs(a, start + 1, res, path)
                path.pop()
                a[i], a[start] = a[start], a[i]

class Solution11:
    def permute(self, a):
        res = []
        path = []
        self.dfs(a, 0, res, path)
        return res
    def dfs(self, a, start, res, path):
        if start == len(a):
            res.append(path[:])
        else:
            for i in range(start, len(a)):
                a[start], a[i] = a[i], a[start]
                path.append(a[start])
                self.dfs(a, start + 1, res, path)
                path.pop()
                a[start], a[i] = a[i], a[start]
if __name__ == '__main__':
    nums = [1,2,3,4]
    s= Solution11()
    print(s.permute(nums))
