class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_char = {}
        for i in range(len(s)):
            last_char[s[i]] = i
        n = len(last_char)
        res = []
        visited = [False] * 26
        for i in range(0, len(s)):
            if visited[ord(s[i]) - 97] == True:
                continue
            # if s[i] < prev, and there is prev in the future, pop
            while len(res) > 0 and s[i] < s[res[-1]] and last_char[s[res[-1]]] > i:
                visited[ord(s[res[-1]]) - 97] = False
                res.pop()
            # if s[i] > prev, append
            res.append(i)
            visited[ord(s[i]) - 97] = True
        return ''.join([s[i] for i in res])


s = Solution()
a = "bcabc" # 'abc
print(s.removeDuplicateLetters(a))
a = "cbacdcbc" # "acdb"
print(s.removeDuplicateLetters(a))
a = "bbcaac" #"bac"
print(s.removeDuplicateLetters(a))
