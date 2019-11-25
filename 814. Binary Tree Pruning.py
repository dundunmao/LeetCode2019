# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        if not root:
            return False
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root.left and not root.right:
            if root.val == 0:
                return True
            else:
                return False
        left_res = True if not root.left else self.dfs(root.left)
        right_res = True if not root.right else self.dfs(root.right)

        if left_res:
            root.left = None
        if right_res:
            root.right = None

        if left_res and right_res and root.val == 0:
            return True

        return False


class Solution:
    def pruneTree(self, root):
        if not root:
            return False
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return True

        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)

        if left_res:
            root.left = None
        if right_res:
            root.right = None

        if left_res and right_res and root.val == 0:
            return True

        return False
