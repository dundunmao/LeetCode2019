# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = self.dfs_serialize(root)
        return ','.join(res)

    def dfs_serialize(self, root):
        if not root:
            return []
        else:
            left = self.dfs_serialize(root.left)
            right = self.dfs_serialize(root.right)
            return left + right + [str(root.val)]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = [int(ele) for ele in data.split(',') if ele]
        res = self.dfs_deserialize(data, float('-inf'), float('inf'))
        return res

    def dfs_deserialize(self, data, lower, upper):
        if not data or data[-1] < lower or data[-1] > upper:
            return None
        val = data.pop()
        root = TreeNode(val)
        root.right = self.dfs_deserialize(data, val, upper) #右子树值在自己和上一层node之间
        root.left = self.dfs_deserialize(data, lower, val) # 左子树值在上一层的node和自己之间
        return root

# Your Codec object will be instantiated and called as such:
P = TreeNode(10)
P.left = TreeNode(5)
P.left.left = TreeNode(2)
P.left.right = TreeNode(7)
P.left.right.left = TreeNode(6)
P.right = TreeNode(12)
codec = Codec()
print(codec.serialize(P))
print(codec.deserialize(codec.serialize(P)))
