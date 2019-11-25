class Solution(object):
    def invertTree(self, root):

        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root



from collections import deque
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        q = deque()
        q.append(root)
        while len(q) != 0:
            cur = q.popleft()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
        return root