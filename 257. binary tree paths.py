class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path = []
        res = []
        self.dfs(root, path, res)
        return res

    def dfs(self, root, path, res):
        path.append(str(root.val))
        # base case
        if not root.left and not root.right:
            res.append(''.join(path))
        # general case
        if root.left:
            path.append('->')
            self.dfs(root.left, path, res)
            path.pop()
        if root.right:
            path.append('->')
            self.dfs(root.right, path, res)
            path.pop()
        path.pop()

# 16 叉
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
            res.append(''.join(path))
        # general case
        for child in root.chlidren:
            if child:
                path.append('->')
                self.dfs(child, path, res)
                path.pop()
        path.pop()

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.chlidren[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.chlidren[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root



class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths


if __name__ == '__main__':
    # root = [10,5,-3,3,2,null,11,3,-2,null,1]
    #      10
    #     /  \
    #    5   -3
    #   / \    \
    #  3   2   11
    # / \   \
    #3  -2   1

    P = TreeNode(10)
    P.left = TreeNode(5)
    P.left.left = TreeNode(3)
    P.left.left.left = TreeNode(3)
    P.left.left.right = TreeNode(-2)
    P.left.right = TreeNode(2)
    P.left.right.right = TreeNode(1)
    P.right = TreeNode(3)
    P.right.right = TreeNode(11)
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution5()
    print(s.binaryTreePaths(P))
