# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        p = l1
        q = l2
        curr = res
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            digit = x+y+carry
            carry = int(digit/10)
            curr.next = ListNode(digit %10)
            curr = curr.next
            if p is not None: p = p.next
            if q is not None: q = q.next
        if carry >0:
            curr.next = ListNode(carry)
        return res.next
        
 