# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        return self.dfs(root)[1]
    # 当前树的 最大深度 & smallest subtree
    def dfs(self, root):
        if not root:
            return -1, None
        left_depth, left_subtree = self.dfs(root.left)
        right_depth, right_subtree = self.dfs(root.right)

        if left_depth == right_depth:
            return left_depth + 1, root

        if left_depth > right_depth:
            return left_depth + 1, left_subtree
        else:
            return right_depth + 1, right_subtree
