# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        if root is None:
            return []
        wrapper = TreeNodeWrapper()
        res = []
        self.dfs(root, wrapper, res)

        return res
    # inorder traverse
    def dfs(self, root, wrapper, res):
        # base case
        if not root:
            return
        # general case
        self.dfs(root.left, wrapper, res)
        if wrapper.pre:
            wrapper.count = wrapper.count + 1 if wrapper.pre.val == root.val else 1
        if wrapper.count >= wrapper.maxi:
            if wrapper.count > wrapper.maxi:
                res.clear()
            res.append(root.val)
            wrapper.maxi = wrapper.count
        wrapper.pre = root
        self.dfs(root.right, wrapper, res)


class TreeNodeWrapper:
    def __init__(self, ):
        self.maxi = 0
        self.pre = None
        self.count = 1

if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \   / \
    #  4      5  6  7

    # P = TreeNode(1)
    # P.left = TreeNode(2)
    # P.left.left = TreeNode(4)
    # P.left.right = TreeNode(5)
    # # P.left.right.left = TreeNode(6)
    # # P.left.right.right = TreeNode(7)
    # # P.left.right.right.right = TreeNode(8)
    # P.right = TreeNode(3)
    # P.right.left = TreeNode(6)
    # P.right.right = TreeNode(7)
    #
    #
    # Q = TreeNode(1)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # Q.right.right = Node(3)

    P = TreeNode(1)
    P.right = TreeNode(2)

    s = Solution()
    print(s.findMode(P))
