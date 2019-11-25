# 根据preoreder和inorder构造二叉树.
#
#  注意事项
#
# 你可以假设树中不存在相同数值的节点
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:
#
#   2
#  / \
# 1   3

# preorder  根左右
# inorder   左根右

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        root.val = preorder[0]
        index_root_inorder = inorder.index(root.val)

        #left
        left_preorder = preorder[1:index_root_inorder+1]
        left_inorder = inorder[:index_root_inorder]
        root.left = self.buildTree(left_preorder, left_inorder)


        #right

        right_preorder = preorder[index_root_inorder+1:]
        right_inorder = inorder[index_root_inorder+1:]
        root.right = self.buildTree(right_preorder, right_inorder)


        return root
##################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        index_in_inorder = {}
        for i in range(len(inorder)):
            index_in_inorder[inorder[i]] = i
        return self.dfs(preorder, inorder, index_in_inorder, 0, 0, len(preorder) - 1)

    def dfs(self, preorder, inorder, index_in_inorder, pre_start, in_start, in_end):
        if in_start > in_end:
            return None
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        root_index = index_in_inorder[root_val]

        left_tree_size = root_index - in_start
        right_tree_size = in_end - root_index

        if left_tree_size > 0:
            root.left = self.dfs(preorder, inorder, index_in_inorder, pre_start + 1, in_start, root_index - 1)
        if right_tree_size > 0:
            root.right = self.dfs(preorder, inorder, index_in_inorder, pre_start + 1 + left_tree_size, root_index + 1, in_end)
        return root
