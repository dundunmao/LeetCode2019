class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.match(word, pattern):
                res.append(word)
        return res

    def match(self, word, pattern):
        match_hash = {}
        for i in range(0, len(word)):
            w = word[i]
            p = pattern[i]
            if w not in match_hash:
                match_hash[w] = p
            if match_hash[w] != p:
                return False
        # 下面保证没有两个value是一样的，就是不能有相同的p跟不同的w配对
        # 我习惯reverse再做一遍，这里是改进的方法
        seen = [None for i in range(26)]
        for p in match_hash.values():
            if seen[ord(p) - 97] == True:
                return False
            seen[ord(p) - 97] = True
        return True

