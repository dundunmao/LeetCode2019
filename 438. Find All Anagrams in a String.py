class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic = {}
        result = []
        for str in p:
            if str not in dic:
                dic[str] = 1
            else:
                dic[str] += 1
        count = len(dic)
        i = 0
        j = 0
        while j < len(s):
            if dic.has_key(s[j]):
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    count -= 1
            j += 1

            while count == 0:
                if dic.has_key(s[i]):
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        count += 1
                if j - i == len(p):
                    result.append(i)
                i += 1
        return result
class Solution:
    def __init__(self):
        self.length = 26
        self.offset = 97
    def findAnagrams(self, s: str, p: str):
        res = []

        char_to_freq_p = [0 for i in range(self.length)]
        for i in range(len(p)):
            index = ord(p[i]) - self.offset
            char_to_freq_p[index] += 1

        dist = len(p)
        char_to_freq_s = [0 for i in range(self.length)]
        for i in range(len(s)):
            # 1: add s[i]
            index = ord(s[i]) - self.offset
            char_to_freq_s[index] += 1
            if char_to_freq_p[index] > 0 and char_to_freq_s[index] <= char_to_freq_p[index]:
                dist -= 1
            # 2: remove s[i - len(p)]
            if i >= len(p):
                index = ord(s[i - len(p)]) - self.offset
                char_to_freq_s[index] -= 1
                if char_to_freq_p[index] > 0 and char_to_freq_s[index] < char_to_freq_p[index]:
                    dist += 1
            # 3. result
            if i - len(p) + 1 >= 0 and dist == 0:
                res.append(i - len(p) + 1)
        return res



class Solution1:
    def findAnagrams(self, s: str, p: str):
        res = []

        char_to_freq_p = [0] * 256
        char_to_freq_s = [0] * 256
        for i in range(len(p)):
            char_to_freq_p[ord(p[i])] += 1

        diff = len(p)
        start = 0
        for i in range(len(s)):
            # add 尾
            cur = s[i]
            if char_to_freq_p[ord(cur)]:
                char_to_freq_s[ord(cur)] += 1
                if char_to_freq_s[ord(cur)] <= char_to_freq_p[ord(cur)]:
                    diff -= 1
            # del 头
            prev = s[start]
            if i - start + 1 > len(p):
                if char_to_freq_p[ord(prev)]:
                    char_to_freq_s[ord(prev)] -= 1
                    if char_to_freq_s[ord(prev)] < char_to_freq_p[ord(prev)]:
                        diff += 1
                start += 1
            # 清算一次
            if i - start + 1 == len(p) and diff == 0:
                res.append(start)
        return res


class Solution0:
    def findAnagrams(self, s: str, p: str):
        res = []

        char_to_freq_p = [0] * 256
        char_to_freq_s = [0] * 256
        count = len(p)
        for i in range(len(p)):
            char_to_freq_p[ord(p[i])] += 1
        for i in range(len(s)):
            if char_to_freq_p[ord(s[i])] == 0:
                continue
            # add head
            char_to_freq_s[ord(s[i])] += 1
            if char_to_freq_s[ord(s[i])] <= char_to_freq_p[ord(s[i])]:
                count -= 1
                # delete tail
            if i >= len(p):
                prev = s[i - len(p)]
                char_to_freq_s[ord(prev)] -= 1
                if char_to_freq_s[ord(prev)] < char_to_freq_p[ord(prev)]:
                    count += 1
            if count == 0:
                res.append(i - len(p) + 1)
        return res


s = Solution0()
p = "cbaebabacd"
t = "abc"
print(s.findAnagrams(p,t))
