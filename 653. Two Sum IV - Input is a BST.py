class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution_lintcode:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # extra space: O(n)
        if root is None:
            return []

        nums = self.in_order_traverse(root)
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] == n:
                return [nums[start], nums[end]]
            elif nums[start] + nums[end] > n:
                end -= 1
            else:
                start += 1

    def in_order_traverse(self, root):
        if root is None:
            return []

        left = self.in_order_traverse(root.left)
        right = self.in_order_traverse(root.right)

        return left + [root.val] + right

# 方法一：没考虑BST的性质，就是想做two sum，一边检查target-cur在不在hash里，不在就加进hash，在返回True
# TC: O(n)
# SC:O(n)

class Solution1(object):
    def findTarget(self, root, k):
        hash = {}
        return self.helper(root, k, hash)
    def helper(self,root, k, hash):
        if root is None:
            return False
        if hash.has_key(k - root.val):
            return True
        hash[root.val] = True
        return self.helper(root.left, k, hash) or self.helper(root.right, k, hash)



# 方法2：跟第一种一样，不过这里的遍历用的是BFS，
from collections import deque
class Solution2(object):
    def findTarget(self, root, k):
        hash = {}
        q = deque()
        q.append(root)
        while len(q) != 0:
            if q[0] != None:
                node = q.popleft()
                if hash.has_key(k - node.val):
                    return True
                hash[node.val] = True
                q.append(node.right)
                q.append(node.left)
            else:
                q.popleft()
        return False

class Solution(object):
    def findTarget(self, root, k):
        array = []
        self.inorder(root,array)
        l = 0
        r = len(array) - 1
        while l < r:
            sum = array[l]+array[r]
            if sum == k:
                return True
            if sum < k:
                l += 1
            else:
                r -= 1
        return False
    def inorder(self,root,array):
        if root is None:
            return
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)
if __name__ == "__main__":
#      4
#    /  \
#  6
# /  \
#3   1

    P = TreeNode(5)
    P.left = TreeNode(3)
    P.left.left = TreeNode(2)
    P.left.right = TreeNode(4)
    P.right = TreeNode(6)
    P.right.right = TreeNode(7)
    k = 28
    s = Solution()
    print s.findTarget(P,k)
