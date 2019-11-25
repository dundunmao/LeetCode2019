# 超时
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        end = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                i = 0
                end -= 1
                j = end
        if end == len(s) - 1:
            return s

        return s[end + 1:][::-1] + s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[j:][::-1] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]
s = Solution()
x = 'aaaaaaaaaaaa'
print(s.shortestPalindrome(x))
