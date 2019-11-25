import collections


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        for_k = self.lengthOfLongestSubstringKDistinct(A, K)
        for_k_minus = self.lengthOfLongestSubstringKDistinct(A, K - 1)
        return sum(a - b for a, b in zip(for_k, for_k_minus))

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res_array = [0] * len(s)
        char_to_freq_hash = {}
        q = collections.deque()
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

            res_array[i] = len(q)
        return res_array

    
s = Solution()
A = [1,1,1,1,1,1,1,1]
K = 1 # 36
print(s.subarraysWithKDistinct(A,K))

A = [2,2,1,2,2,2,1,1]
K = 2 # 23
print(s.subarraysWithKDistinct(A,K))

A = [1, 2]
K = 1 # 2
print(s.subarraysWithKDistinct(A,K))
A = [1,2,1,2,3]
K = 2 # 7
print(s.subarraysWithKDistinct(A,K))
A = [1, 2, 1, 3, 4]
K = 3 # 3
print(s.subarraysWithKDistinct(A,K))

