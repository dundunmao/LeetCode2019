class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = Result(k)
        # result = []
        path = []
        self.dfs(1, k, result, n, path)
        return result.res

    def dfs(self, i, k, result, n, path):
        if result.k == 0:
            return
        path.append(i)
        if len(path) == n:
            result.res = path[:]
            result.k -= 1
        for j in range(i + 1, n + 1):
            self.dfs(j, k, result, n, path)
        path.pop()


class Result:
    def __init__(self, k):
        self.res = []
        self.k = k
x = Solution()
print(x.getPermutation(3,3))
print(x.getPermutation(4,9))

def complement(a):
    while True:
        cur = a 

