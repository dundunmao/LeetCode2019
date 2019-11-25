
# 返回 3
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n==0:
            return 1
        if n <= 2:
            return n
        result = [0 for i in range(n)]
        result[0] = 1
        result[1] = 2
        for i in range(2, n):
            result[i] = result[i-1]+result[i-2]
        return result[n-1]
