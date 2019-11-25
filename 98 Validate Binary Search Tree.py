# 给定一个二叉树，判断它是否是合法的二叉查找树(BST)
#
# 一棵BST定义为：
#
# 节点的左子树中的值要严格小于该节点的值。
# 节点的右子树中的值要严格大于该节点的值。
# 左右子树也必须是二叉查找树。
# 一个节点的树也是二叉查找树。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 一个例子：
#
#   2
#  / \
# 1   4
#    / \
#   3   5
# 上述这棵二叉树序列化为 {2,1,4,#,#,3,5}.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution_leet(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minVal = float('-inf')
        maxVal = float('inf')
        return self.helper(root, minVal, maxVal)

    def helper(self, root, minVal, maxVal): #minVal和maxVal是root的最小最大boundary
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        maxi, mini, valid = self.helper(root)
        return valid
    def helper(self, root):
        if root is None:
            return float('-inf'), float('inf'), True
        l_max, l_min, l_valid = self.helper(root.left)
        r_max, r_min, r_valid = self.helper(root.right)
        if l_valid and r_valid and root.val > l_max and root.val < r_min:
                return max(root.val,r_max), min(root.val,l_min), True
        else:
            return 0, 0, False
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      3     6
    #    /   \
    #  2      4

    P = TreeNode(5)
    P.left = TreeNode(3)
    P.left.left = TreeNode(2)
    P.left.right = TreeNode(4)
    P.right = TreeNode(6)
    # Q = P.left.right

    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution()
    print(s.isValidBST(P))
