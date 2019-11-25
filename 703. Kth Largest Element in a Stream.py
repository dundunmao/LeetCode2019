import heapq
class KthLargest:

    def __init__(self, k, nums):
        self.top_k_min_heap = []
        self.size = k
        i = 0
        while i < len(nums) and k > 0:
            heapq.heappush(self.top_k_min_heap, nums[i])
            i += 1
            k -= 1
        while i < len(nums):
            if self.top_k_min_heap[0] < nums[i]:
                heapq.heappop(self.top_k_min_heap)
                heapq.heappush(self.top_k_min_heap, nums[i])
            i += 1

    def add(self, val: int) -> int:
        if len(self.top_k_min_heap) < self.size:
            heapq.heappush(self.top_k_min_heap, val)
        elif self.top_k_min_heap[0] < val:
            heapq.heappop(self.top_k_min_heap)
            heapq.heappush(self.top_k_min_heap, val)
        return self.top_k_min_heap[0]

    # Your KthLargest object will be instantiated and called as such:
k = 3
nums = [5, -1]
obj = KthLargest(k, nums)
print(obj.add(2))
print(obj.add(1))
print(obj.add(-1))
print(obj.add(3))
print(obj.add(4))


