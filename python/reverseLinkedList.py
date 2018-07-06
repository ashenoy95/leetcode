# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        
        p1 = None
        p2 = head.next
        
        while head:
            head.next = p1
            p1 = head
            head = p2
            if p2:
                p2 = p2.next
        
        return p1

    