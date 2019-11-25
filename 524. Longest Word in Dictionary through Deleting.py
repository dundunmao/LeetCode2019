class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = -1
        res_word = ''
        for word in d:
            length = self.check_valid(s, word)
            if length > res:
                res_word = word
                res = max(res, length)
            elif length == res:
                res_word = min(res_word, word)

        return res_word

    def check_valid(self, s, word):
        count = 0
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j < len(word):
            return -1
        else:
            return len(word)
