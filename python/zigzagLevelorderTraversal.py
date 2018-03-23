# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        level_order = []
        level = []
        items = 1
        zigzag = False
        
        while q:
            node = q.pop(0)
            items -= 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
            if items==0:
                if zigzag:
                    level_order.append(level[::-1])
                    zigzag = False
                else:
                    level_order.append(level)
                    zigzag = True
                # empty level only when all nodes in that level are visited
                level = []  
                items = len(q)
        return level_order