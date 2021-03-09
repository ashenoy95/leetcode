# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        
        queue = deque([root])
        level_order = []

        while queue:
            # l keeps tracks of how many nodes in queue at a certain level because only immediate children will be in queue
            # level_indicator increments every time a node is processed 
            # when l == level_indicator, it means all nodes in a level are processed
            l = len(queue)
            level_indicator = 0
            level = []

            while level_indicator < l:
                node = queue.popleft()
                level.append(node.val)
                level_indicator += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_order.append(level)
            
        
        return level_order
        
