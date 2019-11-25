# 假定用一个链表表示两个数，其中每个节点仅包含一个数字。假设这两个数的数字顺序排列，请设计一种方法将两个数相加，并将其结果表现为链表的形式。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 6->1->7 + 2->9->5。即，617 + 295。
#
# 返回 9->1->2。即，912 。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Write your code here
        num1 = self.converse(l1)
        num2 = self.converse(l2)
        num = num1+num2
        # converse number to list
        dummy = ListNode(0)
        cur = dummy
        length = len(str(num))-1
        # recorde = len(str(num))
        while length!=-1:
            value = num/10**length
            num = num%10**length
            cur.next= ListNode(value)
            cur = cur.next
            length -= 1
        return dummy.next

    def converse(self, ll):
        num = 0
        while ll:
            num = (num*10)+ll.val
            ll = ll.next
        return num

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1 is not None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2.append(l2.val)
            l2 = l2.next
        sum = 0
        list = ListNode(-1)
        while s1 != [] or s2 != []:
            if s1 != []:
                sum += s1.pop()
            if s2 != []:
                sum += s2.pop()
            list.val = sum % 10
            head = ListNode(sum/10)
            head.next = list
            list = head
            sum /= 10
        if list.val == 0:
            return list.next
        else:
            return list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_new = self.reverse_ll(l1)
        l2_new = self.reverse_ll(l2)
        temp = 0
        cur = ListNode(0)
        dummy = cur
        while l1_new and l2_new:
            add_up = l1_new.val + l2_new.val + temp
            cur.next = ListNode(add_up % 10)
            temp = add_up // 10
            cur = cur.next
            l1_new = l1_new.next
            l2_new = l2_new.next
        while l1_new:
            add_up = l1_new.val + temp
            cur.next = ListNode(add_up % 10)
            temp = add_up // 10
            cur = cur.next
            l1_new = l1_new.next

        while l2_new:
            add_up = l2_new.val + temp
            cur.next = ListNode(add_up % 10)
            temp = add_up // 10
            cur = cur.next
            l2_new = l2_new.next
        if temp:
            cur.next = ListNode(temp)
            cur = cur.next
        dummy = dummy.next
        res = self.reverse_ll(dummy)
        while res.val == 0 and dummy.next:
            res = res.next
        return res

    def reverse_ll(self, cur):
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
