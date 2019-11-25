# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = Result()
        self.dfs(root, target, res)
        return res.node.val

    def dfs(self, root, target, res):
        if not root:
            return
        if root.val == target:
            res.node = root
            res.distance = 0
            return
        if abs(root.val - target) < res.distance:
            res.distance = abs(root.val - target)
            res.node = root
        if root.val > target:
            self.dfs(root.left, target, res)
        elif root.val < target:
            self.dfs(root.right, target, res)


class Result:
    def __init__(self):
        self.distance = float('inf')
        self.node = None
