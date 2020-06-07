"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        else:
            while node.parent and node.parent.right == node:
                node = node.parent
            return node.parent
