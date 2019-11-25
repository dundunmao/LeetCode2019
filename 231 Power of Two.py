class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return not n&(n-1)

if __name__ == "__main__":
    nums = [[1, 2, 3], [4, 5], [1, 2, 3]]
    x = Solution()
    print x.isPowerOfTwo(20)