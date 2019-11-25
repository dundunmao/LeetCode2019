class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def insert(self, root, key):
        new = TreeNode(key)
        cur = root
        leaf = None
        # temp会记录遍历到的最后一个叶子
        while cur:
            leaf = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if not leaf:
            leaf = new
        elif key < leaf.key:
            leaf.left = new
        else:
            leaf.rgiht = new

