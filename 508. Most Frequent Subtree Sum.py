class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        if not root:
            return []
        res = {}
        self.dfs(root, res)
        maxi = max([ele for ele in res.values()])

        return [key for key, val in res.items() if val == maxi]

    def dfs(self, root, res):
        # base case
        if not root.left and not root.right:
            sum = root.val
            if sum in res:
                res[sum] += 1
            else:
                res[sum] = 1
            return sum
        # general case
        left = self.dfs(root.left, res) if root.left else 0
        right = self.dfs(root.right, res) if root.right else 0
        sum = left + right + root.val
        if sum in res:
            res[sum] += 1
        else:
            res[sum] = 1
        return sum
if __name__ == '__main__':


    P = TreeNode(5)
    P.left = TreeNode(2)
    # P.left.left = TreeNode(3)
    # P.left.right = TreeNode(4)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(-3)
    # P.right.left = TreeNode(6)
    # P.right.right = TreeNode(6)


    s = Solution()
    print(s.findFrequentTreeSum(P))
