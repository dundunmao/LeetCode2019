class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequ = {}
        for char in s:
            if char in char_to_frequ:
                char_to_frequ[char] += 1
            else:
                char_to_frequ[char] = 1
        for i in range(len(s)):
            if char_to_frequ[s[i]] == 1:
                return i
        return -1
