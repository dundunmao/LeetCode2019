# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的距离。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵如下的二叉树:
#
#   1
#  / \
# 2   3
#    / \
#   4   5
# 这个二叉树的最大深度为3.
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # traverse
    def __init__(self):
        self.result = 0
    def maxDepth(self, root):
        self.traverse(root,1)
        return self.result
    def traverse(self, root, depth):
        if root is None:
            return
        if depth > self.result:
            self.result = depth
        if root.left:
            self.traverse(root.left, depth+1)
        if root.right:
            self.traverse(root.right, depth+1)

    # divide&conquer
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1


class Solution1:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        result = [0]       #不想用class variable时,就把result变成一个array,只对array里的第一个数做变化,result不能是int,因为into是值传递,array是reference传递.
        self.traverse(root, 1, result)
        return result[0]

    def traverse(self, root, depth, result):
        if root is None:
            return
        result[0] = max(result[0], depth)
        if root.left:
            self.traverse(root.left, depth + 1, result)
        if root.right:
            self.traverse(root.right, depth + 1, result)

class Solution3:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # traverse
    def __init__(self):
        self.result = 0
        self.path = []
    def maxDepth(self, root):
        p = []
        self.traverse(root,1,p)
        return self.result,self.path
    def traverse(self, root, depth,p):
        if root is None:
            return
        p.append(root)
        if depth > self.result:
            self.result = depth
            self.path = p[:]
        if root.left:
            self.traverse(root.left, depth+1, p)
        if root.right:
            self.traverse(root.right, depth+1, p)
        p.pop()

class Solution4:

    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return self.helper(root)

    def helper(self,root):
        if root is None:
            return 0,[]
        [left,l_path] = self.helper(root.left)
        [right,r_path] = self.helper(root.right)
        p = [root]
        if not p:
            print("********")
        if left > right:
            if l_path:
                return [left+1, p+l_path]
            else:
                return [left, p]
        else:
            if r_path:
                return [right+1, p+r_path]
            else:
                return [right, p]



import random
class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 16


class Solution6:
    def maxDepth(self, root: TreeNode) -> int:
        new_root = self.copy_tree(root)
        if not new_root:
            return 0
        return self.f(new_root)

    def f(self, root):
        if not root:
            return 0
        res = 0
        for child in root.children:
            child_max_depth = self.f(child)
            res = max(res, child_max_depth)
        return res + 1

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \
    #  4      5
    #        / \
    #       6   7
    #            \
    #             8
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(5)
    P.left.right.left = TreeNode(6)
    P.left.right.right = TreeNode(7)
    P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution6()
    print(s.maxDepth(P))
