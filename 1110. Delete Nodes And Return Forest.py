# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []
        remaining_array = collections.deque()
        remaining_array.append(root)
        to_delete_set = set(to_delete)
        while remaining_array:
            node = remaining_array.popleft()
            if node.val not in to_delete_set:
                res.append(node)
            if len(to_delete_set) > 0:
                self.dfs(node, None, '', to_delete_set, res, remaining_array)
        return res

    def dfs(self, node, pre, direction, to_delete_set, res, remaining_array):
        if node.val in to_delete_set:
            if node.left:
                # res.append(node.left)
                print(node.left.val)
                remaining_array.append(node.left)
            if node.right:
                # res.append(node.right)
                remaining_array.append(node.right)
                print(node.right.val)
            to_delete_set.remove(node.val)
            if pre != None:
                if direction == 'left':
                    pre.left = None
                else:
                    pre.right = None
        elif len(to_delete_set):
            if node.left:
                self.dfs(node.left, node, 'left', to_delete_set, res, remaining_array)
            if node.right:
                self.dfs(node.right, node, 'right', to_delete_set, res, remaining_array)
a = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(4)
p.left.right = TreeNode(3)
b = [2,3]
print(a.delNodes(p, b))
