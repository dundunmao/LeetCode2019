class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = [float('-inf')]
        self.helper(root, res)
        return res[0]

    def helper(self, root, res):
        if root == None:
            res[0] = max(res[0],-1)
            return -1
        if root.left is None and root.right is None:
            res[0] = max(res[0],0)
            return 0
    # 如果有左子树就recursive，left为左子树的F。 ，如果为None就 left = -1
        if root.left:
            left = self.helper(root.left, res)  # left_root to any
        else:
            left = -1
    # 如果有右子树就recursive，right为右子树的F。 如果为None就 right = -1
        if root.right:
            right = self.helper(root.right, res)  # right_root to any
        else:
            right = -1
    # 开始算res和该node的F，l_cal和r_cal是用来算这两个值的
        # left和root值一样和不一样时的 l_cal
        if left >= 0 and root.val == root.left.val:
            l_cal = left
        else:
            l_cal = -1
        # right和root值一样和不一样时的 r_cal
        if right >= 0 and root.val == root.right.val:
            r_cal = right
        else:
            r_cal = -1
    # update最大值
        res[0] = max(res[0], l_cal + r_cal + 2)
    # 算出改node的F
        return max(l_cal, r_cal) + 1  # root-any



class Solution(object):
    def __init__(self):
        self.res = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res
    def helper(self, root): #root-any的结果
        if root is None:
            return 0
        if not root.left and not root.right:
            return 0
        any_root_any = 0 #带root的折线，用来合成self.res的
        root_left = 0 #root_left的结果
        root_right = 0 #root_right的结果
        left = self.helper(root.left)
        right = self.helper(root.right)
        if root.left and root.val == root.left.val:
            any_root_any += left + 1
            root_left = left + 1
        if root.right and root.val == root.right.val:
            any_root_any += right + 1
            root_right = right + 1
        self.res = max(self.res, any_root_any)
        return max(root_left, root_right)


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      4     5
    #    /   \  /
    #  1     1  5

    P = TreeNode(5)
    P.left = TreeNode(4)
    P.right = TreeNode(5)
    P.left.left = TreeNode(1)
    P.left.right = TreeNode(1)
    P.right.left = TreeNode(5)
    s = Solution()
    print(s.longestUnivaluePath(P))
