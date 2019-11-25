import heapq
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        multi_min_heap = []
        for i in range(m):
            ele = MultiEle(i + 1, i, 0)
            heapq.heappush(multi_min_heap, ele)
        # res = []
        while len(multi_min_heap):
            cur = heapq.heappop(multi_min_heap)
            # res.append(cur.val)
            if k == 1:
                return cur.val
            if cur.y + 1 < n:
                next = MultiEle((cur.x + 1) * (cur.y + 2), cur.x, cur.y + 1)
                heapq.heappush(multi_min_heap, next)
            k -= 1
        return -1


class MultiEle:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def __lt__(a, b):
        return a.val < b.val


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo = 1
        hi = m * n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not self.enough(mid, m, n, k):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def enough(self, x, m, n, k):
        count = 0
        for i in range(1, m + 1):
            count += min(x // i, n)
        return count >= k
m = 3
n = 3
k = 5
x = Solution()
print(x.findKthNumber(m, n, k))

