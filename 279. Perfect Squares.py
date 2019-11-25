import math
class Solution1(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [ float('inf') for i in range(n+1)]
        f[0] = 0
        for i in range(0,n+1):
            for j in range(1, int(math.sqrt(i))+1):
                f[i] = min(f[i], f[i-j*j]+1)
        return f[n]

from collections import deque
class Solution(object):
    def numSquares(self, n):
        q = deque()
        q.append(0)
        hash = set()
        hash.add(0)
        depth = 0
        while len(q) != 0:
            size = len(q)
            depth += 1
            while size > 0:
                cur = q.popleft()
                for i in range(1,int(math.sqrt(n))+1):
                    temp = cur + i*i #从当前的位置，加上若干给平方数，看看能不能到n
                    if temp == n: #如果到n了，说明这一层就到了，返回层数
                        return depth
                    if temp > n:  #如果超过n了，就不用再试了
                        break
                    if temp not in hash:  #如果实验的数不在hash里，就放hash里，并且放queue里，作为下一层。
                        q.append(temp)
                        hash.add(temp)
                size -= 1
        return depth


if __name__ == "__main__":
    a = 12
    x = Solution()
    print x.numSquares(a)
