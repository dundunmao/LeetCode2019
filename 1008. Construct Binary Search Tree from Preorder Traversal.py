# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        first_lower_index = self.daily_temperatures(preorder)
        return self.build_tree(preorder, 0, len(preorder) - 1, first_lower_index)

    def build_tree(self, preorder, start, end, first_lower_index):
        root = TreeNode(preorder[start])
        right_start = first_lower_index[start]
        if start + 1 < right_start:
            root.left = self.build_tree(preorder, start + 1, right_start - 1, first_lower_index)
        if right_start <= end:
            root.right = self.build_tree(preorder, right_start, end, first_lower_index)
        return root

# 找到preorder里每个点的第一个比它大的点
    def daily_temperatures(self, T):
        size = len(T)
        res = [size] * size
        unresolved_index_stack = []
        for i in range(size):
            while len(unresolved_index_stack) and T[unresolved_index_stack[-1]] < T[i]:
                index = unresolved_index_stack.pop()
                res[index] = i
            unresolved_index_stack.append(i)
        return res

s = Solution()
a = [8,5,1,7,10,12]
print(s.bstFromPreorder(a))
