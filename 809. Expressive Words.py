class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for word in words:
            if self.help(S, word):
                res += 1
        return res

    def help(self, s, word):
        i = 0
        j = 0
        m = len(s)
        n = len(word)
        while i < m and j < n:
            if s[i] == word[j]:
                target = s[i]
                step_s = 0
                step_w = 0
                while i < m and s[i] == target:
                    i += 1
                    step_s += 1
                while j < n and word[j] == target:
                    j += 1
                    step_w += 1
                if step_w > step_s:
                    return False
                if step_s < 3 and step_s != step_w:
                    return False
            else:
                return False
        return i == m and j == n
