# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        left_head = ListNode(None)
        left_tail = ListNode(None)
        right_head = ListNode(None)
        right_tail = ListNode(None)
        
        while head:
            node = head.next
            head.next = None
            
            if head.val<x:
                if left_head.val==None:
                    left_head = head
                    left_tail = left_head
                else:
                    left_tail.next = head
                    left_tail = head
            else:
                if right_head.val==None:
                    right_head = head
                    right_tail = right_head
                else:
                    right_tail.next = head
                    right_tail = head
                    
            head = node
            
        if left_head.val==None:
            return right_head
        
        if right_head.val!=None:
            left_tail.next = right_head
            
        return left_head