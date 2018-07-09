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
            for succ in curr_level:
                if succ.left:
                    q.append(succ.left) 
                if succ.right:
                    q.append(succ.right)
            
        return level_order