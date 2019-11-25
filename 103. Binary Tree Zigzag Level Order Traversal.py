# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        flag = True
        while len(queue):
            size = len(queue)
            array = collections.deque()
            for i in range(size):
                cur = queue.popleft()
                if flag:
                    array.append(cur.val)
                else:
                    array.appendleft(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(array)
            flag = not flag
        return res


s = Solution()
q = TreeNode(1)
q.left = TreeNode(2)
print(s.zigzagLevelOrder(q))
