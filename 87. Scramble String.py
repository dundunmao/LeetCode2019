# DP

class Solution4(object):
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        n = len(s1)
        f = [[[None for i in range(n+1)] for j in range(n)] for k in range(n)]
        for k in range(1,n+1):
            for i in range(0,n-k+1):
                for j in range(0, n-k+1):
                    if k == 1:
                        f[i][j][k] = (s1[i] == s2[j])
                    else:
                        for p in range(1,k):
                            if not f[i][j][k]:
                                bool1 = f[i][j][p] and f[i + p][j + p][k - p]    #左match左
                                bool2 = f[i][j + k - p][p] and f[i + p][j][k - p]              #左match右
                                f[i][j][k] = bool1 or bool2
        return f[0][0][n]
# 记忆化搜索recursive
class Solution(object):
    def isScramble(self, s1, s2):
        hash = {}
        return self.helper(s1,s2,hash)
    def helper(self,s1,s2,hash):
        if len(s1) != len(s2):
            return False
        if hash.has_key(s1+'#'+s2):
            return hash[s1+'#'+s2]
        n = len(s1)
        # if n == 0:
        #     return True
        if n == 1:
            return s1[0] == s2[0]
        for k in range(1,n):
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:n], s2[k:n]) or self.isScramble(s1[0:k], s2[n-k:n]) and self.isScramble(s1[k:n], s2[0:n-k]):
                hash[s1+'#'+s2] = True
                return True
        hash[s1+'#'+s2] = False
        return False

# 最终的recursive
class Solution3(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2): return False

        if len(s1) <= 3: return True

        for i in range(1, len(s1)):
            boo1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) #s1的左跟s2的左match，#s1的右跟s2的右match，
            boo2 = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]) #s1的左跟s2的右match，#s1的右跟s2的左match，

            if boo1 or boo2: return True

        return False



class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return s1 == s2
        d, d1, d2 = {}, {}, {}
        for i, s in enumerate(s1[:-1], 1):
            d[s] = d.get(s, 0) + 1
            d1[s2[i - 1]] = d1.get(s2[i - 1], 0) + 1
            d2[s2[-i]] = d2.get(s2[-i], 0) + 1
            if d == d1 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if d == d2 and self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s1) - i]):
                return True
        return False
if __name__ == "__main__":
    s = Solution4()
    print(s.isScramble('aa','aa'))

