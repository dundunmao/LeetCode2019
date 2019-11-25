# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        dummy = TreeNode(-1)
        dummy.left = root
        self.dfs(root)
        return dummy.left

    def dfs(self, root):
        if not root.left and not root.right:
            return root
        right_leaf = self.dfs(root.left)
        right_leaf.left = root.right
        right_leaf.right = root
        return root

class Solution1(object):
    def upsideDownBinaryTree(self, root):
        cur = root
        next = None
        temp = None
        pre = None
        while cur != None:
            next = cur.left

            cur.left = temp
            temp = cur.right
            cur.right = pre

            pre = cur
            cur = next
        return pre
