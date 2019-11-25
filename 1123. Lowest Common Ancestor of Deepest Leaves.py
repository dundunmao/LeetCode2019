# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        res = Result()
        self.dfs(root, 0, res)
        return res.lca
    # 返回的是当前node的左右子树的深度
    def dfs(self, node, depth, res):
        # 更新此树最大深度
        res.deepest = max(res.deepest, depth)
        if not node:
            return depth
        # 左边的最大深度
        left = self.dfs(node.left, depth + 1, res)
        # 右边的最大深度
        right = self.dfs(node.right, depth + 1, res)
        # 如果左右都到了最大深度，lca更新成当前node
        # 如到叶子了，左右深度都是这个叶子的深度，都是最大深度，记录这个叶子为lca
        # 再上一层，
        if left == res.deepest and right == res.deepest:
            res.lca = node
        return max(left, right)

class Result:
    def __init__(self):
        self.lca = None
        self.deepest = 0
