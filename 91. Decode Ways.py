# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

# 方法一 backtracking + memorization

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        if s == '0':
            return 0
        hash = {}
        return self.helper(s, 0, hash)

    def helper(self, s, pos, hash): #从pos为起点走，他就是把pos+1为起点和把pos+2为起点加起来
        if pos == len(s):
            return 1
        elif pos == len(s) + 1:
            return 0
        if hash.has_key(s[pos:]):   #先看hash里有没有
            return hash[s[pos:]]
        first = 0
        second = 0
        # 每往下走一步都有两种走法，走一格或走两格，走的时候要check可不可以走，我们需要把这两种方式加起来，
        if int(s[pos:pos + 1]) > 0: #如果这步大于0，可以走。否则走不通，不算了
            first = self.helper(s, pos + 1, hash) #可以走一格时，目前位置(i)的走法=下一个位置(i+1)的走法

        if int(s[pos:pos + 2]) <= 26 and int(s[pos:pos + 2]) > 9:  #如果这步在9-26之间，可以走。否则走不通，不算了
            second = self.helper(s, pos + 2, hash)

        hash[s[pos:]] = first + second  # hash记录
        return first + second

# DP
class Solution1(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        f = [0 for i in range(len(s) + 1)]

        if s[0] == '0':
            return 0
        else:
            f[0] = 1
            f[1] = 1
        for i in range(2,n+1):
            first = int(s[i-1:i])  #前一个
            second = int(s[i-2:i])  #前俩个
            if first >= 1 and first <= 9:
                f[i] = f[i-1]
            if second >= 10 and second <= 26:
                f[i] += f[i-2]
        return f[n]


#滚动数组
class Solution2(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        f = [0 for i in range(3)]
        if s[0] == '0':
            return 0
        else:
            f[0] = 1
            f[1] = 1
        for i in range(2,n+1):
            first = int(s[i-1:i])  #前一个
            second = int(s[i-2:i])  #前俩个
            f[i % 3] = 0 #这里记得在做当前位置之前要先清空他，
            if first >= 1 and first <= 9:
                f[i%3] = f[(i-1)%3]
            if second >= 10 and second <= 26:
                f[i%3] += f[(i-2)%3]
        return f[n%3]  #最后返回的是n % 3



# 记两个variable：pre1和pre2

class Solution3(object):
    def numDecodings(self, s):
        if s is None or len(s) == 0:
            return 0
        # i:-1
        pre2 = 1

        # i:0
        if s[0] == '0':
            return 0
        pre1 = 1
        # i: 1 ~ n-1
        for i in range(2,len(s)+1):
            cur = 0
            first = int(s[i-1:i])  #前一个
            second = int(s[i-2:i])  #前俩个
            if first >= 1 and first <= 9:
                cur = pre1
            if second >= 10 and second <= 26:
                cur += pre2
            pre2 = pre1
            pre1 = cur
        return pre1


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        if s[0] == '0':
            pre1 = 0
        else:
            pre1 = 1

        if len(s) == 1:
            return pre1

        pre2 = 1

        for i in range(1, len(s)):
            res = 0
            if s[i] != '0':
                res += pre1

            if int(s[i - 1:i + 1]) < 27 and int(s[i - 1:i + 1]) > 9:
                res += pre2

            pre2 = pre1
            pre1 = res
        return res

class Solution:
    def numDecodings(self, s: str) -> int:
        return self.dfs(s, len(s) - 1)
    def dfs(self, s, end):
        if end == 0:
            if s[end] == '0':
                return 0
            else:
                return 1
        if end == -1:
            return 1

            # if int(s[end - 1: end + 1]) <= 26 and int(s[end - 1: end + 1]) >= 11:
            #     return 2
            # elif s[end - 1] == '0' or s[end] == '0':
            #     return 0
            # else:
            #     return 1

        res = 0
        if s[end] != '0':
            res = self.dfs(s, end - 1)
        if int(s[end - 1: end + 1]) <= 26 and int(s[end - 1: end + 1]) > 9:
            res += self.dfs(s, end - 2)
        return res


class Solution:
    def numDecodings(self, s: str) -> int:
        res = {}
        self.dfs(s, len(s) - 1, res)
        return res[len(s) - 1]
    def dfs(self, s, end, res):
        if end in res:
            return res[end]
        if end == 0:
            if s[end] == '0':
                res[end] = 0
            else:
                res[end] = 1
            return res[end]
        if end == -1:
            res[end] = 1
            return res[end]


        result = 0
        if s[end] != '0':
            result = self.dfs(s, end - 1, res)
        if int(s[end - 1: end + 1]) <= 26 and int(s[end - 1: end + 1]) > 9:
            result += self.dfs(s, end - 2, res)
        res[end] = result
        return res[end]
if __name__ == "__main__":
    strs = "226"
    # strs = "26"
    # strs = "35465"
    # strs = "10"
    # strs = "01"
    s = Solution7()
    print(s.numDecodings(strs))
