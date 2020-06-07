# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = float('inf')

    def findSecondMinimumValue(self, root: TreeNode) -> int:

        self.dfs(root, root)

        return self.ans if self.ans != float('inf') else -1

    def dfs(self, node, root):
        if node:
            if root.val < node.val < self.ans:
                self.ans = node.val
            else:
                self.dfs(node.left, root)
                self.dfs(node.right, root)
