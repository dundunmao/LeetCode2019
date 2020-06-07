# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        """
        :param head:
        :param root:
        :return:
        """
        # start from one certain point
        def _is_sub_path(list_node, tree_node):
            if list_node is None:
                return True
            if tree_node is None:
                return False
            if list_node.val == tree_node.val:
                return _is_sub_path(list_node.next, tree_node.left) or _is_sub_path(list_node.next, tree_node.right)
            return False

        # start from all nodes
        if not head or not root:
            return False
        if _is_sub_path(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)