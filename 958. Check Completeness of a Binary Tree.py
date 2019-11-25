class Solution:
    def __init__(self):
        self.max_depth = 0

    def isCompleteTree(self, root: TreeNode) -> bool:
        q = collections.deque()
        q.append(root)
        flag = True
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur is None:
                    flag = False
                else:
                    if flag == False:  # 说明空节点在这次出现过了，现在发现不空的，那就错了
                        return False
                    q.append(cur.left)
                    q.append(cur.right)
        return True
