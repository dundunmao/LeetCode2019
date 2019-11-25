
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        dummy = RandomListNode(0)
        pre = dummy
        # pre = newnNode
        map = {}
        while head is not None:
            if map.has_key(head):
                newNode = map.get(head)
            else:
                newNode = RandomListNode(head.label)
                map[head] = newNode
            pre.next = newNode
            if head.random is not None:          #这里别忘了
                if map.has_key(head.random):
                    newNode.random = map.get(head.random)
                else:
                    newNode.random = RandomListNode(head.random.label)
                    map[head.random] = newNode.random
            pre = pre.next            #这里别忘了.
            head = head.next
        return dummy.next

# 方法二,基本同上,但是先循环得到next,再循环一边得到random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        nHead = RandomListNode(head.label)
        old = head
        new = nHead
        hash = {}
        hash[head] = nHead
        while old.next != None:
            old = old.next
            new.next = RandomListNode(old.label)
            new = new.next
            hash[old] = new
        old = head
        new = nHead
        while old != None:
            if old.random != None:
                new.random = hash[old.random]
            old = old.next
            new = new.next
        return nHead




    # 方法3: 先loop一遍,在每一个点后都复制一边这个node 1->1'->2->2'->3->3'->N这时候random都带上
#       再loop一遍,提取每一个新点和起箭头.
class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def splitList(self, head):
        newHead = head.next
        while head is not None:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next is not None:
                temp.next = temp.next.next
        return newHead

    def copyRandom(self, head):
        while head is not None:
            if head.next.random is not None:
                head.next.random = head.random.next
            head = head.next.next

    def copyNext(self, head):
        while head is not None:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next


class Node:
    def __init__(self, x, next, random):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self.copy_node(head)
        self.copy_random(head)
        res = self.split(head)
        return res

    def copy_node(self, head):
        old = head
        while old:
            new = Node(old.val, None, None)
            new.next = old.next
            old.next = new
            old = new.next

    def copy_random(self, head):
        cur = head
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

    def split(self, head):
        dummy = Node(-1, None, None)
        dummy.next = head
        cur = dummy
        while head and head.next:
            cur.next = head.next
            cur = cur.next
            head.next = cur.next
            head = head.next
        return dummy.next


if __name__ == '__main__':

    # P = RandomListNode(1)
    # P.next = RandomListNode(2)
    # P.next.next = RandomListNode(3)
    # P.next.next.next = RandomListNode(4)
    # P.random = P
    # P.next.random = P.next.next
    # P.next.next.random = P.next
    # P.next.next.next.random = None
    #
    #
    # s = Solution4()
    # print(s.copyRandomList(P))

    P = Node(1, None, None)
    P.next = Node(2, None, None)
    # P.next.next = RandomListNode(3)
    # P.next.next.next = RandomListNode(4)
    P.random = P.next
    P.next.random = P.next



    s = Solution4()
    print(s.copyRandomList(P))
