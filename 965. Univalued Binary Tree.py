class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        target = root.val
        return self.dfs(root, target)

    def dfs(self, root, target):
        if root.left == 0 and root.right == 0:
            if root.val != target:
                return False
            else:
                return True
        elif root.val != target:
            return False
        else:
            res = True
            if root.left:
                res &= self.dfs(root.left, target)
            if root.right:
                res &= self.dfs(root.right, target)

        return res
