"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        head, tail = self.helper(root)
        return head

    def helper(self, root):
        '''construct a doubly-linked list, return the head and tail'''
        head, tail = root, root
        if root.left:
            left_head, left_tail = self.helper(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
        if root.right:
            right_head, right_tail = self.helper(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail

        head.left = tail
        tail.right = head
        return head, tail

###################################
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None  # pre
        self.right = None  # next

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        res = self.dfs(root)
        res.head.left = res.tail
        res.tail.right = res.head
        return res.head

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            res = NodeWrapper(root, root)
            return res
        # general case
        if root.left:
            left_wrapper = self.dfs(root.left)
            left_wrapper.tail.right = root
            root.left = left_wrapper.tail
        else:
            left_wrapper = NodeWrapper(None, None)
        if root.right:
            right_wrapper = self.dfs(root.right)
            right_wrapper.head.left = root
            root.right = right_wrapper.head
        else:
            right_wrapper = NodeWrapper(None, None)
        head = left_wrapper.head if left_wrapper.head else root
        tail = right_wrapper.tail if right_wrapper.tail else root
        return NodeWrapper(head, tail)

class NodeWrapper:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

######简化base case

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        res = self.dfs(root)
        res.head.left = res.tail
        res.tail.right = res.head
        return res.head

    def dfs(self, root):
        # base case
        if not root:
            return NodeWrapper(None, None)
        # general case
        left_wrapper = self.dfs(root.left)
        right_wrapper = self.dfs(root.right)

        if left_wrapper.tail:
            left_wrapper.tail.right = root
            root.left = left_wrapper.tail
        if right_wrapper.head:
            right_wrapper.head.left = root
            root.right = right_wrapper.head

        head = left_wrapper.head if left_wrapper.head else root
        tail = right_wrapper.tail if right_wrapper.tail else root

        return NodeWrapper(head, tail)


class NodeWrapper:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

#######
class Solution:
    def treeToDoublyList(self, root):
        if root is None:
            return None
        wrapper = NodeWrapper(None, None)
        self.dfs(root, wrapper)
        wrapper.head.left = wrapper.tail
        wrapper.tail.right = wrapper.head
        return wrapper.head
    def dfs(self, node, wrapper):
        if node is None:
            return
        self.dfs(node.left, wrapper)
        if wrapper.head is None:
            wrapper.head = node
        else:
            wrapper.tail.right = node
            node.left = wrapper.tail
        wrapper.tail = node
        self.dfs(node.right, wrapper)
class NodeWrapper:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail












if __name__ == '__main__':


    P = Node(4)
    P.left = Node(2)
    P.left.left = Node(1)
    P.left.right = Node(3)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    P.right = Node(5)
    # P.right.left = TreeNode(6)
    # P.right.right = TreeNode(6)


    s = Solution1()
    print(s.treeToDoublyList(P))
