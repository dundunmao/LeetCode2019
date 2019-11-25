class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool

        """
        if n < 4:
            return True
        f = [False for i in range(n)]
        f[0] = True
        f[1] = True
        f[2] = True
        for i in range(3, n):
            f[i] = not (f[i - 1] and f[i - 2] and f[i - 3])
        return f[n - 1]

class Solution(object):
    def canWinNim(self, n):
        return not n % 4 == 0