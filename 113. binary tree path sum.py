class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def pathSum(self, root, total):
        if not root:
            return []
        res = []
        path = []
        self.dfs(root, total, path, res)
        return res

    def dfs(self, root, total, path, res):
        path.append(root.val)
        if not root.left and not root.right and sum(path) == total:
            res.append(path[:])
        if root.left:
            self.dfs(root.left, total, path, res)
        if root.right:
            self.dfs(root.right, total, path, res)
        path.pop()


######16 叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import random


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.chlidren = [None] * 16


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# traverse
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path = []
        res = []
        new_root = self.copy_tree(root)
        self.dfs(new_root, path, res)
        return res

    def dfs(self, root, path, res):
        path.append(str(root.val))
        # base case
        if not any(root.chlidren) and path:
            res.append('->'.join(path))
        # general case
        for child in root.chlidren:
            if child:
                self.dfs(child, path, res)

        path.pop()

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.chlidren[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.chlidren[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


p = TreeNode(5)
p.left = TreeNode(4)
p.left.left = TreeNode(11)
p.left.left.right = TreeNode(2)
p.left.left.left = TreeNode(7)
# p.left.right = TreeNode(3)
p.right = TreeNode(8)
p.right.left = TreeNode(13)
p.right.right = TreeNode(4)
p.right.right.left = TreeNode(5)
p.right.right.right = TreeNode(1)

s = Solution()
print(s.pathSum(p, 22))
