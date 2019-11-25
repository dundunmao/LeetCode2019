
# 方法一，backtracking
class Solution1:

    def sum_subarray(self, arr):
        res = []
        array = []
        pos = 0
        self.helper(arr, res, array, pos)
        ans = 0
        for ele in res:
            ans += sum(ele)
        return ans

    def helper(self, arr, res, array, pos):
        for i in range(pos, len(arr)):
            array.append(arr[i])
            res.append(array[:])
            self.helper(arr, res, array, i + 1)
            array.pop()


# 方法二，bit
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

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
            res.append(temp)
        return res

# 换了i,j的循环层

class Solution1(object):
    def subsets(self, nums):
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
            for j in range(total):  #第几个case
                if ((j>>i)&1):
                    res[j].append(nums[le-1-i])
        return res


# 方法三
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result
# 方法四：iteration
class Solution3(object):
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            le = len(result)
            for i in range(le):
                temp = result[i][:]+[n]
                result.append(temp)
        return result


###################
class Solution:
    def subsets(self, a):
        res = []
        # fake base case: i = -1
        empty_list = []
        res.append(empty_list)
        # general case
        for i in range(len(a)):
            # 1. keep as is
            # add a[i]
            size = len(res)
            for j in range(size):
                array = res[j][:]
                array.append(a[i])
                res.append(array)
        return res

class Solution:
    def subsets(self, a):
        res = []
        path = []
        self.dfs(a, len(a) - 1, res, path)
        return res
    def dfs(self, a, i, res, path):
        if i == -1:
            res.append(path[:])
        else:
            # 边1
            self.dfs(a, i - 1, res, path)
            # 边2
            path.append(a[i])
            self.dfs(a, i - 1, res, path)
            path.pop()


class Solution:
    def subsets(self, a):
        res = []
        path = []
        self.dfs(a, 0, res, path)
        return res
    def dfs(self, a, start, res, path):
        res.append(path[:])
        for i in range(start + 1, len(a) + 1):
            path.append(a[i - 1])
            self.dfs(a, i, res, path)
            path.pop()



import collections
class Solution0:
    def subsets(self, a):
        n = len(a)
        res_deque = collections.deque()
        res_deque.append([])
        for i in range(n):
            size = len(res_deque)
            for j in range(size):
                ele = res_deque.popleft()
                res_deque.append(ele[:])
                ele.append(a[i])
                res_deque.append(ele[:])
                print(res_deque)
        return list(res_deque)

class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        return self.dfs(a, len(a) - 1)
    def dfs(self, a, i):
        if i == -1:
            return [[]]
        left = self.dfs(a, i - 1)
        right = [ele + [a[i]] for ele in left]
        return left + right

if __name__ == '__main__':
    s = Solution10()
    a = ['a','b','c']
    print(s.subsets(a))
