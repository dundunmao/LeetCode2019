from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        return self.dfs(pre, post)

    def dfs(self, pre, post):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left_root = pre[1]
        right_root = post[-2]
        if left_root == right_root:  # mean only left or right
            root.left = self.dfs(pre[1:], post[:-1])
            return root
        else:
            left_end_index = pre.index(right_root)
            right_start_index = post.index(left_root)
            root.left = self.dfs(pre[1:left_end_index], post[:right_start_index + 1])
            root.right = self.dfs(pre[left_end_index:], post[(right_start_index + 1):-1])
            return root
s = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
print(s.constructFromPrePost(pre, post))
