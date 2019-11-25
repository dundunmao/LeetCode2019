#  将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
#
#  注意事项
#
# 不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
#               1
#                \
#      1          2
#     / \          \
#    2   5    =>    3
#   / \   \          \
#  3   4   6          4
#                      \
#                       5
#                        \
#                         6

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        self.flatten(root.left)  #左边变成flatten的
        self.flatten(root.right) #右边变成flatten的
        p = root                 #给一个dummy指针指向root
        if p.left == None:       # 如果root的左边是None,这个树就已经flatten好了
            return
        p = p.left                #如果不是，就来的root的左边，
        while p.right:           #一直遍历到左边的最后一个点，
            p = p.right
        p.right = root.right     #把最后一个点跟root的右边连上
        root.right = root.left   #再把左边换到右边
        root.left = None          #再让左边为空
###############################
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.dfs(root)

    def dfs(self, root): # return 最后一个node
        # base case
        if not root.left  and not root.right:
            return root
        # general case
        left = root.left
        right = root.right
        if left:
            root.right = left
            root.left = None
            left_last = self.dfs(left)
            root = left_last
        if right:
            root.right = right
            root.left = None
            right_last = self.dfs(right)
            root = right_last
        return root


    ########################
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        last_visted = TreeNodeWrapper(TreeNode(-1))
        self.dfs(root, last_visted)

    def dfs(self, root, last_visted):
        if not root:
            return
        last_visted.node.right = root
        last_visted.node = root
        left = root.left
        right = root.right
        root.left = None
        self.dfs(left, last_visted)
        self.dfs(right, last_visted)

class TreeNodeWrapper:
    def __init__(self, node):
        self.node = node

    #########################
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \   / \
    #  4      5  6  7

    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(3)
    P.left.right = TreeNode(4)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(5)
    # P.right.left = TreeNode(6)
    P.right.right = TreeNode(6)
    #
    #
    # Q = TreeNode(1)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # Q.right.right = Node(3)

    # P = TreeNode(1)
    # P.right = TreeNode(2)

    s = Solution1()
    print(s.flatten(P))
