# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).max_profit

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            return Result(root.val, 0)
        # general case
        left_res = Result(0, 0) if not root.left else self.dfs(root.left)
        right_res = Result(0, 0) if not root.right else self.dfs(root.right)

        max_profit_without_root = left_res.max_profit + right_res.max_profit
        max_profit = max(max_profit_without_root,
                         root.val + left_res.max_profit_without_root + right_res.max_profit_without_root
                     )

        return Result(max_profit, max_profit_without_root)

class Result:
    def __init__(self, max_profit, max_profit_without_root):
        self.max_profit = max_profit
        self.max_profit_without_root = max_profit_without_root
##############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).max_profit

    def dfs(self, root):
        # base case
        if not root:
            return Result(0, 0)
        # general case
        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)

        max_profit_without_root = left_res.max_profit + right_res.max_profit
        max_profit = max(max_profit_without_root,
                         root.val + left_res.max_profit_without_root + right_res.max_profit_without_root
                         )
        return Result(max_profit, max_profit_without_root)


class Result:
    def __init__(self, max_profit, max_profit_without_root):
        self.max_profit = max_profit
        self.max_profit_without_root = max_profit_without_root



#########################
# 16 叉

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


class Result:
    def __init__(self, max_profit, max_profit_without_root):
        self.max_profit = max_profit
        self.max_profit_without_root = max_profit_without_root


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        new_root = self.copy_tree(root)
        return self.dfs(new_root).max_profit

    def dfs(self, root):
        # base case
        if not root:
            return Result(0, 0)
        # general case
        child_max_profit_without_root_sum = 0
        child_max_profit_sum = 0
        for child in root.children:
            child_res = self.dfs(child)
            child_max_profit_without_root_sum += child_res.max_profit_without_root
            child_max_profit_sum += child_res.max_profit
        max_profit = max(child_max_profit_sum, root.val + child_max_profit_without_root_sum)
        max_profit_without_root = child_max_profit_sum
        return Result(max_profit, max_profit_without_root)

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root
