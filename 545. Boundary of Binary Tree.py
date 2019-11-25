# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res.append(root.val)
        if root.left:
            self.find_left(root.left, res)
        if root.left or root.right: #如果只有一个node，会把这个node重复加
            self.find_leaves(root, res)
        right_array = []
        if root.right:
            self.find_right(root.right, right_array)
        right_array.reverse() #记得要反过来
        return res + right_array

    def find_leaves(self, root, res):
        if not root.left and not root.right:
            res.append(root.val)
            return
        if root.left:
            self.find_leaves(root.left, res)
        if root.right:
            self.find_leaves(root.right, res)

    def find_left(self, root, res):
        if not root:
            return
        if not(not root.left and not root.right):
            res.append(root.val)
        if root.left:
            self.find_left(root.left, res)
        else:
            self.find_left(root.right, res)

    def find_right(self, root, right_array):
        if not root:
            return
        if not(not root.left and not root.right):
            right_array.append(root.val)
        if root.right:
            self.find_right(root.right, right_array)
        else:
            self.find_right(root.left, right_array)
