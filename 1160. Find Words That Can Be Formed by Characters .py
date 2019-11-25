class Solution:
    def countCharacters(self, words, chars: str) -> int:
        hash_to_char = {}
        res = 0
        for ele in chars:
            if ele in hash_to_char:
                hash_to_char[ele] += 1
            else:
                hash_to_char[ele] = 1
        for ele in words:
            hash_for_word = hash_to_char.copy()
            num = 0
            flag = True
            for char in ele:
                if char in hash_for_word:
                    hash_for_word[char] -= 1
                    num += 1
                    if hash_for_word[char] == 0:
                        del hash_for_word[char]
                else:
                    flag = False
                    break
            if flag:
                res += num
        return res
s = Solution()
a = ["hello","world","leetcode"]
b = "welldonehoneyr"
print(s.countCharacters(a, b))
