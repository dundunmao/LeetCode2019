# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = None
        queue = collections.deque()
        queue.append(root)
        while len(queue):
            size = len(queue)
            for i in range(size):
                res = queue.popleft()
                if res.right:
                    queue.append(res.right)
                if res.left:
                    queue.append(res.left)
        return res.val
