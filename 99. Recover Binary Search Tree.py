# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = Result()
        self.dfs(root, result)
        temp = result.first.val
        result.first.val = result.second.val
        result.second.val = temp

    def dfs(self, root, result):
        if not root:
            return
        self.dfs(root.left, result)

        if not result.first and result.pre.val >= root.val:
            result.first = result.pre
        if result.first and result.pre.val >= root.val:
            result.second = root
        result.pre = root
        self.dfs(root.right, result)

class Result:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = TreeNode(float('-inf'))
