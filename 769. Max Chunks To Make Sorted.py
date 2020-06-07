class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        maxi = 0
        for i, x in enumerate(arr):
            maxi = max(maxi, x)
            if maxi == i:
                ans += 1
        return ans
