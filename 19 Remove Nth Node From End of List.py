
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if n <= 0:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        for i in range(0,n):
            head = head.next
        while head is not None:
            head = head.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
