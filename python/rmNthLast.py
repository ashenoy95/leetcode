# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def traverse(self, head, prev, n):
        node = head
        for i in range(n):
            head = head.next
        if not head:
            return node, prev
        return self.traverse(node.next, node, n)
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node, prev = self.traverse(head, head, n)
        if prev==node:  
            return head.next   
        prev.next = node.next
        return head