# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        slow = head
        fast = head
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        # when len is odd, slow will be at mid    
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val!=stack[-1]:
                return False
            slow = slow.next
            stack.pop()
        
        return True