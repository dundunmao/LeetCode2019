# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.f(root)[0]

    def f(self, root):
        if not root.left and not root.right:
            return 0, root.val, root.val
        left_res, left_min, left_max = [0, float('inf'), float('-inf')] if not root.left else self.f(root.left)
        right_res, right_min, right_max = [0, float('inf'), float('-inf')] if not root.right else self.f(root.right)

        root_min = min(root.val, left_min, right_min)
        root_max = max(root.val, left_max, right_max)

        res = max(abs(root.val - min(left_min, right_min)),
                  abs(max(left_max, right_max) - root.val),
                  left_res,
                  right_res)

        return res, root_min, root_max


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.f(root)[0]

    def f(self, root):
        if not root:
            return 0, float('inf'), float('-inf')
        left_res, left_min, left_max = self.f(root.left)
        right_res, right_min, right_max = self.f(root.right)

        root_min = min(root.val, left_min, right_min)
        root_max = max(root.val, left_max, right_max)

        res = max(abs(root.val - min(left_min, right_min)),
                  abs(max(left_max, right_max) - root.val),
                  left_res,
                  right_res)
        return res, root_min, root_max


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import random


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 16


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        my_root = self.copy_tree(root)
        return self.f(my_root)[0]

    def f(self, root):
        if not any(root.children):
            return 0, root.val, root.val
        res, mini, maxi = [0, float('inf'), float('-inf')]
        for child in root.children:
            child_res, child_min, child_max = [0, float('inf'), float('-inf')] if not child else self.f(child)

            mini = min(mini, child_min)
            maxi = max(maxi, child_max)
            res = max(res, child_res)

        root_min = min(root.val, mini)
        root_max = max(root.val, maxi)
        root_res = max(abs(root.val - mini), abs(maxi - root.val), res)
        return root_res, root_min, root_max

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root
