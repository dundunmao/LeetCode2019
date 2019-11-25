class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1,n)
    def helper(self,min, max): #return的是一个array
        res = []
        if min > max:
            return res
        for cur in range(min, max+1):  #当cur是root时
            left = self.helper(min, cur - 1)   #左子树dfs后，所有树的array
            right = self.helper(cur + 1, max)  #右子树dfs后，所有树的array
            if len(left) == 0 and len(right) == 0:  #如果左右子树都是空，root就是所求，加入res
                root = TreeNode(cur)
                res.append(root)
            elif len(left) == 0: #如果左子树都是空，root就跟 right 连
                for r in right: #把right这个array里的每一个树，都连一遍
                    root = TreeNode(cur)
                    root.right = r
                    res.append(root)
            elif len(right) == 0:  #如果右子树都是空，root就跟 left 连
                for l in left:   #把left这个array里的每一个树，都连一遍
                    root = TreeNode(cur)
                    root.left = l
                    res.append(root)
            else:   #如果都不空，就左右都连
                for l in left:   #把left和right这两个array里的每一个树，都连一遍
                    for r in right:
                        root = TreeNode(cur)
                        root.left = l
                        root.right = r
                        res.append(root)
        return res
