"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def _traverse(self, node):
      """
      Helper function to traverse LL to the right till NULL
      """
        while node.next:
            node = node.next
        
        return node
    
    
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node:
            if node.child:
                child_tail = self._traverse(node.child)
                
                node.child.prev = node
                child_tail.next = node.next
                
                if node.next:
                    node.next.prev = child_tail
                    
                node.next = node.child

                node.child = None
                
            node = node.next
            
        return head
                
