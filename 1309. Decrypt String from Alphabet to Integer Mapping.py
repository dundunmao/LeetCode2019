import collections
class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = False
        res = collections.deque()
        i = len(s) - 1
        while i >= 0:
            if s[i] != '#' and temp == False:
                res.appendleft(chr(int(s[i]) + 96))
                i -= 1
            elif s[i] != '#':
                res.appendleft(chr(int(s[i - 1:i + 1]) + 96))
                i -= 2
                temp = False
            else:
                i -= 1
                temp = True
        return ''.join(res)
s = Solution()
a = "10#11#12"
print(s.freqAlphabets(a))
