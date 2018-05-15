# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        first_even = head.next
        node = head
        
        while node.next:
            even = node.next
            if not node.next.next:
                break
            node.next = node.next.next
            node = node.next
            even.next = node.next
            
        node.next = first_even
        
        return head