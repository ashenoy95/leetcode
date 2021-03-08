# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head:
            if head.val == val:
                head = head.next
            else:
                break
                
        node = head        
        if not node:
            return head
        
        while node.next:
            if node.next.val == val:
                # temp = node.next
                node.next = node.next.next
            else:
                node = node.next
                
        return head        
