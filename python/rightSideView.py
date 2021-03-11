# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
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
    
    # DSF    
    def _dfs(self, root, level, level_max, right_side_view):
        if not root:
            return root
        
        if level > level_max:
            right_side_view.append(root.val)
            
        self._dfs(root.right, level+1, len(right_side_view), right_side_view)
        self._dfs(root.left, level+1, len(right_side_view), right_side_view)
        
    
    def rightSideView_dfs(self, root: TreeNode) -> List[int]:
        right_side_view = []
        node = root
        while node:
            right_side_view.append(node.val)
            node = node.right
            
        self._dfs(root, level=1, level_max=len(right_side_view), right_side_view=right_side_view)
        
        return right_side_view
