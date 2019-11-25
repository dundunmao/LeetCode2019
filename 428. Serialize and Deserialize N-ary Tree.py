# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        array = []
        self.dfs_serialize(root, array)
        return ','.join(array)
    # preorder root,left,right,没拿到一个node.val，后面就接他有几个孩子
    def dfs_serialize(self, root, array):
        if not root:
            return
        array.append(str(root.val))
        array.append(str(len(root.children)))
        for child in root.children:
            self.dfs_serialize(child, array)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data or len(data) == 0:
            return None
        s = data.split(',')
        q = collections.deque()
        return self.dfs_deserialize(q)
    # 第一个node是这颗树的root,接着是这数有几个孩子，然后遍历孩子的各数，拿孩子。
    def dfs_deserialize(self, q):
        root = Node(int(q.popleft()), [])
        size = int(q.popleft())
        for i in range(size):
            root.children.append(self.dfs_deserialize(q))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
