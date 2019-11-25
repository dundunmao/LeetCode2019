class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = [0 for i in range(N+1)]
        for i in range(1, N+1):
            c_p = 0  # copy-paste
            for j in range(i-1,-1,-1):
                if i-j-1 > 5:
                    break
                c_p = max(c_p,f[j]*(i-j-1))
            a = f[i - 1] + 1  # 直接敲A
            f[i] = max(a, c_p)
        return f[N]

class Solution2(object):
    def maxA(self, N):
        f = [0 for i in range(N+1)]
        for i in range(1, N+1):
            c_p = 0  # copy-paste
            for j in range(i-1,-1,-1):
                c_p = max(c_p, f[j]*(i-j-2+1))
            a = f[i - 1] + 1  # 直接敲A
            f[i] = max(a, c_p)
        return f[N]

if __name__ == "__main__":
    s = Solution2()
    N = 7
    print s.maxA(N)

