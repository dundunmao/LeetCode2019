# 同构
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):  #这个要检查否则s="ab",t="aa"会return True
            return False
        le = len(s)
        i,j = 0,0
        hash1 = {}
        while i < le and j < le:
            if hash1.has_key(s[i]):
                if hash1[s[i]] != t[j]:
                    return False
            else:
                hash1[s[i]] = t[j]
            i += 1
            j += 1
        return True


class Solution1(object):
    def isIsomorphic(self, pattern, s):
        assert len(pattern) == len(s)
        inds1 = [-1] * 256
        inds2 = [-1] * 256

        for i in range(len(s)):
            a, b = ord(pattern[i]), ord(s[i])
            if inds1[a] != inds2[b]:  # index of a != index of b -> False
                return False
            inds1[a] = inds2[b] = i
        return True
# 如果一个pattern，多个s
from collections import defaultdict
class Solution2(object):
    # def isIsomorphic(self, pattern, s):
    #     decode = self.patterned(pattern)
    #     decode_s = self.patterned(s)
    #     for i,j in zip(decode,decode_s):
    #         if i!= j:
    #             return False
    #     return True

    def isIsomorphic(self, pattern, s):
        decodes = self.patterned(pattern)
        for indexs in decodes:
            if not all(s[i] == s[indexs[0]] for i in indexs):
                return False
        if self.duplicate([s[decodes[i][0]] for i in range(len(decodes))]):
            return False
        return True
    def patterned(self,s):
        patt = defaultdict(list)
        for index, ele in enumerate(s):
            patt[ele].append(index)
        return patt.values()
    def duplicate(self,array):
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if array[i] == array[j]:
                    return True
        return False

class Solution3(object):
    def isIsomorphic(self, pattern, s):
        i = self.decode(pattern)
        j = self.decode(s)
        if i != j:
            return False
        return True

    def decode(self,s):
        count = 0
        for i in range(len(s)):
            cur = s[i]
            if ord(cur)>= 97:
                s = s.replace(cur,str(count))  #所以相同字母都变成一个数字
                count += 1
        return s


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str1_to_str2 = [0] * 256
        str2_to_str1 = [0] * 256

        for i in range(len(s)):
            c1 = ord(s[i])
            c2 = ord(t[i])
            # s to t 做一遍
            if str1_to_str2[c1] != 0:
                if str1_to_str2[c1] != c2:
                    return False
            else:
                str1_to_str2[c1] = c2
            # t to s 做一遍
            if str2_to_str1[c2] != 0:
                if str2_to_str1[c2] != c1:
                    return False
            else:
                str2_to_str1[c2] = c1
        return True
if __name__ == '__main__':
    s = Solution3()
    # a = "egg" #T
    # b = "add"
    #
    # print s.isIsomorphic(a,b)
    # a = "bac" #F
    # b = "aaa"
    # print s.isIsomorphic(a, b)
    # a = "abcdefghijkabc" #T
    # b = "hijklmnopqrhij"
    # print s.isIsomorphic(a, b)
    # a = "32767" #F
    # b = "65535"
    # print  s.isIsomorphic(a, b)
    # a = "apple" #T
    # b = "ellpa"

    a = "paper" #f
    b = "titie"

    a = "paper" #t
    b = "titie"
    print(s.isIsomorphic(a, b))
