# 方法一：divide&conquer + memories
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s) == 0 or s == '':
            return []
        start = 0
        memo = {}
        # 把每一个word的长度放这个set里
        word_length_set = set([len(ele) for ele in wordDict])
        word_set = set(wordDict)
        res = self.helper(s, word_set, word_length_set, start, memo)
        return [' '.join(temp[:]) for temp in res]
    def helper(self, s, word_set, word_length_set, start, memo):
        if start in memo:
            return memo[start]
        res = []
        for size in word_length_set:
            if start + size <= len(s) and s[start : start + size] in word_set:
                cur_array = [s[start : start + size]]
                temp_array = self.helper(s, word_set, word_length_set, start + size, memo)
                if start + size == len(s):
                    res.append(cur_array)
                else:
                    for ele in temp_array:
                        res.append(cur_array + ele)
        memo[start] = res
        return res

# 方法二：traverse
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        path = []
        self.dfs(s, 0, word_set, res, path)
        return res
    def dfs(self, s, start, word_set, res, path):
        if start == len(s):
            res.append(' '.join(path))
            return
        else:
            for i in range(start, len(s)):
                cur = s[start: i + 1]
                if cur in word_set:
                    path.append(cur)
                    self.dfs(s, i + 1, word_set, res, path)
                    path.pop()
