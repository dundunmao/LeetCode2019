# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
# 跟上一题一模一样。用stack每次往里存一排的，然后连上
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #corner case
        if root is None:
            return root

        q =  deque()
        q.append(root)
        while q:
            le = len(q)
            temp = None
            for i in range(le):
                item = q.pop()
                if item.right:
                    q.appendleft(item.right)
                if item.left:
                    q.appendleft(item.left)
                if i == 0:
                    item.next = None
                else:
                    item.next = temp
                temp = item
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = None
        pre = None
        cur = root
        while cur != None:
            while cur != None:  #遍历当前层
                # left
                if cur.left != None:
                    if pre != None:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                # right
                if cur.right != None:
                    if pre != None:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                # move to next node
                cur = cur.next
            # move to next level
            cur = head
            head = None
            pre = None


################
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        deque = collections.deque()
        deque.append(root)
        while len(deque):
            size = len(deque)
            next_node = None
            for i in range(size):
                cur = deque.popleft()
                cur.next = next_node
                next_node = cur
                if cur.right:
                    deque.append(cur.right)
                if cur.left:
                    deque.append(cur.left)

        return root

if __name__ == "__main__":
    strs = "0"
    s = Solution()
    print s.numDecodings(strs)
