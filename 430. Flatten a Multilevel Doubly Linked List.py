# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        first, last = self.dfs(head)
        return first

    def dfs(self, head):
        if not head.next and not head.child:
            return head, head
        first, last = head, head
        head_child = head.child
        head_next = head.next
        if head_child:
            child_first, child_last = self.dfs(head_child)
            last.child = None
            last.next = child_first
            child_first.prev = last
            last = child_last

        if head_next:
            next_first, next_last = self.dfs(head_next)
            last.child = None
            last.next = next_first
            next_first.prev = last
            last = next_last
        return first, last

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while not p:
            if not p.child:
                temp = p.child
                while not temp.next:
                    temp = temp.next
                temp.next = p.next
                if not p.next:
                    p.next.prev = temp
                p.next = p.child
                p.next.prev = p
                p.child = None

            else:
                p = p.next
        return head

if __name__ == '__main__':


    P = Node(1)
    P.next = Node(2)
    P.next.next = Node(3)
    P.next.next.child = Node(7)
    P.next.next.child.next = Node(8)
    P.next.next.child.next.child = Node(11)
    P.next.next.child.next.child.next = Node(12)
    P.next.next.child.next.next = Node(9)
    P.next.next.child.next.next.next = Node(10)

    P.next.next.next = Node(4)
    P.next.next.next.next = Node(5)
    P.next.next.next.next.next = Node(6)

    Q = Node(1)
    Q.next = Node(2)
    Q.child = Node(3)

    s = Solution()
    print(s.flatten(Q))
