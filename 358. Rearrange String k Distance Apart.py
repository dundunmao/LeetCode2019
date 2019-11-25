import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        char_to_freq_hash = {}
        res = []
        # 找到每个字符出现的频率
        for char in s:
            if char in char_to_freq_hash:
                char_to_freq_hash[char] += 1
            else:
                char_to_freq_hash[char] = 1
        # 放heap里
        char_heap = []
        for key, val in char_to_freq_hash.items():
            heapq.heappush(char_heap, Node(key, val))
        # 每次从heap里取k个，放res里，取的k个再重新放回heap
        while len(char_heap) > 0:
            temp_array = []
            for i in range(k):
                cur = heapq.heappop(char_heap)
                res.append(cur.char)
                if cur.freq > 1:
                    cur.freq -= 1
                    temp_array.append(cur)
                if len(char_heap) == 0:
                    if i != k - 1 and len(res) != len(s):
                        return ''
                    break
            for ele in temp_array:
                heapq.heappush(char_heap, ele)
        return ''.join(res) if len(char_heap) == 0 else ''


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(a, b):
        if a.freq == b.freq:
            return a.char < b.char
        return a.freq > b.freq

x = Solution()
s = 'aabbcc'
k = 3
print(x.rearrangeString(s, k))
s = 'aaabc'
k = 2
print(x.rearrangeString(s, k))
