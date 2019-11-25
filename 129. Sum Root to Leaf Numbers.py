# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_up = SumWrapper()
        path = []
        self.dfs(root, sum_up, path)
        return sum_up.sum

    def dfs(self, root, sum_up, path):
        path.append(str(root.val))
        if not root.left and not root.right and path:
            sum_up.sum += int(''.join(path))
        if root.left:
            self.dfs(root.left, sum_up, path)
        if root.right:
            self.dfs(root.right, sum_up, path)
        path.pop()


class SumWrapper:
    def __init__(self):
        self.sum = 0


#####16叉树

import random


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.chlidren = [None] * 16


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_up = SumWrapper()
        path = []
        new_root = self.copy_tree(root)
        self.dfs(new_root, sum_up, path)
        return sum_up.sum

    def dfs(self, root, sum_up, path):
        path.append(str(root.val))
        if not any(root.chlidren) and path:
            sum_up.sum += int(''.join(path))
        for child in root.chlidren:
            if child:
                self.dfs(child, sum_up, path)

        path.pop()

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.chlidren[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.chlidren[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


class SumWrapper:
    def __init__(self):
        self.sum = 0

p = TreeNode(1)
p.left = TreeNode(2)
# p.left.left = TreeNode(1)
# p.left.right = TreeNode(3)
p.right = TreeNode(3)
# p.right.left = TreeNode(0)
# p.right.right = TreeNode(2)

s = Solution()
print(s.sumNumbers(p))
