class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        map = {}
        j = 0
        for i in range(len(s)):
            while j < len(s):  #i固定,j往下走
                if map.has_key(s[j]):
                    map[s[j]] += 1
                else:
                    if len(map) == k: #当map存了k对时，说明k个distinct char了，停止
                        break
                    map[s[j]] = 1
                j+=1
            max_len =max(max_len, j-i) #更新每次最大
            if map.has_key(s[i]):  #把i这个位置的char去掉，准备进入下一个i
                count = map[s[i]]
                if count > 1:
                    map[s[i]] = count - 1
                else:
                    del map[s[i]]
        return max_len
    def lengthOfLongestSubstringKDistinct1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        max_len = 0
        map = {}
        j = 0
        i = 0
        while i < len(s):
            while j < len(s):  #i固定,j往下走
                if map.has_key(s[j]):
                    map[s[j]] += 1
                else:
                    if len(map) == k: #当map存了k对时，说明k个distinct char了，停止
                        break
                    map[s[j]] = 1
                j+=1
            max_len =max(max_len, j-i) #更新每次最大
            while map.has_key(s[i]):  #i往下走，如果频率大于1就减频率，如果=1，就删除，这时候i就不走了
                count = map[s[i]]
                if count > 1:
                    map[s[i]] = count - 1
                    i += 1
                else:
                    del map[s[i]]
                    i += 1
                    break
        return max_len

import collections
##########
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_to_freq_hash = {}
        q = collections.deque()
        res = 0
        size = 0
        for i in range(len(s)):
            # 加我
            q.append(s[i])
            # 调整hash
            if s[i] in char_to_freq_hash:
                char_to_freq_hash[s[i]] += 1
            else:
                char_to_freq_hash[s[i]] = 1
                size += 1
            # 删头
            while size == k + 1 and len(q) > 0:
                start = q.popleft()
                char_to_freq_hash[start] -= 1
                if char_to_freq_hash[start] == 0:
                    del char_to_freq_hash[start]
                    size -= 1

            res = max(res, len(q))
        return res


if __name__ == '__main__':
    s = Solution()
    # a = "aaaabc"
    # k = 2
    #
    # print s.lengthOfLongestSubstringKDistinct1(a,k)
    # a = 'eceba'
    # k = 2
    # print s.lengthOfLongestSubstringKDistinct1(a, k)
    a = 'a'
    k = 0
    print s.lengthOfLongestSubstringKDistinct1(a, k)
