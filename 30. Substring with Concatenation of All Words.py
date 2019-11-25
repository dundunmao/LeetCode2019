import copy
# time limit
class Solution:
    def findSubstring(self, s: str, words):
        if len(words) == 0 or len(s) == 0:
            return []
        word_hash = {}
        size = len(words[0])
        diff = len(words)
        for word in words:
            if word in word_hash:
                word_hash[word] += 1
            else:
                word_hash[word] = 1
        res = []
        i = 0
        hash_map_copy = copy.deepcopy(word_hash)
        for i in range(len(s)):
            start = i
            while s[start:start + size] in hash_map_copy and hash_map_copy[s[start:start + size]] > 0:
                diff -= 1
                hash_map_copy[s[start:start + size]] -= 1
                start = start + size
            if diff == 0:
                res.append(i)
            hash_map_copy = copy.deepcopy(word_hash)
            diff = len(words)
        return res
x = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(x.findSubstring(s, words)) #[0,9]
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(x.findSubstring(s, words)) #【】
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(x.findSubstring(s, words)) #[6,9,12]
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(x.findSubstring(s, words)) #[8]


