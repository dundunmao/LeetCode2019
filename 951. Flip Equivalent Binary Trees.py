class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        return self.dfs(root1, root2)

    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif root1 and not root2:
            return False
        elif not root1.left and not root1.right and not root2.left and not root2.right:
            return root1.val == root2.val
        elif root1.val == root2.val and \
                (   (self.dfs(root1.left, root2.left) and self.dfs(root1.right, root2.right))
                 or (self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left))):
            return True
        else:
            return False

