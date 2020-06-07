import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
s = Solution()
a = [17,13,11,2,3,5,7]
print(s.deckRevealedIncreasing(a))
a = [1,2,3,4,5,6,7,8,9,10]
print(s.deckRevealedIncreasing(a))
