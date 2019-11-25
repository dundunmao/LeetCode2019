class Solution:
    def kEmptySlots(self, bulbs, k: int) -> int:
        days = [0 for i in range(len(bulbs))]
        for day, pos in enumerate(bulbs, 1):
            days[pos - 1] = day

        res = float('inf')
        left = 0
        right = k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = i + k + 1
                    break
            else:
                res = min(res, max(days[left], days[right]))
                left, right = right, right + k + 1
        return res if res < float('inf') else -1
s = Solution()
a = [1,2,3,4,5,7,6]
k = 1
print(s.kEmptySlots(a,k))
