# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # dfs--find path from root to targe
        root_to_target = []
        path = []
        self.dfs(root, target, root_to_target, path)
        # bfs - find results
        results = []
        # find target 孩子方向的result
        self.bfs(target, K, results)
        # find target 父亲方向的result
        for dist in range(1, K + 1):
            if len(root_to_target) - 1 - dist < 0:
                break
            node = root_to_target[len(root_to_target) - 1 - dist]
            prev_child = root_to_target[len(root_to_target) - dist]

            # 保存 prev child
            left = node.left
            right = node.right
            # 断开prev child
            if prev_child == left:
                node.left = None
            if prev_child == right:
                node.right = None

            self.bfs(node, K - dist, results)

            # 重连prev child
            node.left = left
            node.right = right
        return results

    def dfs(self, node, target, root_to_target, path):
        path.append(node)

        if node == target:
            root_to_target += path[:]
            return
        if node.left:
            self.dfs(node.left, target, root_to_target, path)
        if node.right:
            self.dfs(node.right, target, root_to_target, path)

        path.pop()

    def bfs(self, root, level, results):
        deque = collections.deque()
        deque.append(root)
        depth = 0
        while len(deque):
            size = len(deque)
            for i in range(size):
                cur = deque.popleft()
                if depth == level:
                    results.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)

            if depth == level:
                return
            depth += 1


class Solution:
    def distanceK(self, root, target, K):
        node_to_parent_hash = {}
        # get node_to_parent relationship
        self.dfs(root, None, node_to_parent_hash)

        # from node to k step to 3 direction
        res = []
        visited = set()
        self.to_k_steps(target, K, node_to_parent_hash, res, visited)
        return res

    def dfs(self, node, parent, node_to_parent_hash):
        if not node:
            return
        node_to_parent_hash[node] = parent
        self.dfs(node.left, node, node_to_parent_hash)
        self.dfs(node.right, node, node_to_parent_hash)

    def to_k_steps(self, node, k, node_to_parent_hash, res, visited):
        if not node:
            return
        if node in visited:
            return
        # 找到了，加进去
        if k == 0:
            res.append(node.val)

        visited.add(node) #为了防止duplicate，这样保证走过的不会再走

        self.to_k_steps(node.left, k - 1, node_to_parent_hash, res, visited)
        self.to_k_steps(node.right, k - 1, node_to_parent_hash, res, visited)
        self.to_k_steps(node_to_parent_hash[node], k - 1, node_to_parent_hash, res, visited)




