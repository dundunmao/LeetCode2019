class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j = 0,0
        hash = {}
        res = 0
        while i < len(s):
            while j < len(s):
                if s[j] in hash:
                    hash[s[j]] += 1
                else:
                    if len(hash) == 2:
                        break
                    hash[s[j]] = 1
                j += 1
            res = max(res,j-i)
            while i < j:
                if hash[s[i]]>1:
                    hash[s[i]] -= 1
                    i += 1
                else:
                    del hash[s[i]]
                    i += 1
                    break
        return res