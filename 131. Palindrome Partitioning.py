# 给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。
#
# 返回s所有可能的回文串分割方案。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 s = "aab"，返回
#
# [
#   ["aa", "b"],
#   ["a", "a", "b"]
# ]

# traverse
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if s is None:
            return []
        result = []
        path = []
        pos = 0
        self.help_function(s,path,pos,result)
        return result
    def help_function(self,s, path,pos,result):
        if pos == len(s):   #起始点遍历到最后一位时,说明完成了.
            path_save = [x for x in path]
            result.append(path_save)
            return
        for i in range(pos,len(s)):
            prefix = s[pos:i+1]
            if not self.isPalindrome(prefix):
                continue
            path.append(prefix)
            self.help_function(s, path, i+1, result)
            path.pop()
    def isPalindrome(self, s):
        beg = 0
        end = len(s)-1
        while beg < end:
            if s[beg] != s[end]:
                return False
            beg += 1
            end -= 1
        return True

# divide&conquer
class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == '':
            return False
        return self.helper(s)
    def helper(self, s):
        if s == '':
            return []
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s) + 1):
            if self.is_pali(s[:i]):
                A = self.helper(s[i:])
                if A == []:
                    res.append([s[:i]])
                for ele in A:
                    res.append([s[:i]] + ele)
        return res
    def is_pali(self, s):  # return boolean
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


class Solution:
    def minCut(self, s: str) -> int:
        res = [None for i in range(len(s))]
        # base case: i = 0
        res[0] = 0
        pal_array = self.is_pal(s)
        # genera case: i = 1 ~ n-1
        for i in range(1, len(s)):
            if self.is_pal(s, 0, i):
                res[i] = 0
            else:
                res[i] = len(s) - 1
                for j in range(0, i):
                    if self.is_pal(s, j + 1, i):
                        res[i] = min(res[i], 1 + res[j])
        return res[len(s) - 1]

    def is_pal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution6(object):
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
####################

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palim_matrix = self.palimdrome(s)
        res = []
        path = []
        self.dfs(s, len(s) - 1, path, res, palim_matrix)
        return res

    def dfs(self, s, end, path, res, palim_matrix):
        if end == -1:
            res.append(path[:][::-1])
        for i in range(0, end + 1):
            if palim_matrix[i][end]:
                path.append(s[i: end + 1])
                self.dfs(s, i - 1, path, res, palim_matrix)
                path.pop()

    def palimdrome(self, s):
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




if __name__ == '__main__':


    x = Solution6()
    s = "aab"
    print(x.partition(s))
    s = 'acbb'
    print(x.partition(s))

