class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        num = n
        while num != 0:
            res += num/5
            num /= 5
        return res
if __name__ == '__main__':
    s = Solution()
    n = 50
    print(s.trailingZeroes(n))
