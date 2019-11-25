# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         if root is None:
#             return 0
#         return self.f(root, L, R)
#
#     def f(self, root, L, R):
#         if not root:
#             return 0
#         sum_left = 0 if root.val < L else self.f(root.left, L, R)
#         sum_right = 0 if root.val > R else self.f(root.right, L, R)
#         node_val = root.val if root.val >= L and root.val <= R else 0
#         return sum_left + sum_right + node_val
#
#
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         if root is None:
#             return 0
#         return self.f(root, L, R)
#
#     def f(self, root, L, R):
#         if not root:
#             return 0
#         if root.val < L:
#             return self.f(root.right, L, R)
#         if root.val > R:
#             return self.f(root.left, L, R)
#         sum_left = self.f(root.left, L, R)
#         sum_right = self.f(root.right, L, R)
#         node_val = root.val
#         return sum_left + sum_right + node_val
#
#
#
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         if root is None:
#             return 0
#         return self.f(root, L, R)
#
#     def f(self, root, L, R):
#         if not root:
#             return 0
#         sum_left = self.f(root.left, L, R)
#         sum_right = self.f(root.right, L, R)
#         node_val = root.val if root.val <= R and root.val >= L else 0
#         return sum_left + sum_right + node_val
#

def x(n):
    res = ''
    pre = (n - 1) // 702 + 1
    if pre > 1:
        n = n - (702 * (pre-1))
    while n:
        mod = (n - 1) % 26
        res += chr(mod + 65)
        n = (n - 1) // 26
    return str(pre) + res[::-1]
s = 721
print(x(s))
