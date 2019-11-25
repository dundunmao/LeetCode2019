class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res = res * 26 + ord(s[i]) - 65 + 1
        return res
s = Solution()
x = 'AB'
print(s.titleToNumber(x))
