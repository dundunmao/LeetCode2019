import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        char_to_freq = {}
        for ele in S:
            if ele in char_to_freq:
                char_to_freq[ele] += 1
            else:
                char_to_freq[ele] = 1
        heap = []
        for char, freq in char_to_freq.items():
            heapq.heappush(heap, Node(char, freq))
        res = []
        while len(heap) > 0:
            temp_array = []
            for i in range(2):
                cur = heapq.heappop(heap)
                res.append(cur.char)
                if cur.freq > 1:
                    cur.freq -= 1
                    temp_array.append(cur)
                if len(heap) == 0:
                    if i != 1 and len(S) != len(res):
                        return ''
                    break
            for ele in temp_array:
                heapq.heappush(heap, ele)
        return ''.join(res)


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(a, b):
        if a.freq == b.freq:
            return a.char < b.char
        return a.freq > b.freq


class Solution1(object):
    def reorganizeString(self, S):
        n = len(S)
        A = []
        char_to_freq = {}
        for ele in S:
            if ele in char_to_freq:
                char_to_freq[ele] += 1
            else:
                char_to_freq[ele] = 1
        for char, freq in char_to_freq.items():
            A.append(Node(char, freq))
        ans = [''] * n
        pos = 0
        for node in A:
            count = node.freq
            char = node.char
            if count > (n + 1) // 2:
                return ''
            for i in range(count):
                if pos >= n:
                    pos = 0
                ans[pos] = char
                pos += 2
        return ''.join(ans)


s = Solution1()
a = "aaabbc"
print(s.reorganizeString(a))
