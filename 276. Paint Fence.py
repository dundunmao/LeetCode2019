class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:  #没栅栏是0种涂法
            return 0
        if n == 1:  #一个栅栏 k 种涂法
            return k
        same = 0
        diff = k
        total = k
        for i in range(2,n+1):
            same = diff
            diff = (k-1)*total
            total = same + diff
        return total
