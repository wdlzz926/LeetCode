# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail = head
        fast = slow = head
        if not head:
            return None
        n = 0
        while(1):
            n+=1
            if tail.next == None:
                break
            tail = tail.next
        k = k%n
        if k==0:
            return head
        for i in range(k):
            fast = fast.next
        while(fast.next):
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
            