# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_up = float('-inf')
        res = 0
        queue = collections.deque()
        queue.append(root)
        level = 1
        while len(queue) > 0:
            size = len(queue)
            level_sum = 0
            for i in range(size):
                cur = queue.popleft()
                level_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # print(level_sum)
            if level_sum > sum_up:
                res = level
                sum_up = level_sum

            level += 1
        return res
