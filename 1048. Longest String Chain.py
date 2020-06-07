from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 0
        words.sort(key=lambda x:len(x))
        for word in words:
            best = 0
            dp[word] = 1
            for i in range(len(word)):
                new = word[:i] + word[i + 1:]
                if new in dp:
                    best = max(best, dp[new])
            dp[word] = best + 1
            res = max(res, dp[word])
        return res
s = Solution()
a = ["a","b","ba","bca","bda","bdca"]
print(s.longestStrChain(a))
