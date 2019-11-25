class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        i = dummy
        j = dummy
        while j.next != None:
            j = j.next
            if j.val != 9:
                i = j
        if j.val != 9:
            j.val += 1
        else:
            i.val += 1
            i = i.next
            while i != None:
                i.val = 0
                i = i.next
        if dummy.val == 0:
            return dummy.next
        return dummy