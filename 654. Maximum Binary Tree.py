# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        node_stack = []
        for num in nums:
            cur = TreeNode(num)
            # 大的要进栈，pop出前面小的都放left
            while len(node_stack) > 0 and node_stack[-1].val < num:
                cur.left = node_stack.pop()
            # 要进栈的要接到 栈顶 的right
            if len(node_stack) > 0:
                node_stack[-1].right = cur
            # 入栈
            node_stack.append(cur)
        return node_stack[0]


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, start, end):
        if start == end:
            return TreeNode(nums[start])
        root_val = max(nums[start: end + 1])
        root_index = nums.index(root_val)
        root = TreeNode(root_val)
        if start < root_index:
            left_tree = self.dfs(nums, start, root_index - 1)
            root.left = left_tree
        if root_index < end:
            right_tree = self.dfs(nums, root_index + 1, end)
            root.right = right_tree
        return root
