import collections
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = collections.deque()
        self.dfs(res, root, target, k)
        return res
    def dfs(self, res, root, target, k):
        if not root:
            return
        self.dfs(res, root.left, target, k)
        if len(res) == k:
            if abs(res[0] - target) > abs(root.val - target):
                res.popleft()
            else:
                return
        if len(res) < k:
            res.append(root.val)
        self.dfs(res, root.right, target, k)

# o(lgn)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []
        pred = []
        succ = []
        self.ini_pred(root, target, pred)
        self.ini_succ(root, target, succ)
        if len(pred) > 0 and len(succ) > 0 and succ[-1] == pred[-1]:
            self.helper(pred, False)
        while k > 0:
            if len(succ) == 0:
                res.append(self.helper(pred, False))
            elif len(pred) == 0:
                res.append((self.helper(succ, True)))
            else:
                suc_diff = abs(succ[-1].val - target)
                pre_diff = abs(pred[-1].val - target)
                if suc_diff < pre_diff:
                    res.append(self.helper(succ, True))
                else:
                    res.append((self.helper(pred, False)))
            k -= 1
        return res

    def ini_succ(self, root, target, succ):
        while root:
            if root.val == target:
                succ.append(root)
                break
            elif root.val > target:
                succ.append(root)
                root = root.left
            else:
                root = root.right

    def ini_pred(self, root, target, pred):
        while root:
            if root.val == target:
                pred.append(root)
                break
            elif root.val < target:
                pred.append(root)
                root = root.right
            else:
                root = root.left
    def helper(self, stack, is_succ):
        cur = stack.pop()
        res = cur.val
        if is_succ:
            cur = cur.right
        else:
            cur = cur.left
        while cur:
            stack.append(cur)
            if is_succ:
                cur = cur.left
            else:
                cur = cur.right
        return res

##### 好理解的
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []
        pred = []
        succ = []
        self.inorder_pred(root, target, pred)
        self.reverse_inorder_succ(root, target, succ)
        while k > 0:
            if len(pred) == 0:
                res.append(succ.pop())
            elif len(succ) == 0:
                res.append((pred.pop()))
            elif abs(pred[-1] - target) <= abs(succ[-1] - target):
                res.append((pred.pop()))
            else:
                res.append(succ.pop())
            k -= 1
        return res

    def inorder_pred(self, node, target, pred): #得到的是升序 array
        if not node:
            return
        self.inorder_pred(node.left, target, pred)
        if node.val >= target:
            return
        pred.append(node.val)
        self.inorder_pred(node.right, target, pred)

    def reverse_inorder_succ(self, node, target, succ): #得到的是降序 array
        if not node:
            return
        self.reverse_inorder_succ(node.right, target, succ)
        if node.val < target:
            return
        succ.append(node.val)
        self.reverse_inorder_succ(node.left, target, succ)
