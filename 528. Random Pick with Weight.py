import random


class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.sum = w

    def pickIndex(self) -> int:
        target = random.randint(1, self.sum[-1])
        return self.binary_search(target)

    def binary_search(self, target):
        start = 0
        end = len(self.sum) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.sum[mid] < target:
                start = mid
            elif self.sum[mid] > target:
                end = mid
            else:
                return mid
        if target <= self.sum[start]:
            return start
        else:
            return end

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
