class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(cur.val)
        return res


class Solution(object):
    def rightSideView(self, root):
        res = []
        if root is None:
            return res
        right = self.rightSideView(root.right)  #左子树的res
        left = self.rightSideView(root.left)    #右子树的res
        res.append(root.val)
        res.extend(right)   #右子树的res全加入res里
        for i in range(len(right), len(left)):  #左子树多余的res全加入res里
            res.append(left[i])
        return res


#####
import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        deque = collections.deque()
        deque.append(root)
        res = []
        while len(deque):
            size = len(deque)
            res.append(deque[0].val)
            for i in range(size):
                cur = deque.popleft()
                # 先加right再加left，这样每次for之前，只要把deque的第一个放res里就行
                if cur.right:
                    deque.append(cur.right)
                if cur.left:
                    deque.append(cur.left)

        return res
