# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        g_set = set(G)
        cur = head
        while cur:
            if cur.val in g_set and (not cur.next or cur.next.val not in g_set):
                res += 1
            cur = cur.next

        return res
