# 给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵二叉树：
#
#        1
#       / \
#      2   3
# 返回 6
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 用resultTyoe这个class
class ResultType(object):
    def __init__(self, root2any, any2any):
        self.root2any = root2any
        self.any2any = any2any

class Solution1:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        result = self.helper(root)
        return result.any2any
    def helper(self, root):
        if root is None:
            return ResultType(float('-inf'), float('-inf'))

        # Divide
        left = self.helper(root.left)
        right = self.helper(root.right)

        # Conquer
        root2any = max(0,max(left.root2any, right.root2any)) + root.val

        any2any = max(left.any2any, right.any2any)
        any2any = max(any2any,
                      max(0,left.root2any) +
                      max(0,right.root2any) +
                      root.val)

        return ResultType(root2any, any2any)




# 不用resultTyoe这个class,这个方法最好

class Solution2(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        any_any, root_any = self.helper(root)
        return any_any

    def helper(self, root):
        if root is None:
            return float('-inf'), float('-inf')
        left_any_any, left_root_any = self.helper(root.left)
        right_any_any, right_root_any = self.helper(root.right)
        root_any = root.val + max(0, left_root_any, right_root_any)
        any_any = max(left_any_any, right_any_any, root_any, root.val + left_root_any + right_root_any)
        return any_any, root_any

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        if not root:
            return 0
        ans = [float('-inf')]  #在这里更新global的最大path-sum
        self.helper(root,ans)  #表现从root出发的最大path—sum(root-any)
        return ans[0]
    def helper(self,root,ans):
        if not root:
            return 0
        l = max(0, self.helper(root.left, ans))   #左子树的root-any
        r = max(0, self.helper(root.right, ans))  #右子树的root-any
        sum = l + r + root.val  #root这棵树的global的any-any
        ans[0] = max(ans[0], sum) #更新
        return max(l,r) + root.val  #返回的是 root-any

#################################################3
# 2019 rockey

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            raise ValueError('not valid input')
        return self.dfs(root).max_sum

    def dfs(self, root):
        # base case
        if not root.left and not root.right:
            return Result(root.val, root.val)

        # general case
        res_left = Result(float('-inf'), float('-inf')) if not root.left else self.dfs(root.left)
        res_right = Result(float('-inf'), float('-inf')) if not root.right else self.dfs(root.right)

        max_sum = max(res_left.max_sum,
                      res_right.max_sum,
                      max(0, res_left.max_sum_to_root) + max(0, res_right.max_sum_to_root) + root.val
                      )
        max_sum_to_root = max(root.val,
                              res_left.max_sum_to_root + root.val,
                              res_right.max_sum_to_root + root.val
                              )
        return Result(max_sum, max_sum_to_root)


class Result:
    def __init__(self, max_sum, max_sum_to_root):
        self.max_sum = max_sum
        self.max_sum_to_root = max_sum_to_root



#################################################3


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            raise ValueError('not valid input')
        return self.dfs(root).max_sum

    def dfs(self, root):
        # base case
        if not root:
            return Result(float('-inf'), float('-inf'))

        # general case
        res_left = self.dfs(root.left)
        res_right = self.dfs(root.right)

        max_sum = max(res_left.max_sum,
                      res_right.max_sum,
                      max(0, res_left.max_sum_to_root) + max(0, res_right.max_sum_to_root) + root.val
                      )
        max_sum_to_root = max(root.val,
                              res_left.max_sum_to_root + root.val,
                              res_right.max_sum_to_root + root.val
                              )
        return Result(max_sum, max_sum_to_root)


class Result:
    def __init__(self, max_sum, max_sum_to_root):
        self.max_sum = max_sum
        self.max_sum_to_root = max_sum_to_root

#################################################3
# 16 个分支
import random

class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 16

class Result:
    def __init__(self, max_sum, max_sum_to_root):
        self.max_sum = max_sum
        self.max_sum_to_root = max_sum_to_root

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            raise ValueError('not valid input')
        new_root = self.copy_tree(root)
        return self.dfs(new_root).max_sum

    def dfs(self, root):
        # base case
        if not root:
            return Result(float('-inf'), float('-inf'))

        # general case
        max_sum_without_root = float('-inf')
        biggest_sum_to_child = float('-inf')
        bigger_sum_to_child = biggest_sum_to_child
        for ele in root.children:
            ele_res = self.dfs(ele)
            max_sum_without_root = max(max_sum_without_root, ele_res.max_sum)
            if ele_res.max_sum_to_root > biggest_sum_to_child:
                bigger_sum_to_child = biggest_sum_to_child
                biggest_sum_to_child = ele_res.max_sum_to_root
            elif ele_res.max_sum_to_root > bigger_sum_to_child:
                bigger_sum_to_child = ele_res.max_sum_to_root

        total_max_sum = max(max_sum_without_root,
                            max(0, biggest_sum_to_child) + max(0, bigger_sum_to_child) + root.val
                            )
        total_max_sum_to_root = max(root.val, biggest_sum_to_child + root.val)

        return Result(total_max_sum, total_max_sum_to_root)

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


################
# 16分支

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import random


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 16


class Result:
    def __init__(self, max_profit, max_profit_without_root):
        self.max_profit = max_profit
        self.max_profit_without_root = max_profit_without_root


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        new_root = self.copy_tree(root)
        return self.dfs(new_root).max_profit

    def dfs(self, root):
        # base case
        if not root:
            return Result(0, 0)
        # general case
        child_max_profit_without_root_sum = 0
        child_max_profit_sum = 0

        for child in root.children:
            child_res = self.dfs(child)
            child_max_profit_without_root_sum += child_res.max_profit_without_root
            child_max_profit_sum += child_res.max_profit

        max_profit = max(child_max_profit_sum, root.val + child_max_profit_without_root_sum)
        max_profit_without_root = child_max_profit_sum

        return Result(max_profit, max_profit_without_root)

    def copy_tree(self, root):
        if not root:
            return None
        my_root = MyTreeNode(root.val)
        my_root.children[random.randint(0, 7)] = self.copy_tree(root.left)
        my_root.children[random.randint(0, 7) + 8] = self.copy_tree(root.right)
        return my_root


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      3     6
    #    /   \
    #  2      4

    P = TreeNode(1)
    P.left = TreeNode(2)
    s = Solution()
    print(s.maxPathSum(P))





