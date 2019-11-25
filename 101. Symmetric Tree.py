class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution1:
    def isSymmetric(self, root):
        # Write your code here
        if root:
            return self.help(root.left, root.right)
        return True

    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False
from collections import deque
class Solution:
    def isSymmetric(self, root):
        q = deque()
        q.append(root)
        q.append(root)
        while len(q) != 0:
            t1 = q.popleft()
            t2 = q.popleft()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /    \
    #      2       2
    #    /   \   /  \
    #  3      4 4   3
    #
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.right = TreeNode(2)
    P.left.left = TreeNode(3)
    P.left.right = TreeNode(4)
    P.right.left = TreeNode(4)
    P.right.right = TreeNode(3)
    s = Solution()
    s.isSymmetric(P)

































