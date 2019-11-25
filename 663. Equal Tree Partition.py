# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkEqualTree(self, root):
        if not root:
            raise ValueError('not valid input')
        total_sum = self.sum_up(root)

        return self.dfs(root, total_sum).has_edge

    def sum_up(self, root):
        if not root.left and not root.right:
            return root.val
        left_sum = 0 if not root.left else self.sum_up(root.left)
        right_sum = 0 if not root.right else self.sum_up(root.right)
        res = root.val + left_sum + right_sum
        return res

    def dfs(self, root, root_sum):
        if not root.left and not root.right:
            return Result(False, root.val)
        left_res = Result(False, 0) if not root.left else self.dfs(root.left, root_sum)
        right_res = Result(False, 0) if not root.right else self.dfs(root.right, root_sum)
        sum_until_now = left_res.sum_until_now + right_res.sum_until_now + root.val
        has_edge = left_res.has_edge \
                   or right_res.has_edge \
                   or (root.left  is not None and root_sum == 2 * left_res.sum_until_now) \
                   or (root.right is not None and root_sum == 2 * right_res.sum_until_now)
        return Result(has_edge, sum_until_now)

class Result:
    def __init__(self, has_edge, sum_until_now):
        self.has_edge = has_edge
        self.sum_until_now = sum_until_now

###################

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        if not root:
            raise ValueError('not valid input')
        total_sum = self.sum_up(root)

        return self.dfs(root, total_sum).has_edge

    def sum_up(self, root):
        if not root:
            return 0
        left_sum = self.sum_up(root.left)
        right_sum = self.sum_up(root.right)
        res = root.val + left_sum + right_sum
        return res

    def dfs(self, root, root_sum):
        if not root:
            return Result(False, 0)
        left_res = self.dfs(root.left, root_sum)
        right_res = self.dfs(root.right, root_sum)
        sum_until_now = left_res.sum_until_now + right_res.sum_until_now + root.val
        has_edge = left_res.has_edge \
                   or right_res.has_edge \
                   or (root.left  is not None and root_sum == 2 * left_res.sum_until_now) \
                   or (root.right is not None and root_sum == 2 * right_res.sum_until_now)
        return Result(has_edge, sum_until_now)



class Result:
    def __init__(self, has_edge, sum_until_now):
        self.has_edge = has_edge
        self.sum_until_now = sum_until_now

##################
# 16 叉


import random


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 16


class Result:
    def __init__(self, has_edge, sum_until_now):
        self.has_edge = has_edge
        self.sum_until_now = sum_until_now


class Solution3:
    def checkEqualTree(self, root: TreeNode) -> bool:
        if not root:
            raise ValueError('not valid input')
        new_root = self.copy_tree(root)
        total_sum = self.sum_up(new_root)

        return self.dfs(new_root, total_sum).has_edge

    def sum_up(self, root):
        if not root:
            return 0
        sum_up = 0
        for child in root.children:
            sum_up += self.sum_up(child)
        return root.val + sum_up

    def dfs(self, root, root_sum):
        if not root:
            return Result(False, 0)
        sum_until_now = 0
        has_edge = False
        for child in root.children:
            child_res = self.dfs(child, root_sum)
            sum_until_now += child_res.sum_until_now
            has_edge = has_edge or child_res.has_edge or (
                        child is not None and root_sum == 2 * child_res.sum_until_now)

        sum_until_now += root.val

        return Result(has_edge, sum_until_now)

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


P = TreeNode(5)
P.left = TreeNode(10)
P.right = TreeNode(10)
P.right.left = TreeNode(2)
P.right.right = TreeNode(3)

Q = TreeNode(0)
Q.left = TreeNode(-1)
Q.right = TreeNode(1)

T = TreeNode(-1)
T.left = TreeNode(1)
s = Solution3()
print(s.checkEqualTree(T))
