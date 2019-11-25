# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def __init__(self):
        self.target = None

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        parent_hash = {}
        self.dfs(root, None, k, parent_hash)
        visited = set()
        return self.bfs(parent_hash, visited)
    # 边找target那个node，边用parent_hash简历node->parent 关系
    def dfs(self, node, parent, k, parent_hash):
        if node.val == k:
            self.target = node
        if node not in parent_hash and parent:
            parent_hash[node] = parent
        if not node.left and not node.right:
            return
        parent = node
        if node.left:
            self.dfs(node.left, node, k, parent_hash)
        if node.right:
            self.dfs(node.right, node, k, parent_hash)
    # 从target出发，找最近的叶子
    def bfs(self, parent_hash, visited):
        q = collections.deque()
        q.append(self.target)
        visited.add(self.target)
        while q:
            cur = q.popleft()
            if not cur.right and not cur.left:
                return cur.val
            if cur.right and cur.right not in visited:
                visited.add(cur.right)
                q.append(cur.right)
            if cur.left and cur.left not in visited:
                visited.add(cur.left)
                q.append(cur.left)
            if cur in parent_hash and parent_hash[cur] not in visited:
                visited.add(parent_hash[cur])
                q.append(parent_hash[cur])
