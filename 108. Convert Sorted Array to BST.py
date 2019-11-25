class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        size = len(nums)
        root_index = size // 2  # 找到root
        root = TreeNode(nums[root_index])  # 生成root

        left = nums[:root_index]
        left_bst = self.sortedArrayToBST(left)  # 生成左边的bst

        right = nums[root_index + 1:]
        right_bst = self.sortedArrayToBST(right)  # 生成右边的bst

        root.left = left_bst  # 建树
        root.right = right_bst

        return root


#########
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        n = len(nums)
        return self.build_tree(nums, 0, n - 1)

    def build_tree(self, a, start, end):
        mid = start + (end - start) // 2
        root = TreeNode(a[mid])
        if start <= mid - 1:
            root.left = self.build_tree(a, start, mid - 1)
        if mid + 1 <= end:
            root.right = self.build_tree(a, mid + 1, end)
        return root

