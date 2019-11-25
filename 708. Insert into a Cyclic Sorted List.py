# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        # 找到最大node
        max_node = head
        while max_node.next != head and max_node.val <= max_node.next.val:
            max_node = max_node.next
        # 找到最小node
        min_node = max_node.next
        cur = min_node
        if insertVal >= max_node.val or insertVal <= min_node.val:
            node = Node(insertVal, min_node)
            max_node.next = node
        else:
            while cur.next.val < insertVal:
                cur = cur.next
            new_node = Node(insertVal, cur.next)
            cur.next = new_node
        return head

s = Solution()
a = None
print(s.insert(a, 2))

a = Node(1, None)
b = Node(4, a)
c = Node(3,b)
a.next = c
print(s.insert(a, 2))
