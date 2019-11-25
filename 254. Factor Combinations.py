
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        array = []
        start = 2
        self.helper(res, array, n, start)
        return res

    def helper(self, res, array, n, start):
        if n == 1 and len(array) > 1: #n=1是退出条件，所以for循环是要循环到n的，这样n/i=1试符合退出条件，
            res.append(array[:])
            return
        for i in range(start, n+1):  #n这个数并不算因子，遍历到n是为了符合退出条件
            if n % i == 0:
                array.append(i)
                self.helper(res, array, n / i, i )
                array.pop()
import math
class Solution1(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        array = []
        start = 2
        self.helper(res, array, n, start)
        return res

    def helper(self, res, array, n, start):
        if n == 1 and len(array) > 1:
            res.append(array[:])
            return
        i = start
        while i <= n :
            if i > int(math.sqrt(n)):  #这里检查如果超过平方根了，就直接让i=n,走到最后，因为当i=n时，会让n/i=1，这样就符合退出条件了
                i = n
            if n % i == 0:
                array.append(i)
                self.helper(res, array, n / i, i)
                array.pop()
            i+=1


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        path_of_left_brother = []
        results = []
        self.dfs(1, n, path_of_left_brother, results)
        return results

    def dfs(self, left, right, path_of_left_brother, results):

        if left != 1:
            path_of_left_brother.append(left)

        if left != 1:
            res = path_of_left_brother[::]
            res.append(right)
            results.append(res)

        sqrt_right_brother = int(math.sqrt(right))
        for left_child in range(max(2, left), sqrt_right_brother + 1):
            if right % left_child == 0:
                self.dfs(left_child, right // left_child, path_of_left_brother, results)

        if left != 1:
            path_of_left_brother.pop()

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        start = 2
        self.dfs(res, path, n, start)
        return res

    def dfs(self, res, path, n, start):
        if n == 1:
            if len(path) > 1:
                res.append(path[:])
        else:
            for i in range(start, n + 1):
                if n % i == 0:
                    path.append(i)
                    self.dfs(res, path, n / i, i)
                    path.pop()



if __name__ == "__main__":
    a = 5
    x = Solution()
    print(x.getFactors(a))
