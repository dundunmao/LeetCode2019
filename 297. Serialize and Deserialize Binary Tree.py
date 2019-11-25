
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''

    def serialize(self, root):
        # write your code here
        if root is None:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        # 这时q=【1，2，3，4，5，N,N,N,N,6,7,N,N,N,8,N,N】
        while queue[-1] is None: #把最后几个None去掉，就是8的left，right
            queue.pop()
        for i in range(len(queue)): #把里面的None用'#'替换
            if queue[i] == None:
                queue[i] = '#'
            else:
                queue[i] = str(queue[i].val)
        return '{'+','.join(queue)+'}' #'{1,2,3,4,5,#,#,#,#,6,7,#,#,#,8}'

        # return '{%s}' % ','.join([str(node.val) if node is not None else '#'
        #                           for node in queue])

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    # 上的得到的data = '{1,2,3,4,5,#,#,#,#,6,7,#,#,#,8}'
    def deserialize(self, data):
        # write your code here
        data = data.strip('\n')  #把他前面的空格去掉

        if data == '{}':
            return None

        vals = data[1:-1].split(',')  #把除了'{'之外的str变成array
        # vals = ['1', '2', '3', '4', '5', '#', '#', '#', '#', '6', '7', '#', '#', '#', '8']
        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root
###################
# bfs
import collections
class Codec:
    # return "[1,2,3,null,null,4,5]"
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur:
                    res.append(str(cur.val))
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    res.append('#')
        # print(res)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        print(data)
        root = TreeNode(data[0])
        cur_queue = collections.deque()
        cur_queue.append(root)
        i = 1
        while i < len(data):
            size = len(cur_queue)
            for j in range(size):
                ele = cur_queue.popleft()
                if data[i] != '#':
                    ele.left = TreeNode(data[i])
                    cur_queue.append(ele.left)
                i += 1
                if data[i] != '#':
                    ele.right = TreeNode(data[i])
                    cur_queue.append(ele.right)
                i += 1
        return root

# dfs
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        return self.dfs_serialize(root)

    def dfs_serialize(self, root):
        if not root:
            return '#,'
        else:
            res = str(root.val) + ','
            left = self.dfs_serialize(root.left)
            right = self.dfs_serialize(root.right)
        return res + left + right


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        q = collections.deque(data)

        return self.dfs_deserialize(q)


    def dfs_deserialize(self, q):
        if q[0] == '#':
            q.popleft()
            return None
        root = TreeNode(int(q[0]))
        q.popleft()
        root.left = self.dfs_deserialize(q)
        root.right = self.dfs_deserialize(q)
        return root


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2      3
    #    /   \   / \
    #  4      5 N  N
    # / \    / \
    #N  N   6   7
    #      / \ / \
    #     N  N N 8
    #           / \
    #          N  N
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(5)
    P.left.right.left = TreeNode(6)
    P.left.right.right = TreeNode(7)
    P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)
    s = Codec1()
    #
    data = '1,2,3,4,5,#,#,#,#,6,7,#,#,#,8,#,#'
    # print(s.deserialize(data))
    print(s.serialize(P))
    print(s.deserialize(s.serialize(P)))




    s = Solution()
    data = s.serialize(P)
    print(s.deserialize(data))
