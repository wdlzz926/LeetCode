# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        later = dummy
        for i in range(n):
            later = later.next
        while(1):
            if later.next == None:
                cur.next = cur.next.next
                return dummy.next
            later = later.next
            cur = cur.next
        