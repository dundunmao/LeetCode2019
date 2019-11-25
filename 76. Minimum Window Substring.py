# two pointer.基本就是
# hash记录t的char频次
# count记录set(t)的char个数
# 循环开始，j往后走，每次hash里面的value=0，count就减1.
#       一旦count为0了，说明找到一组就更新返回值和最短距离。
#       这时候i要在while里往前走，一直走到遇到t里面的char，也就是count不为0时

# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if len(s) < len(t):
#             return ''
#         res = ''
#         count = len(set(t))   #count记录的是set(t)
#         hash = {}
#         distant = float('inf')
#         for ele in t:        #建 hash，里面含频次
#             hash[ele] = hash.setdefault(ele, 0) + 1
#         i = 0
#         j = -1
#         while i < len(s) and j < len(s):
#             while count == 0:   #当count为0时，处理更不更新distance和res，还要把i往前走，知道count不为0，就是i往外吐时吐出了t里的东西
#                 if distant > j - i + 1:
#                     distant = j - i + 1
#                     res = s[i:j + 1]
#                 if s[i] in hash:
#                     hash[s[i]] += 1
#                     if hash[s[i]] > 0:
#                         count += 1
#                 i += 1
#             j += 1              #每一轮j都要往后走一步，然后检查需不需要更新hash和count。
#             if j < len(s) and s[j] in hash:
#                 hash[s[j]] -= 1
#                 if hash[s[j]] == 0:
#                     count -= 1
#         return res
# # 推荐
# from collections import Counter
# class Solution1(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         if len(s) < len(t):
#             return ''
#         res = ''
#         count = len(set(t))   #count记录的是set(t)
#         hash = {}
#         distant = float('inf')
#         # for ele in t:        #建 hash，里面含频次
#         #     hash[ele] = hash.setdefault(ele, 0) + 1
#         hash = Counter(t)
#         i = 0
#         j = -1
#         while i < len(s) and j < len(s):
#             while count == 0:   #当count为0时，处理更不更新distance和res，还要把i往前走，知道count不为0，就是i往外吐时吐出了t里的东西
#                 if distant > j - i + 1:
#                     distant = j - i + 1
#                     res = s[i:j + 1]
#                 if s[i] in hash:
#                     hash[s[i]] += 1
#                     if hash[s[i]] > 0:
#                         count += 1
#                 i += 1
#             j += 1              #每一轮j都要往后走一步，然后检查需不需要更新hash和count。
#             if j < len(s) and s[j] in hash:
#                 hash[s[j]] -= 1
#                 if hash[s[j]] == 0:
#                     count -= 1
#         return res
# # 最终的
# class Solution2(object):
#     def minWindow(self, s, t):
#         if s is None or t is None or len(s) == 0 or len(t) == 0:
#             return ''
#         count = 0
#         res = ''
#         hash_t = [0 for i in range(256)]  #把t的频次存在256里
#         for string in t:
#             hash_t[ord(string)] += 1
#         hash_s = [0 for i in range(256)] #初始化s里t出现的频次
#         left = self.find_next(0,s,hash_t) #从0开始在s里找t
#         if left == len(s):  #如果s里压根就没t ，就返回''
#             return ''
#         right = left  #如果存在，left和right都从那点开始
#         while right < len(s):
#             # right开始往后走
#             right_char = ord(s[right]) #如果right在s里的频次小于在t里的，s里面加频次，同时说明找到了有效的，count就加一，
#             if hash_s[right_char] < hash_t[right_char]:
#                 count += 1  #count表示（有效计数）
#             hash_s[right_char] += 1
#             # 频次加好，count算好后，检查达不达到res是标准
#             # 当left没到头，count（有效计数）正好等于t的长度，说明找到了
#             # 这时候要处理：更新res；left放在下一个有效位，left往前走时更新hash_s，count也做相应变化
#             while left < len(s) and count == len(t):
#                 if res == '' or len(res) > right - left + 1:
#                     res = s[left:right+1]
#                 left_char = ord(s[left])
#                 if hash_s[left_char] <= hash_t[left_char]: #如果left那个字符在hash_s里比在hash_t里少，说明有效计数也在减少
#                     count -= 1
#                 hash_s[left_char] -= 1
#                 left = self.find_next(left+1, s, hash_t)
#             # 找没找到，都要去找下一个right的位置
#             right = self.find_next(right+1, s, hash_t)
#         return res
#     def find_next(self,start,s,hash_t): #从start开始，在s里，找下一个存在于t的字符
#         while start< len(s):
#             c = ord(s[start])
#             if hash_t[c] != 0:
#                 return start
#             start += 1
#         return start
#
#
# ########################
# class Solution10:
#     def minWindow(self, s: str, t: str) -> str:
#         char_to_freq_hash_t = [0] * 256
#         char_to_freq_hash_s = [0] * 256
#         for ele in t:
#             char_to_freq_hash_t[ord(ele) + 97] += 1
#         diff = len(t)
#         start = 0
#         res = float('inf')
#         res_start = -1
#         res_end = -1
#         for i in range(len(s)):
#             if char_to_freq_hash_t[ord(s[i]) + 97] == 0:
#                 continue
#             # add tail
#             char_to_freq_hash_s[ord(s[i]) + 97] += 1
#             if char_to_freq_hash_s[ord(s[i]) + 97] <= char_to_freq_hash_t[ord(s[i]) + 97]:
#                 diff -= 1
#             # kick off head
#             if diff == 0:
#                 while char_to_freq_hash_t[ord(s[start]) + 97] == 0 or char_to_freq_hash_s[ord(s[start]) + 97] > char_to_freq_hash_t[ord(s[start]) + 97]:
#                     char_to_freq_hash_s[ord(s[start]) + 97] -= 1
#                     start += 1
#                 # cal res
#                 if res > i - start + 1:
#                     res_start = start
#                     res_end = i
#                     res = i - start + 1
#
#         return s[res_start: res_end + 1]


class Solution20:
    def minWindow(self, s: str, t: str) -> str:
        char_to_freq_hash_t = [0] * 256
        for ele in t:
            char_to_freq_hash_t[ord(ele)] += 1
        valid_num = len(t)
        char_to_freq_hash_s = [0] * 256
        start = 0
        min_length = float('inf')
        res = ''
        for i in range(len(s)):
            # add head
            if char_to_freq_hash_t[ord(s[i])] >= 1:
                char_to_freq_hash_s[ord(s[i])] += 1
                if char_to_freq_hash_s[ord(s[i])] <= char_to_freq_hash_t[ord(s[i])]:
                    valid_num -= 1
            while char_to_freq_hash_t[ord(s[start])] <= 0 or char_to_freq_hash_s[ord(s[start])] > char_to_freq_hash_t[
                ord(s[start])]:
                char_to_freq_hash_s[ord(s[start])] -= 1
                start += 1

            # check
            if valid_num == 0:
                if i - start + 1 < min_length:
                    res = s[start: i + 1]
                    min_length = i - start + 1
        return res


if __name__ == "__main__":
    x = Solution20()
    # s = "2412"
    # t = "12"
    # print(x.minWindow(s,t))# ab
    s = "ADOBECODEBANC"
    t = "ABC"
    print(x.minWindow(s,t)) # "BANC"

    s = "cabwefgewcwaefgcf"
    t = "cae"
    print(x.minWindow(s,t)) # "cwae"
    s = "dccaeacae"
    t = "cae"
    print(x.minWindow(s,t)) # "cwae"
