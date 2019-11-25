class Solution:
    def shortestWordDistance(self, words, word1: str, word2: str) -> int:
        res = float('inf')
        res1 = []
        res2 = []
        for i in range(len(words)):
            if words[i] == word1:
                res1.append(i)
            if words[i] == word2:
                res2.append(i)
        if word1 == word2 and len(res1) <= 1:
                return 2147483647

        i = 0
        j = 0
        while i < len(res1) and j < len(res2):
            if res1[i] == res2[j]:
                i += 1
                continue
            res = min(res, abs(res1[i] - res2[j]))
            if res1[i] > res2[j]:
                j += 1
            else:
                i += 1
        return res

s = Solution()
w1 = 'a'
w2 = 'a'
words = ['a', 'a', 'a']
print(s.shortestWordDistance(words, w1, w2))
w1 = 'makes'
w2 = 'makes'
words = ["practice", "makes", "perfect", "coding", "makes"]
print(s.shortestWordDistance(words, w1, w2))
w1 = 'practice'
w2 = 'practice'
words = ["practice", "makes", "perfect", "coding", "makes"]
print(s.shortestWordDistance(words, w1, w2))
