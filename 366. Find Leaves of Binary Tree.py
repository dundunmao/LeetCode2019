# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        max_depth = self.get_max_dep(root)
        result = [[] * depth]
        self.dfs(root, result)
        return result

    def get_max_dep(self, root):
        if not root:
            return 0
        return 1 + max(self.get_max_dep(root.left), self.get_max_dep(root.right))

    def dfs(self, node, result):
        if not node:
            return -1
        depth = 1 + max(self.dfs(node.left, result), self.dfs(node.right, result))
        result[depth].append(node.val)
        return depth

# 我的解法，不好

import collections
class Solution:
    def findLeaves(self, root: TreeNode):
        queue = collections.deque()
        queue.append(root)
        res = []
        set_node = set()
        array = self.bfs(queue, res, set_node)
        while len(array):
            array = self.get_new(array, set_node, res)
        return res

    def bfs(self, queue, res, set_node):
        array = []
        new_queue = collections.deque()
        while len(queue) > 0:

            node = queue.popleft()
            if (node.left and node.left not in set_node) or (node.right and node.right not in set_node):
                new_queue.append(node)
                if node.left and node.left not in set_node:
                    queue.append(node.left)
                if node.right and node.right not in set_node:
                    queue.append(node.right)
            else:
                array.append(node.val)
                set_node.add(node)
        res.append(array)
        return new_queue

    def get_new(self, array, set_node, res):
        new = []
        cur_array = []
        for node in array:
            if (node.left and node.left not in set_node) or (node.right and node.right not in set_node):
                new.append(node)
            else:
                cur_array.append(node.val)
                set_node.add(node)
        res.append(cur_array[:])
        return new


x = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)

print(x.findLeaves(p))
