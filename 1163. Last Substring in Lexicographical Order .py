class Solution:
    def lastSubstring(self, s: str) -> str:
        stack_char = []
        stack_char.append(0)
        temp = 0
        for i in range(1, len(s)):
            # print(s[temp:])
            j = temp
            cur = i
            while i < len(s):
                if s[j] == s[i]:
                    if s[j:] > s[i:]:
                        break
                    else:
                        temp = cur
                        break
                elif s[j] > s[i]:
                    break
                else:
                    temp = cur
                    break
        return s[temp:]
s = Solution()
x = "abab"
print(s.lastSubstring(x))
x = "leetcode"
print(s.lastSubstring(x))
x = "zbbzbczabzd"
print(s.lastSubstring(x))
x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(s.lastSubstring(x))
