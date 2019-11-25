# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor in the tree, return null.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        last_root = None
        while root != None and root.val != p.val:
            if root.val > p.val:
                last_root = root   #只有往左子树走的时候,才把这个root记录着(因为当某个点无右子树时,他的下一个点是他的上一层,就是这个root),把左子树都走完了前一直是这个root
                root = root.left
            else:
                root = root.right
        #遍历到最底层还没找到
        if root is None:
            return None
         #找到了，这个node右子树空，那他的下一个点就是他上层那个root
        if root.right is None:
            if last_root:
                return last_root.val
            else:
                return None
         #如果有右子树，要找这个右子树的最小点
        root = root.right
        while root.left != None:
            root = root.left
        return root.val


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        last_root = None
        while root and root.val != p.val:
            if root.val < p.val:

                root = root.right
            else:
                last_root = root
                root = root.left
        if not root:
            return None
        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root
        else:
            return last_root
