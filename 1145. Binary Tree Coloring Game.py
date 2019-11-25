# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        cur = self.search_node(root, x)
        if cur.left:
            left = self.count_node(cur.left)
        else:
            left = 0
        if cur.right:
            right = self.count_node(cur.right)
        else:
            right = 0
        parent = n - left - right - 1
        maxi = max(left, right, parent)
        return maxi > (n - maxi)

    def search_node(self, root, x):
        if root.val == x:
            return root
        if not root:
            return None
        if root.left:
            left = self.search_node(root.left, x)
            if left:
                return left
        if root.right:
            right = self.search_node(root.right, x)
            if right:
                return right
        return None

    def count_node(self, node):
        if node.left is None and node.right is None:
            return 1
        left = self.count_node(node.left)
        right = self.count_node(node.right)
        return left + right + 1

x = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.left.left.left = TreeNode(8)
p.left.left.right = TreeNode(9)
p.left.right.left = TreeNode(10)
p.left.right.right = TreeNode(11)
p.right.left = TreeNode(6)
p.right.right = TreeNode(7)

print(x.btreeGameWinningMove(p, 11, 3))
