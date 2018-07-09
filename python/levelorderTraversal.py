# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            q = [root]
        level_order = []
        
        while q:
            level_order.append([node.val for node in q])

            curr_level = [node for node in q]
            q = []
            for node in curr_level:
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
            
        return level_order    