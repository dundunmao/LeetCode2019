class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        # hash里存order
        hash_char_to_pos = {}
        for i in range(len(order)):
            hash_char_to_pos[order[i]] = i
        # 每相邻两个单词一组，把前面相同的char去掉后，比较不同的第一个char
        for i in range(1, len(words)):
            j = 0
            while j < len(words[i - 1]) and j < len(words[i]):
                if words[i - 1][j] == words[i][j]:
                    j += 1
                else:
                    break
            # 查其中一个或者两个j走到头时的情况
            if j == len(words[i - 1]) and j == len(words[i]):
                return True
            elif j == len(words[i - 1]):
                return True
            elif j == len(words[i]):
                return False
            # 如果都没走到头的情况
            if hash_char_to_pos[words[i - 1][j]] > hash_char_to_pos[words[i][j]]:
                return False
            else:
                continue
        return True
s = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(s.isAlienSorted(words, order))

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))
