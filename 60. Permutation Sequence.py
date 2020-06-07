class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res_string = ''
        # res = [i for i in range(n)]
        factorial = [1 for i in range(n)]
        values = [i + 1 for i in range(n)]
        k = k - 1
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        for i in range(n):
            group = factorial[n - 1 - i]
            res_string += str(values[k // group])
            values.remove(values[k // group])
            k = k % group
        return res_string
s = Solution()
n = 4
k = 17
print(s.getPermutation(n,k))
