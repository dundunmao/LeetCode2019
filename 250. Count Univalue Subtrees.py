# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.count
    def helper(self,root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            self.count += 1
            return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left is False or right is False:
            return False
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        self.count += 1
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root).count_total

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            return Result(True, 1)
        # general case
        left_res = Result(True, 0) if not root.left else self.dfs(root.left)
        right_res = Result(True, 0) if not root.right else self.dfs(root.right)

        count_total = left_res.count_total + right_res.count_total
        is_uni = False

        if left_res.is_uni and right_res.is_uni:
            if (root.left and root.left.val == root.val) and (root.right and root.right.val == root.val):
                count_total += 1
                is_uni = True
            elif (not root.left and root.right and root.right.val == root.val) or (
                    not root.right and root.left and root.left.val == root.val):
                count_total += 1
                is_uni = True
            elif not root.left and not root.right:
                count_total += 1
                is_uni = True

        return Result(is_uni, count_total)


class Result:
    def __init__(self, is_uni, count_total):
        self.is_uni = is_uni
        self.count_total = count_total


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      1     5
    #    /   \  / \
    #  5     5  5 5

    P = TreeNode(5)
    P.left = TreeNode(1)
    P.right = TreeNode(5)
    P.left.left = TreeNode(5)
    P.left.right = TreeNode(5)
    P.right.left = TreeNode(5)
    P.right.right = TreeNode(5)
    s = Solution()
    print(s.countUnivalSubtrees(P))
