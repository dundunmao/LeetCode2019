class Solution:
    def palindromePairs(self, words):
        res = []
        if not words or len(words) < 2:
            return res
        hash = {}
        for i in range(len(words)):
            hash[words[i]] = i
        for i in range(len(words)):
            #把words[i]作为base，看有没有其他word跟他和
            for j in range(len(words[i]) + 1):
                str1 = words[i][0: j]
                str2 = words[i][j:]
                if self.is_palindrome(str1):
                    reversed_str2 = str2[::-1]
                    # 如果有这么一个str，而且不是words[i]自己
                    if reversed_str2 in hash and hash[reversed_str2] != i:
                        res.append((hash[reversed_str2], i))
                if len(str2) != 0 and self.is_palindrome(str2):
                    reversed_str1 = str1[::-1]
                    if reversed_str1 in hash and hash[reversed_str1] != i:
                        res.append((i, hash[reversed_str1]))
        return res

    def is_palindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

s = Solution()
a = ["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(a))
a = ["a",""]
print(s.palindromePairs(a))
