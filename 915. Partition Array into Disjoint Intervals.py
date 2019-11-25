from collections import deque


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        # 从左最大
        maxi = float('-inf')
        maxi_left = deque()
        for ele in A:
            maxi = max(maxi, ele)
            maxi_left.append(maxi)
        # 从右最小
        mini = float('inf')
        mini_right = deque()
        for i in range(len(A) - 1, -1, -1):
            mini = min(mini, A[i])
            mini_right.appendleft(mini)
        # 挨个比较
        for i in range(1, len(A)):
            if maxi_left[i - 1] <= mini_right[i]:
                return i
        return -1


