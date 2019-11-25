import heapq
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        hash = {}
        for w in words:
            if w in hash:
                hash[w] += 1
            else:
                hash[w] = 1

        for w, freq in hash.items():
            heapq.heappush(heap, Node(freq, w))
            if len(heap) > k:
                heapq.heappop(heap)
        res = collections.deque()
        while len(heap) > 0:
            res.appendleft(heapq.heappop(heap).string)
        return res


class Node:
    def __init__(self, freq, string):
        self.freq = freq
        self.string = string

    def __lt__(a, b):
        if a.freq == b.freq:
            return a.string > b.string
        return a.freq < b.freq
