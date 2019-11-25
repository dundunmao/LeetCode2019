# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        smallest_path = StringWrapper()
        path = []
        self.dfs(root, smallest_path, path)
        return smallest_path.string

    def dfs(self, root, smallest_path, path):
        path.append(chr(root.val + 97))
        # base case
        if not root.left and not root.right:
            temp = ''.join(path[::-1]) # 不能用path.reverse(),是inplace的，返回None
            if not smallest_path.string or smallest_path.string > temp:
                smallest_path.string = temp

        # general case
        if root.left:
            self.dfs(root.left, smallest_path, path)
        if root.right:
            self.dfs(root.right, smallest_path, path)
        path.pop()



############ 16 叉树

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
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        smallest_path = StringWrapper()
        path = []
        new_root = self.copy_tree(root)
        self.dfs(new_root, smallest_path, path)
        return smallest_path.string

    def dfs(self, root, smallest_path, path):
        path.append(chr(root.val + 97))
        # base case
        if not any(root.chlidren):
            temp = ''.join(path[::-1])  # 不能用path.reverse(),是inplace的，返回None
            if not smallest_path.string or smallest_path.string > temp:
                smallest_path.string = temp

        # general case
        for child in root.chlidren:
            if child:
                self.dfs(child, smallest_path, path)
        path.pop()

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.chlidren[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.chlidren[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root

class StringWrapper:
    def __init__(self):
        self.string = ''




p = TreeNode(25)
p.left = TreeNode(1)
p.left.left = TreeNode(1)
p.left.right = TreeNode(3)
p.right = TreeNode(3)
p.right.left = TreeNode(0)
p.right.right = TreeNode(2)

s = Solution()
print(s.smallestFromLeaf(p))
