# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

#解题： For every node, length of longest path which pass it = MaxDepth of its left subtree + MaxDepth of its right subtree.
# 所以就是走一遍求maxdepth,边走边更新self.max.最后return的就是self.max
class Solution(object):
    def __init__(self):
        self.maxi = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.MaxDepth(root)
        return self.maxi

    def MaxDepth(self, root):  # 不用考虑root = None,因为底下已经考虑了如果左枝或右枝是空就不往那走
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            right = self.MaxDepth(root.right)
            self.maxi = max(self.maxi, right + 1)
            return right + 1
        elif root.right is None:
            left = self.MaxDepth(root.left)
            self.maxi = max(self.maxi, left + 1)
            return left + 1
        else:
            left = self.MaxDepth(root.right)
            right = self.MaxDepth(root.left)
            self.maxi = max(self.maxi, left + right + 2)
            return max(left, right) + 1

# 或者简化点写，不用判断有没有左右node,如果没有就return -1，这样后面"+2"其实就是"+1"
class Solution(object):
    def __init__(self):
        self.maxi = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.MaxDepth(root)
        return self.maxi

    def MaxDepth(self, root):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return 0
        left = self.MaxDepth(root.right)
        right = self.MaxDepth(root.left)
        self.maxi = max(self.maxi, left + right + 2)
        return max(left, right) + 1
############################
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).max_diameter

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            return Result(0, 0)
        # general case
        left_res = Result(-1, 0) if not root.left else self.dfs(root.left)
        right_res = Result(-1, 0) if not root.right else self.dfs(root.right)
        to_root_diameter = max(left_res.to_root_diameter, right_res.to_root_diameter) + 1
        max_diameter = max(left_res.max_diameter,
                           right_res.max_diameter,
                           left_res.to_root_diameter + right_res.to_root_diameter + 2)
        return Result(to_root_diameter, max_diameter)


class Result:
    def __init__(self, to_root_diameter, max_diameter):
        self.to_root_diameter = to_root_diameter
        self.max_diameter = max_diameter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).max_diameter

    def dfs(self, root):
        # base case
        if not root:
            return Result(-1, 0)
        # general case
        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)

        to_root_diameter = max(left_res.to_root_diameter, right_res.to_root_diameter) + 1
        max_diameter = max(left_res.max_diameter,
                           right_res.max_diameter,
                           left_res.to_root_diameter + right_res.to_root_diameter + 2)

        return Result(to_root_diameter, max_diameter)


class Result:
    def __init__(self, to_root_diameter, max_diameter):
        self.to_root_diameter = to_root_diameter
        self.max_diameter = max_diameter
