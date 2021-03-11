# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_side_view = []
        q = deque()
        if root:
            q.append(root)

        while q:
            ctr = 0
            q_len = len(q)
            
            while ctr < q_len:
                node = q.popleft()
                ctr += 1
                
                if ctr == q_len:
                    right_side_view.append(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return right_side_view
    
