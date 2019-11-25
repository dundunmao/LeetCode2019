
# 给定一个字符串s，将s分割成一些子串，使每个子串都是回文。
#
# 返回s符合要求的的最少分割次数。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如，给出字符串s = "aab"，
#
# 返回 1， 因为进行一次分割可以将字符串s分割成["aa","b"]这样两个回文子串
# 记忆化搜索的DP
class Solution:
    def palimdrome(self, s):
        is_pa= [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_pa[i][i+1] = True
            else:
                is_pa[i][i + 1] =False
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2,len(s)):
                is_pa[i][j] = is_pa[i+1][j-1] and (s[i] == s[j])
        return is_pa
    def minCut(self, s):
        if s is None or len(s) == 0:
            return 0
        is_pa = self.palimdrome(s)
        func = [i for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if is_pa[j][i - 1]:
                    func[i] = min(func[i], func[j] + 1)
        return func[len(s)] - 1

#这种是正在DP，但是超时，所以要把palindrome存矩阵里
class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if s is None or len(s) == 0:
            return 0
        # normal case
        f = [i for i in range(len(s))]
        f.insert(0, -1)
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if self.is_p(s[j:i]):
                    f[i] = min(f[i], f[j] + 1)
        return f[len(s)]

    def is_p(self, s):  # return boolean
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution_rocky:
    def minCut(self, s: str) -> int:
        res = [None for i in range(len(s))]
        return self.helper(s, len(s) - 1, res)
    def helper(self, s, i, res):
        if res[i] != None:
            return res[i]
        if self.is_pal(s, 0, i):
            res[i] = 0
        else:
            res[i] = float('inf')
            for j in range(0, i):
                if self.is_pal(s, j+1, i):
                    res[i] = min(res[i], 1 + self.helper(s, j, res))
        return res[i]
    def is_pal(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

class Solution_rocky2:
    def minCut(self, s: str) -> int:
        res = [None for i in range(len(s))]
        # base case: i = 0
        res[0] = 0
        pal_array = self.is_pal(s)
        # genera case: i = 1 ~ n-1
        for i in range(1, len(s)):
            if pal_array[0][i]:
                res[i] = 0
            else:
                res[i] = len(s) - 1
                for j in range(0, i):
                    if pal_array[j+1][i]:
                        res[i] = min(res[i], 1 + res[j])
        return res[len(s) - 1]

    def is_pal(self, s):
        is_pa = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_pa[i][i+1] = True
            else:
                is_pa[i][i + 1] =False
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2,len(s)):
                is_pa[i][j] = is_pa[i+1][j-1] and (s[i] == s[j])
        return is_pa

#因为is_pal会超时
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        f = [i for i in range(size)]
        for i in range(1, size):
            if self.is_pal(s, 0, i):
                f[i] = 0
            for j in range(i):
                if self.is_pal(s, j + 1, i):
                    f[i] = min(f[i], f[j] + 1)
        return f[size - 1]
 
    def is_pal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

###############
# recursive
class Solution2:
    def minCut(self, s: str) -> int:
        pal_array = self.is_pal(s)
        return self.dfs(s, len(s) - 1, pal_array)

    def dfs(self, s, cur, pal_array):
        res = cur
        for i in range(cur):
            if i == 0 and pal_array[i][cur]:
                return 0
            if pal_array[i+1][cur]:
                res = min(res, self.dfs(s, i, pal_array) + 1)
        return res

    def is_pal(self, s):
        is_pa = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_pa[i][i + 1] = True
            else:
                is_pa[i][i + 1] = False
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                is_pa[i][j] = is_pa[i + 1][j - 1] and (s[i] == s[j])
        return is_pa

#############recursive + memorize
class Solution4:
    def minCut(self, s: str) -> int:
        result = [float('inf')] * len(s)
        pal_array = self.is_pal(s)
        self.dfs(s, len(s) - 1, result, pal_array)
        return result[len(s) - 1]

    def dfs(self, s, cur, result, pal_array):
        if result[cur] != float('inf'):
            return result[cur]
        if cur == 0:
            result[cur] = 0
            return 0
        res = result[cur]
        for i in range(cur):
            if i == 0 and pal_array[i][cur]:
                result[cur] = 0
                return result[cur]
            if pal_array[i+1][cur]:
                res = min(res, self.dfs(s, i, result, pal_array) + 1)

        result[cur] = res
        return res

    def is_pal(self, s):
        is_pa = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                is_pa[i][i + 1] = True
            else:
                is_pa[i][i + 1] = False
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                is_pa[i][j] = is_pa[i + 1][j - 1] and (s[i] == s[j])
        return is_pa

if __name__ == "__main__":
    s = 'a'
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    x = Solution4()
    print(x.minCut(s))


