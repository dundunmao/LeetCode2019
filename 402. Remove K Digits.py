import collections

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)
        if n == k:
            return '0'
        res_deque = collections.deque()
        # 保持增序，遇到将pop，直至pop k 个
        for i in range(n):
            while len(res_deque) > 0 and res_deque[-1] > nums[i] and k > 0:
                res_deque.pop()
                k -= 1
            res_deque.append(nums[i])
        # 如果k没用完，从后面减去剩下的
        while k != 0:
            k -= 1
            res_deque.pop()
        res = []
        while len(res_deque) and res_deque[0] == '0':
            res_deque.popleft()
        if len(res_deque) == 0:
            return '0'
        else:
            return ''.join(res_deque)

s = Solution()
s.removeKdigits('10', 1)
