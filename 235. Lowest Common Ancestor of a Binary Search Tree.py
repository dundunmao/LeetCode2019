# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p == root or q == root:
            return root
        mini = min(p.val,q.val)
        maxi = max(p.val,q.val)
        if root.val > maxi:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < mini:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if p.val < q.val:
            small = p
            big = q
        else:
            small = q
            big = p
        return self.helper(root, small, big)

    def helper(self, root, small, big):
        if root is None:
            return None
        if root.val == small.val or root.val == big.val:
            return root
        if root.val < small.val:
            return self.helper(root.right, small, big)
        elif root.val > big.val:
            return self.helper(root.left, small, big)
        else:
            return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if p.val < q.val:
            small = p
            big = q
        else:
            small = q
            big = p
        while root:
            if root.val > big.val:
                root = root.left
            elif root.val < small.val:
                root = root.right
            # elif root.val < big.val and root.val > small.val
            else:
                return root
