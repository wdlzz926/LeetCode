# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        curr = head
        while curr != None:
            tmp_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = tmp_node
        return new_head

#recursive
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None): return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
