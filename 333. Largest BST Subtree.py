class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = 1
        self.maxi = float('-inf')
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res
    def helper(self,root):
        if root is None:  # None
            return True, float('inf'), float('-inf'),0
        if root.left is None and root.right is None:  #叶子节点
            return True, root.val, root.val, 1
        left, min_left, max_left, count_left = self.helper(root.left)  #左子树
        right, min_right, max_right,count_right = self.helper(root.right)  #右子树
        if left and right and root.val > max_left and root.val < min_right:  #当前树为BST
            count = count_left + 1 + count_right
            maxi = max(root.val, max_right)
            mini = min(root.val, min_left)
            if maxi >= self.maxi:
                self.res =  count
            return True, mini, maxi, count
        else:
            return False, float('inf'), float('-inf'),0  #当前树不是BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).num_nodes

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            return Result(root.val, root.val, True, 1)
        # general case
        left_res = Result(root.val, float('-inf'), True, 0) if not root.left else self.dfs(root.left)
        right_res = Result(float('inf'), root.val, True, 0) if not root.right else self.dfs(root.right)
        if left_res.is_bst and right_res.is_bst and left_res.maxi < root.val and right_res.mini > root.val:
            is_bst = True
            mini = left_res.mini
            maxi = right_res.maxi
            num_nodes = left_res.num_nodes + right_res.num_nodes + 1
            return Result(mini, maxi, is_bst, num_nodes)
        else:
            return Result(0, 0, False, max(left_res.num_nodes, right_res.num_nodes))


class Result:
    def __init__(self, mini, maxi, is_bst, num_nodes):
        self.mini = mini
        self.maxi = maxi
        self.is_bst = is_bst
        self.num_nodes = num_nodes


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      1     5
    #    /   \  / \
    #  5     4  5 5

    # P = TreeNode(5)
    # P.left = TreeNode(1)
    # P.right = TreeNode(5)
    # P.left.left = TreeNode(5)
    # P.left.right = TreeNode(4)
    # P.right.left = TreeNode(4)
    # P.right.right = TreeNode(6)
    # s = Solution()  #3
    # print s.largestBSTSubtree(P)
    # P = TreeNode(1)
    # P.left = TreeNode(4)
    # P.right = TreeNode(5)
    # P.left.left = TreeNode(2)
    # s = Solution() #2
    # print s.largestBSTSubtree(P)
    # P = TreeNode(3)
    # P.right = TreeNode(4)
    # P.right.right = TreeNode(1)
    # P.right.right.right = TreeNode(2)
    # s = Solution() #2
    # print s.largestBSTSubtree(P)
    P = TreeNode(2)
    P.left = TreeNode(5)
    P.right = TreeNode(4)
    P.right.right = TreeNode(3)
    P.right.right.left = TreeNode(1)
    s = Solution2() #2
    print(s.largestBSTSubtree(P))
