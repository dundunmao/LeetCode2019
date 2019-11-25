
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        can = [False for i in range(len(A))]
        can[0] = True
        for i in range(1,len(A)):
            for j in range(0,i):
                if can[j] and j+A[j]>=i:
                    can[i] = True
                    break
        return can[-1]
class Solution_greedy:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False] * n
        f[0] = True
        for i in range(0, n):
            if f[i] == True:
                for j in range(1, A[i] + 1):
                    if i + j <= n - 1:
                        f[i + j] = True
                    else:
                        break
        return f[n - 1]

# greedy method 我的练习
class Solution3:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False for i in range(n)]
        f[0] = True
        for i in range(0, n):
            if f[i] == True:
                for j in range(1, A[i] + 1):
                    if i + j < n:
                        f[i + j] = True
            else:
                return False
        return f[-1]


if __name__ == '__main__':
    s = Solution5()
    x = [4,6,9,5,9,3,0]
    print s.canJump(x)
