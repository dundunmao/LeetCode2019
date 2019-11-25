# 求一串string里最长的无重复char的子串长度
# 基本同题406
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if s == '':
            return 0
        #
        hash = {}
        res = 0
        i = 0
        j = i
        while i < len(s) and j < len(s):
                if not hash.has_key(s[j]):
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j+=1
                else:
                    temp = hash[s[j]] + 1
                    while i < temp:
                        del hash[s[i]]
                        i += 1
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j += 1
        return res


class Solution1:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        map = [0 for i in range(256)]
        i,j = 0,0
        ans = 0
        for i in range(len(s)):
            while j < len(s) and map[ord(s[j])] == 0:
                map[ord(s[j])] = 1
                ans = max(ans, j-i+1)
                j+=1
            map[ord(s[i])] = 0
        return ans


# two pointer，i等着起点，j往前走，边走边加入hash,
# 当发现hash里已经有了的时候，i要走到已经有的那个char的下一位，i边走边减hash里的ele
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if s == '':
            return 0
        #
        hash = {}
        res = 0
        i = 0
        j = i
        while i < len(s) and j < len(s):
                if not hash.has_key(s[j]):
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j+=1
                else:
                    temp = hash[s[j]] + 1
                    while i < temp:
                        del hash[s[i]]
                        i += 1
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j += 1
        return res


class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        hash = {}
        res = 0
        start = 0
        for i in range(len(s)):
            if hash.has_key(s[i]):
                start = max(start, hash[s[i]]+1 )
            res = max(res, i - start +1)
            hash[s[i]] = i
        return res
#######################
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        q = collections.deque()
        res = 0
        for i in range(len(s)):
            while s[i] in hash_set:
                start = q.popleft()
                hash_set.remove(start)
            q.append(s[i])
            hash_set.add(s[i])
            res = max(res, len(q))
        return res
########################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = [False for i in range(256)]
        q = collections.deque()
        res = 0
        count = 0
        for i in range(len(s)):
            while char_map[ord(s[i]) - 97] == True:
                cur = q.popleft()
                char_map[ord(cur) - 97] = False
                count -= 1
            q.append(s[i])
            char_map[ord(s[i]) - 97] = True
            count += 1
            res = max(res, count)

        return res
if __name__ == "__main__":
    s = Solution3()
    x = "a" #2
    print(s.lengthOfLongestSubstring(x))
    x = "abcabcbb"  #3
    print(s.lengthOfLongestSubstring(x))
