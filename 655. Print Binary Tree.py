class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        height = self.height(root)
        w = 2 ** height - 1
        res = [[[""] for i in range(w)] for j in range(height)]

        self.dfs(root, 0, 0, w - 1, res)
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.left)) + 1
    def dfs(self, root, height, left, right, res):
        if not root:
            return
        mid = (left + right) // 2
        res[height][mid] = str(root.val)
        # if root.left:
        self.dfs(root.left, height + 1, left, mid - 1, res)
        self.dfs(root.right, height + 1, mid + 1, right, res)
