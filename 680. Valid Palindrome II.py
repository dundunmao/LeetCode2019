# 问一个string是不是palindrome,可以最多去掉一个char
class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPanlin(s,l,r-1) or self.isPanlin(s,l+1,r)
            l += 1
            r -= 1
    def isPanlin(self,s,i,j):

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
if __name__ == '__main__':
    s = Solution()
    a = 'abbb'
    print s.validPalindrome(a)
