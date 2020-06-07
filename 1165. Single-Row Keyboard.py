class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index_map = {}
        for i in range(len(keyboard)):
            index_map[keyboard[i]] = i
        start = 0
        res = 0
        for i in range(len(word)):
            pos = index_map[word[i]]
            res += abs(pos - start)
            start = pos
        return res
